# Zotero Setup — Deprecated

This file previously described Zotero MCP integration for lit-synthesis. That mode has been removed.

## Current Approach: Local Library Pipeline

lit-synthesis now uses a single local-library mode. Papers are accessed as markdown files converted from PDFs alongside a `references.bib` file for bibliographic metadata.

### How to Get Started

1. **Export your references** as BibTeX to `references.bib` (lit-search produces this automatically; or export from your reference manager).

2. **Convert PDFs to markdown** using the ingest script:
   ```bash
   uv run plugins/sociology-skillset/scripts/ingest.py --file /path/to/paper.pdf
   ```
   Converted files land in `library/markdown/`, metadata added to `references.bib`.

3. **Run lit-synthesis** — it reads directly from `library/markdown/` and `references.bib`. No MCP server required.

See `skills/lit-synthesis/SKILL.md` for the full workflow.
