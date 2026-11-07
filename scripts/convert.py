#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4==4.14.3", "markdownify==1.2.2"]
# ///
"""Convert the pinned Space without evaluating MDX or dropping unknown content.

uv run scripts/convert.py [--check]
The ignored clone is the input; src/upstream is a complete tracked-file snapshot.
Run capture_figures.py once after conversion, then rerun conversion for figure text.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess

from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter

ROOT = Path(__file__).resolve().parents[1]
CLONE = ROOT / ".upstream/moe-blogpost"
SHA = "ef70726e6f8b99d74298a16a4894340f288a58c2"
URL = "https://huggingface.co/spaces/huggingface/moe-blogpost"
FRAGMENT = re.compile(r'<Fragment\s+set:html=\{("(?:[^"\\]|\\.)*")\}\s*/>')
VIZ = re.compile(r'<Viz\b[^>]*\s*/>')
CHAPTERS = [
    "1-introduction", "2-setup-and-your-first-run", "3-anatomy-of-moe-training",
    "4-from-training-to-serving", "5-conclusion", "A-appendix",
]
ALLOWED_TAGS = set("a b blockquote br button code dd defs desc details div dl dt em figcaption figure g h1 h2 h3 h4 h5 h6 hr html i img li line marker ol p path polygon polyline pre rect section script span strong style sub summary sup svg table tbody td text th thead title tr tspan ul".split())


def soup(text):
    return BeautifulSoup(text, "html.parser")


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def digest(data):
    return hashlib.sha256(data).hexdigest()


class Converter(MarkdownConverter):
    def convert_a(self, el, text, parent_tags):
        if el.get("id"):
            return f'<a id="{el["id"]}"></a>'
        return super().convert_a(el, text, parent_tags)

    def convert_summary(self, el, text, parent_tags):
        return f"\n\n**{text.strip()}**\n\n"

    def convert_sup(self, el, text, parent_tags):
        return text

    def convert_span(self, el, text, parent_tags):
        if "sn" in el.get("class", []):
            return f" {text.strip()} "
        return text

    def convert_pre(self, el, text, parent_tags):
        value = el.get_text()
        fence = "`" * max(3, max((len(x) + 1 for x in re.findall(r"`+", value)), default=3))
        return f"\n\n{fence}\n{value.rstrip(chr(10))}\n{fence}\n\n"

    def convert_svg(self, el, text, parent_tags):
        # Preserve labels, descriptions and nested tspan text, without geometric markup.
        labels = [self.escape(normalize(n.get_text(" ")), parent_tags) for n in el.find_all(["title", "desc", "text"])]
        return "\n\n" + "\n\n".join(labels) + "\n\n"


def markdown(tree):
    return Converter(heading_style="ATX", escape_underscores=True, escape_asterisks=True,
                     escape_misc=True, bullets="-", table_infer_header=True).convert_soup(tree).strip() + "\n"


def code_text(pre):
    lines = pre.select("span.line")
    if lines:
        result = []
        for line in lines:
            code = line.select_one("span.code")
            assert code is not None, "Source line without code span"
            match = re.search(r"--i:\s*(\d+)ch", code.get("style", ""))
            assert match, "Source indentation missing"
            result.append(" " * int(match[1]) + code.get_text())
        return "\n".join(result)
    return pre.get_text()


def prepare(tree, ids, popups):
    unknown = {x.name for x in tree.find_all()} - ALLOWED_TAGS
    assert not unknown, f"Unhandled HTML elements: {unknown}"
    for script in list(tree.find_all("script")):
        if script.get("type") == "application/json":
            data = json.loads(script.string or script.get_text())
            assert isinstance(data, dict), "Unexpected script data"
            for key, value in data.items():
                assert key not in popups, f"Duplicate citation key {key}"
                popups[key] = value
        elif not any(x in script.get_text() for x in ["document.currentScript", "fn-pop", "copy-code"]):
            raise AssertionError("Unhandled script; preserve its knowledge explicitly")
        script.decompose()
    for item in list(tree.select("style, .code-toolbar")):
        item.decompose()
    captures = ROOT / "src/embedded-captures.json"
    if captures.exists():
        for css_class, html in json.loads(captures.read_text()).items():
            for container in tree.select("." + css_class):
                container.clear()
                container.append(soup(html))
    # Keep the relationship between numbered citations and their detailed evidence cards.
    for sup in tree.find_all("sup"):
        keys = sup.get("data-k", "").split()
        for a in sup.select("a[data-ks]"):
            keys.extend(a["data-ks"].split())
        for key in dict.fromkeys(keys):
            sup.append(NavigableString(" "))
            link = tree.new_tag("a", href=f"../citation-evidence.md#{key}") if isinstance(tree, BeautifulSoup) else soup(f'<a href="../citation-evidence.md#{key}">evidence</a>').a
            link.string = "evidence"
            sup.append(link)
    # Code line numbers are presentation; indentation is stored in CSS custom properties.
    for pre in tree.find_all("pre"):
        value = code_text(pre)
        pre.clear()
        pre.append(NavigableString(value))
    for item in tree.find_all(id=True):
        if item.name not in ["script", "style"]:
            anchor = soup(f'<a id="{item["id"]}"></a>').a
            item.insert_before(anchor)
            del item["id"]
    for a in tree.find_all("a", href=True):
        href = a["href"]
        if href.startswith("#") and href[1:] in ids:
            a["href"] = ids[href[1:]] + href
        elif href.startswith("#") and not a.get("id"):
            raise AssertionError(f"Unknown source anchor {href}")
        elif href.startswith("/") and not href.startswith("//"):
            a["href"] = "../upstream/app/public" + href
    for img in tree.find_all("img", src=True):
        if img["src"].startswith("/"):
            img["src"] = "../upstream/app/public" + img["src"]
    return tree


def decode_mdx(raw):
    parts = []
    pos = 0
    pattern = re.compile(f"(?:{FRAGMENT.pattern})|(?:{VIZ.pattern})")
    for match in pattern.finditer(raw):
        gap = re.sub(r'^import [^\n]*\n?', '', raw[pos:match.start()], flags=re.M).strip()
        assert not gap, f"Unhandled MDX: {gap[:100]}"
        if match.group().startswith("<Fragment"):
            parts.append(("html", json.loads(FRAGMENT.fullmatch(match.group())[1])))
        else:
            attrs = dict(re.findall(r'(\w+)="([^"]*)"', match.group()))
            assert "name" in attrs, "Unnamed figure"
            parts.append(("viz", attrs))
        pos = match.end()
    assert not raw[pos:].strip(), "Trailing MDX content"
    return parts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Compare regenerated files without writing")
    args = parser.parse_args()
    outputs = {}
    def emit(path, value):
        outputs[path] = value.encode() if isinstance(value, str) else value
    def emit_json(path, value):
        emit(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")

    assert subprocess.check_output(["git", "-C", str(CLONE), "rev-parse", "HEAD"], text=True).strip() == SHA, "Wrong upstream revision"
    tracked = subprocess.check_output(["git", "-C", str(CLONE), "ls-tree", "-rz", "--name-only", "HEAD"]).decode().split("\0")
    tracked = list(filter(None, tracked))
    refs = "".join(f"HEAD:{name}\n" for name in tracked).encode()
    blobs = subprocess.check_output(["git", "-C", str(CLONE), "cat-file", "--batch"], input=refs)
    offset = 0
    files = []
    for name in tracked:
        end = blobs.index(b"\n", offset)
        oid, kind, size = blobs[offset:end].split()
        assert kind == b"blob", f"Unexpected object: {name}"
        offset = end + 1
        original = blobs[offset:offset + int(size)]
        offset += int(size) + 1
        data = (CLONE / name).read_bytes()
        assert not data.startswith(b"version https://git-lfs.github.com/spec/v1"), f"Unfetched LFS asset: {name}"
        if original.startswith(b"version https://git-lfs.github.com/spec/v1"):
            expected = re.search(rb"oid sha256:([a-f0-9]{64})", original)[1].decode()
            expected_size = int(re.search(rb"size (\d+)", original)[1])
            assert digest(data) == expected and len(data) == expected_size, f"LFS integrity failure: {name}"
        else:
            assert data == original, f"Upstream checkout differs from pinned Git object: {name}"
        emit("src/upstream/" + name, data)
        files.append({"path": name, "git_blob": oid.decode(), "bytes": len(data), "sha256": digest(data)})
    emit_json("src/provenance.json", {"url": URL, "revision": SHA, "files": files})
    assert "app/.gitattributes" not in tracked, "Attribute override would replace an upstream file"
    emit("src/upstream/app/.gitattributes", "# Added by the conversion: retain vendored bytes in ordinary Git.\n* -filter -text !diff !merge\n")

    sources = {name: decode_mdx((CLONE / f"app/src/content/chapters/{name}.mdx").read_text()) for name in CHAPTERS}
    ids, titles = {}, {}
    for name, parts in sources.items():
        h = soup("".join(v for k, v in parts if k == "html"))
        titles[name] = h.find("h2").get_text()
        for el in h.find_all(id=True):
            assert el["id"] not in ids, f"Duplicate source id: {el['id']}"
            ids[el["id"]] = name + ".md"
    captures_path = ROOT / "src/figure-captures.json.gz"
    captures = json.loads(gzip.decompress(captures_path.read_bytes())) if captures_path.exists() else {}
    popups, report, figure_refs = {}, {}, []
    for name, parts in sources.items():
        chunks = [f"> Source: [Hugging Face handbook]({URL}/blob/{SHA}/app/src/content/chapters/{name}.mdx), revision `{SHA}`.\n"]
        facts = {"fragments": 0, "headings": 0, "tables": 0, "code_blocks": 0, "figures": 0}
        for kind, value in parts:
            if kind == "viz":
                fig = value["name"]
                label = value.get("caption", fig)
                query = value.get("query", "")
                assert (CLONE / f"app/public/viz/posters/{fig}.webp").exists(), f"Missing poster: {fig}"
                chunks.append(f"\n\n**{label}**\n\n![{fig}](../upstream/app/public/viz/posters/{fig}.webp)\n\n[Figure explanation, controls and captured states](../figures/{fig}.md) · [Interactive original](../upstream/app/public/viz/index.html?c={fig}{query})\n")
                figure_refs.append(fig)
                facts["figures"] += 1
                continue
            tree = soup(value)
            facts["fragments"] += 1
            facts["headings"] += len(tree.find_all(re.compile(r"^h[1-6]$")))
            facts["tables"] += len(tree.find_all("table"))
            facts["code_blocks"] += len(tree.find_all("pre"))
            prepared = prepare(tree, ids, popups)
            rendered = markdown(prepared)
            # Exact code content must survive; broad text checks are in verify.py.
            for pre in prepared.find_all("pre"):
                assert pre.get_text().rstrip("\n") in rendered, f"Code changed in {name}"
            chunks.append(rendered)
        emit(f"src/chapters/{name}.md", "\n\n".join(chunks).strip() + "\n")
        report[name] = facts

    popup_chunks = ["# Citation evidence\n\nThese are the handbook’s citation popovers, preserved as searchable Markdown. Quotations and findings below are attributed to the original cited sources; they are not additional skill instructions.\n"]
    for key, value in popups.items():
        # Appendix popup links use source-global IDs.
        popup_chunks.append(f'<a id="{key}"></a>\n\n## {key}\n\n' + markdown(prepare(soup(value), ids, {})))
    emit("src/citation-evidence.md", "\n\n".join(popup_chunks))

    # Turn the existing reverse index into a directly accessible troubleshooting reference.
    appendix = soup("".join(v for k, v in sources["A-appendix"] if k == "html"))
    table = appendix.find("table")
    rows = table.select("tbody tr")
    assert len(rows) == 42, f"Expected 42 debugging symptoms, got {len(rows)}"
    debug = "# Troubleshooting index\n\nStart with the first signal that changed. Check stack correctness using the two sanity checks in [§2.5](../src/chapters/2-setup-and-your-first-run.md#s-2-5), then follow the linked handbook explanation. Symptoms suggest hypotheses, not proven causes.\n\n"
    # The source's RL row names its section without a hyperlink; make it navigable.
    for row in rows:
        cell = row.find_all("td")[-1]
        if cell.get_text() == "4 RL routing":
            cell.clear()
            a = appendix.new_tag("a", href="#s-4-rl-routing")
            a.string = "4 RL routing"
            cell.append(a)
    debug += markdown(prepare(table, ids, {})).replace("](", "](../src/chapters/")
    debug += "\nRead the full [debugging commentary](../src/chapters/A-appendix.md#s-a-2) and [measurement limits](../src/chapters/A-appendix.md#s-a-1) before interpreting metrics.\n"
    emit("references/troubleshooting.md", debug)

    for name in sorted(set(figure_refs) | captures.keys()):
        capture = captures.get(name)
        intro = f"# {name}\n\n[Interactive original](../upstream/app/public/viz/index.html?c={name}) · [Poster](../upstream/app/public/viz/posters/{name}.webp)\n\n"
        if not capture:
            emit(f"src/figures/{name}.md", intro + "Capture pending: run `scripts/capture_figures.py` and rerun conversion.\n")
            continue
        intro += "The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.\n\n"
        intro += f"[Calculation and rendering source](../upstream/app/public/viz/assets/{capture['module']})\n\n## Controls\n\n```json\n" + json.dumps(capture["params"], ensure_ascii=False, indent=2) + "\n```\n"
        if capture["duration"]:
            intro += f"\nAnimation duration: {capture['duration']} seconds. Samples include narrative transitions.\n"
        for i, sample in enumerate(capture["samples"], 1):
            # SVG formulas retain labels; HTML tables and KaTeX TeX remain searchable.
            tree = soup(sample["html"])
            for el in list(tree.find_all(["script", "style"])):
                el.decompose()
            for el in list(tree.find_all(["math", "semantics"])):
                el.unwrap()
            body = markdown(tree)
            intro += f"\n## Sample {i}\n\nParameters: `{json.dumps(sample['state'], sort_keys=True)}`\n\n{body}"
        emit(f"src/figures/{name}.md", intro)

    index = f"# The Ultimate MoE Training Handbook\n\nBy Nouamane Tazi, Leandro von Werra, and Thomas Wolf (Hugging Face), published November 5, 2026.\n\n[Original Space]({URL}) · Revision `{SHA}`\n\n"
    index += "\n".join(f"- [{titles[n]}](chapters/{n}.md)" for n in CHAPTERS)
    index += "\n\n- [Citation evidence](citation-evidence.md)\n- [Preservation report](preservation-report.json)\n- [Provenance and checksums](provenance.json)\n- [Complete upstream snapshot](upstream/)\n\n"
    index += "The chapters preserve the handbook’s text, tables, code and references. Figure pages expose rendered knowledge and controls; the complete original interactive code, datasets and posters are retained under `upstream/app/public`. To run figures offline, serve that directory with `python3 -m http.server --directory src/upstream/app/public 8000`, then open `http://localhost:8000/viz/index.html`. No training jobs are needed to read this skill.\n\n"
    index += "Original conversion tooling and skill instructions are licensed under the [MIT License](../LICENSE). This license does not relicense third-party handbook material, including its vendored files, converted text, assets, and derived excerpts. Source material retains its authorship and any supplied notices; the pinned Space supplies no explicit license file. Original MDX and site files are retained verbatim for audit and recovery.\n"
    emit("src/index.md", index)
    emit_json("src/preservation-report.json", {"revision": SHA, "chapters": report, "citation_popovers": len(popups), "figure_occurrences": len(figure_refs), "unique_referenced_figures": len(set(figure_refs)), "captured_gallery_figures": len(captures), "debugging_symptoms": len(rows), "original_files": len(files), "original_bytes": sum(f["bytes"] for f in files)})

    for path, data in outputs.items():
        target = ROOT / path
        if args.check:
            assert target.is_file() and target.read_bytes() == data, f"Regeneration differs: {path}"
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    print(f"{'Checked' if args.check else 'Wrote'} {len(outputs)} files; {len(popups)} citation popovers; {len(set(figure_refs))} referenced figures")


if __name__ == "__main__":
    main()
