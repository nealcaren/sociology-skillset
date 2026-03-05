# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A Claude Code plugin marketplace containing two plugins:
- **`sociology-skillset`** — 27 markdown-based skills for academic sociology research covering qualitative, quantitative, and mixed methods workflows.
- **`socibook-skillset`** — 10 skills for planning and drafting book-length scholarly monographs, grounded in genre analysis of political sociology and American politics monographs.

No build system, no compiled code; skills are structured markdown files that Claude Code loads as instructions.

## Repository Layout

```
.claude-plugin/marketplace.json          # Marketplace catalog (version + plugin list)
plugins/
  sociology-skillset/
    plugin.json                          # Plugin manifest (version must match marketplace.json)
    skills/[skill-name]/
      SKILL.md                           # Skill definition (YAML frontmatter + instructions)
      phases/                            # Phase-specific guides (phase0-intake.md, etc.)
      clusters/ or pathways/             # Empirically-derived style variants
      techniques/                        # Craft reference guides
  socibook-skillset/
    plugin.json                          # Plugin manifest for monograph writing
    skills/[skill-name]/
      SKILL.md
      phases/
      clusters/
```

## Skill Anatomy

Each skill has a `SKILL.md` with YAML frontmatter:
```yaml
---
name: skill-name
description: One-line description shown in /help
---
```

Skills follow a **phase-based workflow** pattern: numbered phases with pause points for user review. Writing skills use **cluster-based guidance** derived from corpus analysis of Social Problems and Social Forces articles.

## Key Architectural Patterns

**Project coordination**: Skills read/write `project.yaml` (canonical paths, metadata) and `progress.yaml` (workflow state, artifact registry) in the user's research project directory. The `project-scaffold` skill creates these files; `research-coordinator` orchestrates the full workflow across skills.

**Skill composition**: Skills chain together with documented inputs/outputs. Example chains:
- Qualitative: `lit-search` → `lit-synthesis` → `contribution-framer` → `argument-builder` → `interview-analyst` → `qual-findings-writer` → `article-bookends`
- Quantitative: `lit-search` → `lit-synthesis` → `contribution-framer` → `argument-builder` → `r-analyst`/`stata-analyst` → `quant-findings-writer` → `article-bookends`
- Mixed: Both qualitative and quantitative strands → `contribution-framer` → `mixed-methods-findings-writer` → `article-bookends`

**Three project types**: qualitative, quantitative, and mixed methods. Skills check project type from `project.yaml` and adapt their workflows accordingly.

**Local BibTeX pipeline**: `references.bib` serves as the canonical metadata store for each project, with PDFs/EPUBs in `library/pdfs/` and converted markdown in `library/markdown/`. The `ingest.py` script handles adding new papers (with Crossref/Open Library metadata lookup), and `migrate-zotero.py` supports one-time migration from exported Zotero libraries. The `zotero` and `zotero-rag` skills are deprecated.

**Bibliography generation**: Use `pandoc --citeproc` with a CSL style file to produce formatted reference lists from `references.bib`. This applies to the `bibliography-builder` skill (Phase 4) and the `argument-builder` skill (Phase 5). Pandoc handles name formatting, sorting, punctuation, and all style-specific rules via CSL files (ASA, APA, Chicago, etc.).

## Publishing Updates

See `PUBLISHING.md` for the full process. The critical rule: **versions must match** in both `plugin.json` and `marketplace.json`. After pushing, update the local marketplace with `/plugin marketplace update sociology-skillset`.

## Version Sync Checklist

When bumping versions or adding/removing skills, update the plugin's `version` and `description` in **both** its `plugin.json` and `.claude-plugin/marketplace.json`. The `description` field is duplicated verbatim between the two files — it must list the current skill count and all skill names grouped by category. Keep descriptions identical.

For `sociology-skillset`: update `plugins/sociology-skillset/plugin.json` and `marketplace.json` `plugins[0]`.
For `socibook-skillset`: update `plugins/socibook-skillset/plugin.json` and `marketplace.json` `plugins[1]`.

Also update the "Current Skills" section below and the skill count in this file's opening paragraph.

## Adding a New Skill

1. Create `plugins/sociology-skillset/skills/<skill-name>/SKILL.md` with YAML frontmatter (`name`, `description`)
2. Add phase files in `phases/` subdirectory if the skill uses phased workflows
3. Add cluster/pathway files if the skill offers style variants
4. Update skill count and skill list in: this file (CLAUDE.md), `plugin.json`, and `marketplace.json`
5. Bump the version in both `plugin.json` and `marketplace.json`
6. Use `genre-skill-builder` to create new writing skills from corpus analysis

## Current Skills

### sociology-skillset (27 skills)

**Reference management**: zotero [deprecated], zotero-rag (local library RAG)
**Literature**: lit-search, lit-synthesis, reading-agent, argument-builder
**Qualitative analysis**: interview-analyst
**Quantitative analysis**: r-analyst, stata-analyst
**Computational text analysis**: text-analyst
**Text classification**: prompt-optimizer
**Findings writing**: qual-findings-writer, quant-findings-writer, mixed-methods-findings-writer
**Manuscript sections**: methods-writer, case-justification, contribution-framer, article-bookends, abstract-builder
**Revision**: verifier, peer-reviewer, revision-coordinator, writing-editor, bibliography-builder
**Meta**: genre-skill-builder, project-scaffold, research-coordinator

### socibook-skillset (10 skills)

**Architecture**: book-architecture
**Chapter writing**: book-introduction, book-theory-chapter, book-context-chapter, book-parallel-case, book-cross-issue, book-quant-chapter, book-conclusion
**Revision**: book-editor, book-continuity
