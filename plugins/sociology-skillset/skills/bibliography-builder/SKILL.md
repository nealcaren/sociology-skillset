---
name: bibliography-builder
description: Build bibliographies from manuscript citations by extracting in-text citations, matching them against a references.bib file, identifying issues, and generating a formatted reference list.
---

# Bibliography Builder

You help researchers **build bibliographies** from manuscript citations by extracting in-text citations, matching them against a local `references.bib` file, identifying issues, and generating a formatted reference list.

## Project Integration

This skill reads from `project.yaml` when available:

```yaml
# From project.yaml
paths:
  drafts: drafts/sections/
```

**Project type:** This skill works for **all project types**. Bibliography building is essential for any academic manuscript.

Updates `progress.yaml` when complete:
```yaml
status:
  bibliography: done
artifacts:
  bibliography: drafts/sections/bibliography.md
```

## File Management

This skill uses git to track progress across phases. Before modifying any output file at a new phase:
1. Stage and commit current state: `git add [files] && git commit -m "bibliography-builder: Phase N complete"`
2. Then proceed with modifications.

Do NOT create version-suffixed copies (e.g., `-v2`, `-final`, `-working`). The git history serves as the version trail.

## What This Skill Does

This is a **utility skill** that automates bibliography creation:

1. **Extract** all in-text citations from a document — supports both Pandoc `[@citationKey]` format and legacy `(Author Year)` format
2. **Match** each citation against the local `references.bib` file — direct `citationKey` lookup for Pandoc format, author+year string matching for legacy
3. **Review** for issues: missing items, ambiguous matches, duplicates
4. **Generate** a properly formatted bibliography in the requested style

## When to Use This Skill

Use this skill when you have:
- A **manuscript with in-text citations** — either Pandoc `[@citationKey]` format (from our writing skills) or legacy `(Author Year)` format
- A **`references.bib`** BibTeX file containing your library entries
- A need for a **formatted bibliography** (APA, ASA, Chicago, etc.)

**Pandoc format manuscripts** (written with our skills) get fast, deterministic matching via `citationKey` lookup directly in the `.bib` file. **Legacy format manuscripts** still work through author+year string matching against `.bib` entries.

## Requirements

- A **`references.bib`** BibTeX file containing the project's library entries. This file is typically located in the project root or a `references/` subdirectory and is populated by the local BibTeX pipeline (via `ingest.py`).
- **`pandoc`** installed with citeproc support (included by default in pandoc 2.11+). Used in Phase 4 to generate the formatted reference list.
- A **CSL style file** for the target citation style. Common styles:
  - ASA: `american-sociological-association.csl`
  - APA 7th: `apa.csl`
  - Chicago Author-Date: `chicago-author-date.csl`
  - Download from https://github.com/citation-style-language/styles if not already present. Place in project root or a `csl/` subdirectory.

## Workflow Phases

### Phase 0: Intake
**Goal**: Read the document and confirm citation style.

**Process**:
- Read the manuscript file
- Identify citation format (Author Year, Author-Year with comma, etc.)
- Count approximate citations
- Confirm output format (APA, ASA, Chicago Author-Date, etc.)

**Output**: Citation inventory with format confirmation.

> **Pause**: User confirms citation style and desired output format.

---

### Phase 1: Citation Extraction
**Goal**: Parse all in-text citations from the document.

**Process**:
- Use regex patterns to find Author-Year citations
- Handle variations:
  - Single author: `(Smith 2020)`
  - Two authors: `(Smith and Jones 2020)` or `(Smith & Jones 2020)`
  - Multiple authors: `(Smith et al. 2020)`
  - Multiple citations: `(Smith 2020; Jones 2019)`
  - Page numbers: `(Smith 2020, p. 45)` or `(Smith 2020: 45)`
  - Narrative citations: `Smith (2020) argues...`
- Deduplicate and sort alphabetically
- Create citation list with frequency counts
- **Verify with grep**: Run shell commands to independently confirm extraction caught all citations (catches edge cases like McAdam, hyphenated names, accented characters)

**Output**: Extraction results presented in conversation (not saved to a file).

> **Pause**: User reviews extracted citations for accuracy.

---

### Phase 2: BibTeX Matching
**Goal**: Find each citation in the local `references.bib` file.

**Process**:
- Read `references.bib` into memory
- For each extracted citation:
  - Pandoc format: look up `citationKey` directly against BibTeX entry keys
  - Legacy format: match author surname(s) and year against BibTeX `author` and `year` fields
  - Record match status: Found, Ambiguous, Not Found
- Build match table with BibTeX entry keys

**Output**: Match results presented in conversation (not saved to a file).

> **Pause**: User reviews matches, especially ambiguous/missing items.

---

### Phase 3: Issue Review
**Goal**: Identify and resolve problems.

**Process**:
- Flag issues:
  - **Missing**: Citations not found in `references.bib`
  - **Ambiguous**: Multiple possible matches (same author, year)
  - **Year mismatch**: Author found but year differs
  - **Name variations**: "Smith" vs "Smith, J." vs "Smith, John"
- Generate issue report with suggested actions
- User provides resolutions for ambiguous cases

**Output**: Issues presented in conversation (not saved to a file).

> **Pause**: User resolves any remaining issues.

---

### Phase 4: Bibliography Generation
**Goal**: Produce the formatted bibliography using pandoc with citeproc.

**Process**:
1. **Build a dummy markdown file** containing only the matched citation keys as pandoc citations:
   ```markdown
   ---
   bibliography: references.bib
   csl: american-sociological-association.csl
   nocite: |
     @smithHousing2020, @jonesUrban2019, @williamsRace2021
   ---
   # References
   ```
   The `nocite` field lists every matched citation key (from Phases 2–3). This tells pandoc to include them in the bibliography even though they're not cited inline.

2. **Run pandoc** to generate the formatted bibliography:
   ```bash
   pandoc dummy-refs.md --citeproc -o bibliography.md -t markdown
   ```
   Adjust the CSL file path as needed. Common styles:
   - ASA: `--csl american-sociological-association.csl`
   - APA 7th: `--csl apa.csl`
   - Chicago: `--csl chicago-author-date.csl`

3. **Clean up**: Remove the dummy file. Review `bibliography.md` for any citeproc warnings (missing fields, unresolved keys).

4. **Append unmatched citations** (from Phase 3) as a separate section at the end of `bibliography.md`:
   ```markdown
   ## Unmatched Citations (require manual lookup)
   - Smith (2020) — Not found in references.bib
   ```

**Output**: `bibliography.md` with pandoc/citeproc-formatted references.

**Why pandoc?** Pandoc's citeproc engine handles the full complexity of citation formatting — name particles, edited volumes, translations, sorting, punctuation — far more reliably than manual formatting. It uses the same CSL styles as Zotero, Mendeley, and other reference managers.

---

## Citation Pattern Reference

### Pandoc Format (Primary — from our writing skills)

| Pattern | Example | Regex |
|---------|---------|-------|
| Parenthetical | `[@smithHousing2020]` | `\[@([a-zA-Z0-9]+)\]` |
| Multiple | `[@smith2020; @jones2019]` | `\[@([a-zA-Z0-9]+(?:;\s*@[a-zA-Z0-9]+)*)\]` |
| With page | `[@smith2020, p. 45]` | `\[@([a-zA-Z0-9]+),\s*p\.\s*\d+\]` |
| Narrative | `@smithHousing2020 argues` | `(?<!\[)@([a-zA-Z0-9]+)(?!\])` |
| Suppress author | `[-@smith2020]` | `\[-@([a-zA-Z0-9]+)\]` |
| String modifiers | `[see @key1; cf. @key2]` | `\[(?:see\|e\.g\.,\|cf\.)\s*@` |

### Legacy Format (Fallback — for manuscripts not written with our skills)

| Pattern | Example | Regex |
|---------|---------|-------|
| Single author | `(Smith 2020)` | `\(([A-Z][a-z]+)\s+(\d{4})\)` |
| Two authors | `(Smith and Jones 2020)` | `\(([A-Z][a-z]+)\s+(?:and|&)\s+([A-Z][a-z]+)\s+(\d{4})\)` |
| Et al. | `(Smith et al. 2020)` | `\(([A-Z][a-z]+)\s+et\s+al\.?\s+(\d{4})\)` |
| Multiple citations | `(Smith 2020; Jones 2019)` | Split on `;\s*` then parse each |
| With page | `(Smith 2020, p. 45)` | `\(([A-Z][a-z]+)\s+(\d{4}),?\s*p?p?\.?\s*\d+\)` |
| Narrative | `Smith (2020)` | `([A-Z][a-z]+)\s+\((\d{4})\)` |

### Edge Cases (Legacy Format)

- **Hyphenated names**: `(García-López 2020)` - include hyphen in author pattern
- **Particles**: `(van der Berg 2020)` - lowercase particles before surname
- **Organizations**: `(WHO 2020)` - all-caps or mixed case organizations
- **No date**: `(Smith n.d.)` - handle "n.d." as year placeholder
- **Forthcoming**: `(Smith forthcoming)` - handle non-numeric years

## Output Formats

Formatting is handled entirely by pandoc's citeproc engine using CSL style files. You do **not** need to manually format entries. Simply specify the correct CSL file for the target style:

| Style | CSL file | Notes |
|-------|----------|-------|
| ASA | `american-sociological-association.csl` | Default for sociology journals |
| APA 7th | `apa.csl` | Psychology and interdisciplinary |
| Chicago Author-Date | `chicago-author-date.csl` | History, some social sciences |

Download CSL files from https://github.com/citation-style-language/styles if not already present in the project.

## File Structure

```
project/
├── manuscript.md           # Input: document with citations
├── bibliography/
│   └── bibliography.md     # Final output (Phase 4)
```

Phases 1–3 produce conversation output only. No intermediate files are saved.

## Key Reminders

- **`references.bib` must be present** and readable in the project directory
- **Author names vary**: Match flexibly against the BibTeX `author` field (last name + year first, then refine)
- **Multiple matches are possible**: Same author may have multiple works per year in the `.bib` file
- **Missing items**: User may need to add entries to `references.bib` before proceeding
- **Format matters**: Confirm desired style before generating bibliography

## Starting the Process

When the user is ready to begin:

1. **Ask for the manuscript**:
   > "Please share the path to your manuscript file (markdown, .docx, or .txt)."

2. **Confirm citation style**:
   > "I'll extract Author-Year citations. What bibliography format do you need? (APA, ASA, Chicago, other)"

3. **Locate `references.bib`**:
   > "Let me verify the `references.bib` file is present. Is it in the project root or a `references/` subdirectory?"

4. **Proceed with Phase 0** to read the document and inventory citations.
