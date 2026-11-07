# The Ultimate MoE Training Handbook

By Nouamane Tazi, Leandro von Werra, and Thomas Wolf (Hugging Face), published November 5, 2026.

[Original Space](https://huggingface.co/spaces/huggingface/moe-blogpost) · Revision `ef70726e6f8b99d74298a16a4894340f288a58c2`

- [1. Introduction](chapters/1-introduction.md)
- [2. Setup and your first run](chapters/2-setup-and-your-first-run.md)
- [3. Anatomy of MoE Training](chapters/3-anatomy-of-moe-training.md)
- [4. From training to serving](chapters/4-from-training-to-serving.md)
- [5. Conclusion](chapters/5-conclusion.md)
- [Appendix](chapters/A-appendix.md)

- [Citation evidence](citation-evidence.md)
- [Preservation report](preservation-report.json)
- [Provenance and checksums](provenance.json)
- [Complete upstream snapshot](upstream/)

The chapters preserve the handbook’s text, tables, code and references. Figure pages expose rendered knowledge and controls; the complete original interactive code, datasets and posters are retained under `upstream/app/public`. To run figures offline, serve that directory with `python3 -m http.server --directory src/upstream/app/public 8000`, then open `http://localhost:8000/viz/index.html`. No training jobs are needed to read this skill.

Original conversion tooling and skill instructions are licensed under the [MIT License](../LICENSE). This license does not relicense third-party handbook material, including its vendored files, converted text, assets, and derived excerpts. Source material retains its authorship and any supplied notices; the pinned Space supplies no explicit license file. Original MDX and site files are retained verbatim for audit and recovery.
