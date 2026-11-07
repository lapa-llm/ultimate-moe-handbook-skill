#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright==1.56.0"]
# ///
"""Capture searchable figure content; retain exact interactive code separately.

Run after convert.py: uv run scripts/capture_figures.py
Install the browser once: uv run --with playwright==1.56.0 playwright install chromium
"""
import functools
import gzip
import io
import http.server
import json
from pathlib import Path
import re
import threading

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "src/upstream/app/public"
if not PUBLIC.is_dir():
    PUBLIC = ROOT / ".upstream/moe-blogpost/app/public"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def main():
    bundle = next((PUBLIC / "viz/assets").glob("index-*.js")).read_text()
    modules = dict(re.findall(
        r'"\./components/([^"/]+)\.ts":\(\)=>\w+\(\(\)=>import\(`\./([^`]+)`\)', bundle
    ))
    assert modules, "Cannot discover gallery modules"
    handler = functools.partial(QuietHandler, directory=str(PUBLIC))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    captures = {}
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": 1600, "height": 1200})
            page.goto(f"http://127.0.0.1:{server.server_port}/robots.txt")
            # One chapter contains a script-generated token-file diagram outside the gallery.
            source = (ROOT / ".upstream/moe-blogpost/app/src/content/chapters/2-setup-and-your-first-run.mdx").read_text()
            fragments = re.findall(r'<Fragment\s+set:html=\{("(?:[^"\\]|\\.)*")\}\s*/>', source)
            page.set_content("".join(json.loads(x) for x in fragments))
            diagram = page.locator(".megatron-tokenization-format svg").evaluate("el => el.outerHTML")
            (ROOT / "src").mkdir(exist_ok=True)
            (ROOT / "src/embedded-captures.json").write_text(json.dumps({"megatron-tokenization-format": diagram}, ensure_ascii=False, indent=2) + "\n")
            page.goto(f"http://127.0.0.1:{server.server_port}/robots.txt")
            for name, filename in sorted(modules.items()):
                captures[name] = page.evaluate("""async (filename) => {
                  const m = await import('/viz/assets/' + filename);
                  if (typeof m.render !== 'function') throw Error('Missing render: ' + filename);
                  const params = m.params || {};
                  const defaults = Object.fromEntries(Object.entries(params).map(([k,v])=>[k,v.value]));
                  const el = document.createElement('div'); document.body.append(el);
                  const clean = () => {
                    const copy = el.cloneNode(true);
                    copy.querySelectorAll('script,style').forEach(n=>n.remove());
                    // KaTeX includes both readable MathML and a duplicate visual representation.
                    copy.querySelectorAll('.katex-html').forEach(n=>n.remove());
                    copy.querySelectorAll('annotation').forEach(n=>n.replaceWith(n.textContent));
                    return copy;
                  };
                  const render = state => {
                    el.innerHTML = ''; m.render(el, {...defaults, ...state});
                    const copy = clean();
                    return {state, html: copy.innerHTML,
                      text: copy.textContent.replace(/\\s+/g,' ').trim()};
                  };
                  const states = [{t:0}];
                  if (m.duration) states.push({t:m.duration/2},{t:m.duration});
                  for (const [k,v] of Object.entries(params)) {
                    const count = Math.round((v.max-v.min)/v.step);
                    const values = count <= 12 ? Array.from({length:count+1},(_,i)=>v.min+i*v.step)
                      : [v.min, (v.min+v.max)/2, v.max];
                    for (const value of values) states.push({[k]:value,t:0});
                  }
                  // The gallery itself uses 0.1s sampling for its narrative step discovery.
                  let previous = '';
                  if (m.duration) for (let t=0;t<=m.duration+0.001;t+=0.1) {
                    el.innerHTML=''; m.render(el,{...defaults,t});
                    const narrative = [...el.querySelectorAll('[aria-live]')]
                      .map(n=>n.textContent.replace(/Step \\d+ of \\d+\\.?\\s*/g,'')).join(' ');
                    if (narrative && narrative !== previous) { states.push({t:Number(t.toFixed(2))}); previous=narrative; }
                  }
                  const seen = new Set(), samples=[];
                  for (const state of states) {
                    const sample=render(state);
                    if (!seen.has(sample.text)) { seen.add(sample.text); samples.push(sample); }
                  }
                  el.remove();
                  return {module:filename,params,duration:m.duration||null,samples};
                }""", filename)
                print(f"Captured {name}: {len(captures[name]['samples'])} distinct samples", flush=True)
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    path = ROOT / "src/figure-captures.json.gz"
    # GzipFile fixes filename, timestamp and OS metadata across Python versions.
    buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=buffer, mode="wb", filename="", mtime=0) as archive:
        archive.write((json.dumps(captures, ensure_ascii=False, indent=2) + "\n").encode())
    path.write_bytes(buffer.getvalue())
    print(f"Wrote {len(captures)} figures to {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
