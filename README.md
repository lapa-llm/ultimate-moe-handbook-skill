# Ultimate MoE Handbook Skill

A training advisor built from Hugging Face’s [The Ultimate MoE Training Handbook](https://huggingface.co/spaces/huggingface/moe-blogpost), by Nouamane Tazi, Leandro von Werra, and Thomas Wolf. It helps plan MoE runs, review configurations, and diagnose common failures across frameworks, with version-specific Megatron recipes.

Keep the complete repository together in your agent’s skills directory. [SKILL.md](SKILL.md) is the entrypoint; the [handbook index](src/index.md) contains the full converted source, and the [troubleshooting index](references/troubleshooting.md) covers 42 symptoms. Runtime advice only needs the local files; no Python dependencies, browser, cluster, or network are required to read them.

Example requests:

- “Use $ultimate-moe-handbook to diagnose low throughput despite auxiliary loss near 1.”
- “Review this MoE config for stability, memory and communication pitfalls.”
- “Adapt the handbook’s load-balancing guidance to my framework and GPU layout.”

## Reproduce the source conversion

The upstream revision is pinned to `ef70726e6f8b99d74298a16a4894340f288a58c2`. Conversion tools require Python 3.11+ and [uv](https://docs.astral.sh/uv/); inline dependency versions are pinned in each script.

```bash
python3 scripts/fetch_upstream.py
uv run scripts/convert.py
uv run --with playwright==1.56.0 playwright install chromium
uv run scripts/capture_figures.py
uv run scripts/convert.py
uv run scripts/verify.py
uv run tests/test_conversion.py
uv run scripts/convert.py --check
```

The ignored clone lives in `.upstream/moe-blogpost`. The committed `src/upstream` snapshot retains all 371 original files, including hydrated large-file assets; conversion verifies them against pinned Git objects and LFS hashes. A generated `app/.gitattributes` override prevents inherited LFS rules from turning vendored assets back into pointers.

All six chapters, 158 code blocks, 15 tables, 300 citation popovers, 55 interactive figure explanations and the script-generated token-file diagram are preserved. Figure pages expose sampled states and controls; exact implementations, datasets and posters remain available locally. Sampling does not enumerate every continuous value or combination. [Provenance](src/provenance.json) records file checksums, and the [preservation report](src/preservation-report.json) inventories the conversion.

To view the original interactive figures offline:

```bash
python3 -m http.server --directory src/upstream/app/public 8000
```

Open `http://localhost:8000/viz/index.html`. The added skill guidance distinguishes handbook findings from adaptations and verifies exact software flags before transferring recipes to another version.

## License

Original skill instructions and tooling are licensed under the [MIT License](LICENSE), copyright 2026 Yurii Paniv. This license does not relicense third-party handbook material, including its vendored files, converted text, assets, and derived excerpts. That material retains its authorship and supplied notices; the pinned Space contains no explicit license file.
