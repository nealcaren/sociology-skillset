# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A Claude Code plugin marketplace containing the `sociology-skillset` plugin — 24 markdown-based skills for academic sociology writing covering qualitative, quantitative, and mixed methods research. No build system, no compiled code; skills are structured markdown files that Claude Code loads as instructions.

## Repository Layout

```
.claude-plugin/marketplace.json          # Marketplace catalog (version + plugin list)
plugins/sociology-skillset/
  plugin.json                            # Plugin manifest (version must match marketplace.json)
  skills/[skill-name]/
    SKILL.md                             # Skill definition (YAML frontmatter + instructions)
    phases/                              # Phase-specific guides (phase0-intake.md, etc.)
    clusters/ or pathways/               # Empirically-derived style variants
    techniques/                          # Craft reference guides
to-add/                                  # Work-in-progress skills not yet released
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
- Qualitative: `lit-search` → `lit-synthesis` → `argument-builder` → `interview-analyst` → `qual-findings-writer` → `article-bookends`
- Quantitative: `lit-search` → `lit-synthesis` → `argument-builder` → `r-analyst`/`stata-analyst` → `quant-findings-writer` → `article-bookends`
- Mixed: Both qualitative and quantitative strands → `mixed-methods-findings-writer` → `article-bookends`

**Three project types**: qualitative, quantitative, and mixed methods. Skills check project type from `project.yaml` and adapt their workflows accordingly.

**Zotero integration**: `zotero` and `zotero-rag` skills wrap the `mcp-zotero` MCP server (separate package at `nealcaren/mcp-zotero`). Both include first-run checks that detect whether the server is installed.

## Publishing Updates

See `PUBLISHING.md` for the full process. The critical rule: **versions must match** in both `plugin.json` and `marketplace.json`. After pushing, update the local marketplace with `/plugin marketplace update sociology-skillset`.

## Version Sync Checklist

When bumping versions or adding/removing skills, update:
1. `plugins/sociology-skillset/plugin.json` — `version` and `description`
2. `.claude-plugin/marketplace.json` — `version` and `description`

Both description fields should list the current skill count and names.

## Current Skills (25)

**Zotero**: zotero, zotero-rag
**Literature**: lit-search, lit-synthesis, reading-agent, argument-builder
**Qualitative analysis**: interview-analyst
**Quantitative analysis**: r-analyst, stata-analyst
**Text classification**: prompt-optimizer
**Findings writing**: qual-findings-writer, quant-findings-writer, mixed-methods-findings-writer
**Manuscript sections**: methods-writer, case-justification, article-bookends, abstract-builder
**Revision**: verifier, peer-reviewer, revision-coordinator, writing-editor, bibliography-builder
**Meta**: genre-skill-builder, project-scaffold, research-coordinator
