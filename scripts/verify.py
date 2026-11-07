#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4==4.14.3", "markdownify==1.2.2", "markdown-it-py==4.0.0"]
# ///
"""Audit source-to-Markdown preservation, local links, captures and provenance."""
import hashlib
import gzip
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

sys.path.insert(0, str(Path(__file__).resolve().parent))
import convert as c

MD = MarkdownIt("commonmark").enable("table")


def compact(value):
    return re.sub(r"\s+", "", value)


def rendered(path):
    return BeautifulSoup(MD.render(path.read_text()), "html.parser")


def check_blocks(source, target, label):
    text = compact(target.get_text())
    checked = 0
    # Compare semantic blocks after rendering Markdown, not just generated strings.
    # Leaf nodes also cover text in source divs, SVG labels and unwrapped callouts.
    blocks = list(source.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "td", "th", "summary", "pre", "figcaption", "li", "blockquote"]))
    blocks += [node for node in source.find_all(string=True) if node.strip()]
    for node in blocks:
        value = node.get_text() if hasattr(node, "get_text") else str(node)
        value = compact(value)
        if value:
            assert value in text, f"Lost or changed text in {label}: {value[:180]}"
            checked += 1
    return checked


def main():
    manifest = json.loads((c.ROOT / "src/provenance.json").read_text())
    for entry in manifest["files"]:
        data = (c.ROOT / "src/upstream" / entry["path"]).read_bytes()
        assert len(data) == entry["bytes"] and hashlib.sha256(data).hexdigest() == entry["sha256"], entry["path"]
        assert not data.startswith(b"version https://git-lfs.github.com/spec/v1"), entry["path"]

    ids, source_parts = {}, {}
    for name in c.CHAPTERS:
        raw = (c.ROOT / f"src/upstream/app/src/content/chapters/{name}.mdx").read_text()
        source_parts[name] = c.decode_mdx(raw)
        for kind, value in source_parts[name]:
            if kind == "html":
                for el in c.soup(value).find_all(id=True):
                    ids[el["id"]] = name + ".md"
    popups, total_blocks = {}, 0
    for name, parts in source_parts.items():
        target = rendered(c.ROOT / f"src/chapters/{name}.md")
        for kind, value in parts:
            if kind == "html":
                source = c.prepare(c.soup(value), ids, popups)
                total_blocks += check_blocks(source, target, name)
                for pre in source.find_all("pre"):
                    assert any(pre.get_text().rstrip("\n") == out.get_text().rstrip("\n") for out in target.find_all("pre")), f"Code formatting changed: {name}"
        print(f"Verified semantic content and code: {name}")
    evidence = rendered(c.ROOT / "src/citation-evidence.md")
    for key, value in popups.items():
        total_blocks += check_blocks(c.prepare(c.soup(value), ids, {}), evidence, f"citation {key}")

    captures = json.loads(gzip.decompress((c.ROOT / "src/figure-captures.json.gz").read_bytes()))
    for name, capture in captures.items():
        target_path = c.ROOT / f"src/figures/{name}.md"
        target = rendered(target_path)
        for sample in capture["samples"]:
            source = c.soup(sample["html"])
            for el in source.find_all(["script", "style"]):
                el.decompose()
            total_blocks += check_blocks(source, target, f"figure {name}")

    paths = [*sorted(c.ROOT.glob("*.md")), *sorted((c.ROOT / "references").glob("*.md")),
             *sorted((c.ROOT / "tests").glob("*.md")),
             c.ROOT / "src/index.md", c.ROOT / "src/citation-evidence.md",
             *sorted((c.ROOT / "src/chapters").glob("*.md")),
             *sorted((c.ROOT / "src/figures").glob("*.md"))]
    trees = {p.resolve(): rendered(p) for p in paths}
    links = 0
    for path, tree in trees.items():
        for el in tree.find_all(["a", "img"]):
            href = el.get("href") or el.get("src")
            if not href:
                continue
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            assert target.is_relative_to(c.ROOT), f"Link escapes bundle: {path}: {href}"
            assert target.exists(), f"Missing link target: {path.relative_to(c.ROOT)}: {href}"
            if url.fragment and target.suffix == ".md":
                target_tree = trees.get(target)
                if target_tree is None:
                    target_tree = rendered(target)
                assert target_tree.find(id=unquote(url.fragment)), f"Missing anchor: {path.relative_to(c.ROOT)}: {href}"
            links += 1
    debug = rendered(c.ROOT / "references/troubleshooting.md")
    assert len(debug.select("tbody tr")) == 42, "Incomplete troubleshooting index"
    report = {"upstream_files_verified": len(manifest["files"]), "semantic_blocks_and_text_nodes_verified": total_blocks,
              "local_links_verified": links, "citation_popovers_verified": len(popups),
              "gallery_figures_verified": len(captures), "debugging_symptoms_verified": 42}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
