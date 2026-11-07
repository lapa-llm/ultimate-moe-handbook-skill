#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4==4.14.3", "markdownify==1.2.2", "markdown-it-py==4.0.0"]
# ///
"""Regression cases for known ways HTML-to-Markdown conversion loses knowledge."""
from pathlib import Path
import sys
import unittest

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import convert as c


class ConversionTests(unittest.TestCase):
    def render(self, raw, ids=None, popups=None):
        prepared = c.prepare(c.soup(raw), ids or {}, popups if popups is not None else {})
        result = c.markdown(prepared)
        return BeautifulSoup(MarkdownIt("commonmark").enable("table").render(result), "html.parser")

    def test_code_indentation_is_recovered_without_line_numbers(self):
        raw = '<pre class="src"><span class="line"><span class="ln">91</span><span class="code" style="--i:0ch">if x &lt; 3:</span></span><span class="line"><span class="ln">92</span><span class="code" style="--i:4ch">print(&quot;a_b * [x]&quot;)</span></span><span class="line"><span class="ln">93</span><span class="code" style="--i:0ch"></span></span></pre>'
        self.assertEqual(self.render(raw).pre.get_text(), 'if x < 3:\n    print("a_b * [x]")\n')

    def test_plain_text_and_tex_backslashes_survive_markdown_parsing(self):
        text = r'aux_loss uses * not emphasis, [labels], and $\{2,3,4\}$; x &lt; y'
        self.assertEqual(self.render('<p>' + text + '</p>').p.get_text(), text.replace('&lt;', '<'))

    def test_expanded_details_and_cross_chapter_anchors_survive(self):
        output = self.render('<h3 id="s-3">Router</h3><details><summary>Evidence</summary><p>Read <a href="#s-a-1">monitoring</a>.</p></details>', {"s-3": "router.md", "s-a-1": "appendix.md"})
        self.assertIsNotNone(output.find(id="s-3"))
        self.assertIn('Evidence', output.get_text())
        self.assertEqual(output.find('a', string='monitoring')['href'], 'appendix.md#s-a-1')

    def test_json_citation_evidence_is_extracted_and_linked(self):
        popups = {}
        raw = '<p>Claim<sup data-k="paper"><a href="#ref-paper">1</a></sup></p><script type="application/json">{"paper":"<blockquote>Detailed evidence</blockquote>"}</script>'
        output = self.render(raw, {"ref-paper": "appendix.md"}, popups)
        self.assertEqual(popups, {"paper": "<blockquote>Detailed evidence</blockquote>"})
        self.assertEqual(output.find('a', string='evidence')['href'], '../citation-evidence.md#paper')

    def test_unknown_components_and_scripts_fail_instead_of_disappearing(self):
        with self.assertRaises(AssertionError):
            c.decode_mdx('<UnknownComponent value="knowledge" />')
        with self.assertRaises(AssertionError):
            self.render('<canvas>hidden data</canvas>')
        with self.assertRaises(AssertionError):
            self.render('<script>const trainingResults = [1,2,3]</script>')

    def test_svg_nested_labels_and_sidenotes_remain_readable(self):
        output = self.render('<p>First.<span class="sn">Aside.</span> Last.</p><svg><title>Budget</title><desc>Active versus total</desc><text>3 × 2048 = <tspan>6144</tspan></text></svg>')
        self.assertEqual(c.normalize(output.p.get_text()), 'First. Aside. Last.')
        self.assertIn('3 × 2048 = 6144', output.get_text())
        self.assertIn('Active versus total', output.get_text())


if __name__ == "__main__":
    unittest.main(verbosity=2)
