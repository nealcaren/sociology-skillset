---
name: lit-synthesis
description: Deep reading and synthesis of literature corpus. Theoretical mapping, thematic clustering, and debate identification using local library of markdown-converted papers.
---

# Literature Synthesis

You help sociologists move from a corpus of papers to a deep understanding of a field. This is the analytical bridge between finding papers (lit-search) and writing about them (argument-builder).

## Project Integration

This skill reads from `project.yaml` when available:

```yaml
# From project.yaml
paths:
  lit_synthesis: literature/synthesis/
```

**Project type:** This skill works for **all project types**. Literature synthesis is essential for qualitative, quantitative, and mixed methods research.

Updates `progress.yaml` when complete:
```yaml
status:
  lit_synthesis: done
artifacts:
  field_synthesis: literature/synthesis/field-synthesis.md
```

## The Lit Trilogy

This skill is the middle step in a three-skill workflow:

| Skill | Role | Key Output |
|-------|------|------------|
| **lit-search** | Find papers via OpenAlex | `database.json`, `references.bib`, download checklist |
| **lit-synthesis** | Analyze & organize via local library | `field-synthesis.md` (with theoretical map, thematic clusters, debate map as sections) |
| **argument-builder** | Draft prose | Publication-ready Theory section |

**Input**: Papers as markdown files in `library/` (converted from PDFs) and `references.bib` (from lit-search or user's existing library)
**Output**: Organized understanding of the field ready for writing

## When to Use This Skill

Use this skill when users:
- Have a corpus of papers (from lit-search or their own collection)
- Need to understand the theoretical landscape before writing
- Want to identify debates, tensions, and competing positions
- Need to organize papers thematically or by theoretical tradition
- Want deep reading notes, not just metadata extraction

## Core Principles

1. **Read deeply, not widely**: Better to understand 15 papers thoroughly than 50 superficially.

2. **Theoretical traditions matter**: Papers exist within intellectual lineages. Map who cites whom and why.

3. **Debates are gold**: Competing positions create space for contributions. Find the tensions.

4. **Organization serves writing**: The clusters and maps you create should directly feed argument-builder's architecture phase.

5. **Full text when possible**: Abstracts tell you *what*; full text tells you *how* and *why*.

## File Management

This skill uses git to track progress across phases. Before modifying any output file at a new phase:
1. Stage and commit current state: `git add [files] && git commit -m "lit-synthesis: Phase N complete"`
2. Then proceed with modifications.

Do NOT create version-suffixed copies (e.g., `-v2`, `-final`, `-working`). The git history serves as the version trail.

---

## Local Library Integration

This skill reads papers from a local library of markdown-converted PDFs alongside `references.bib` for bibliographic metadata.

### Expected Library Layout

```
project/
├── references.bib          # BibTeX from lit-search (or user's reference manager)
└── library/
    └── markdown/
        ├── smith2020-cultural-frames.md
        ├── jones2019-institutional.md
        └── ...             # One .md per paper, converted from PDF
```

### Converting PDFs to Markdown

Use the shared conversion script:

```bash
plugins/sociology-skillset/scripts/convert-to-md.sh /path/to/paper.pdf
```

This script handles PDF-to-markdown conversion with caching. Run it for each PDF before starting Phase 1. See the script for full usage and options.

### Using reading-agent Skill

For structured reading notes, use the bundled **reading-agent** skill:

```
/reading-agent

Paper: [Author Year - Title]
PDF: /path/to/paper.pdf
DOI: [doi]
```

The reading-agent skill handles PDF conversion and produces structured notes with:
- Bibliographic info and identifiers
- Core arguments and theoretical frameworks
- Methods and empirical strategy
- Key findings and contribution claims
- Key quotes with page numbers

### Batch Processing

For batch processing many papers:

1. **Convert PDFs**: Run `plugins/sociology-skillset/scripts/convert-to-md.sh` on each paper
2. **Use reading-agent in batch mode**:
   ```
   /reading-agent

   Batch process these papers:
   - /papers/smith2020.pdf (DOI: 10.1086/123456)
   - /papers/jones2019.pdf (OpenAlex: W2123456789)
   ```
3. **Collect outputs**: Notes saved to `reading-notes/` directory

---

## Workflow Phases

### Phase 0: Corpus Audit
**Goal**: Assess what's in the corpus and identify gaps.

**Process**:
- Review the database from lit-search (or user's reference library)
- Count papers by year, journal, author, theoretical tradition
- Identify potential gaps in coverage
- Prioritize which papers need deep reading vs. skimming

**Output**: Corpus audit results presented in conversation (statistics and reading priorities).

> **Pause**: User confirms corpus coverage and reading priorities.

---

### Phase 1: Deep Reading
**Goal**: Close read priority papers and extract analytical insights.

**Process**:
- For each priority paper, read full text from `library/markdown/`
- Extract: argument structure, theoretical framework, key concepts, methodological approach
- Note: how theory is deployed, what evidence supports claims, limitations acknowledged
- Create structured reading notes

**Output**: `reading-notes/` directory with per-paper notes.

> **Pause**: User reviews reading notes for key papers.

---

### Phase 2: Theoretical Mapping
**Goal**: Identify intellectual traditions and lineages.

**Process**:
- Identify which theoretical frameworks appear across papers
- Map citation relationships (who cites whom)
- Note foundational texts and their descendants
- Identify "camps" or schools of thought
- Document key concepts and how they're used

**Output**: `## Theoretical Map` section written into `field-synthesis.md`.

> **Pause**: User reviews theoretical landscape.

---

### Phase 3: Thematic Clustering
**Goal**: Organize papers by what they study and how.

**Process**:
- Group papers by empirical focus (population, setting, phenomenon)
- Group papers by theoretical approach
- Group papers by methodological strategy
- Identify papers that bridge multiple clusters
- Note within-cluster consensus and variation

**Output**: `## Thematic Clusters` section appended to `field-synthesis.md`.

> **Pause**: User reviews clustering logic.

---

### Phase 4: Debate Mapping
**Goal**: Identify tensions, disagreements, and competing positions.

**Process**:
- Find explicit disagreements (papers that critique each other)
- Find implicit tensions (contradictory findings or incompatible assumptions)
- Identify unresolved questions the field is grappling with
- Note where evidence is mixed or contested
- Document the "state of the debate" for each tension

**Output**: `## Debate Map` section appended to `field-synthesis.md`.

> **Pause**: User reviews debates and selects focus areas.

---

### Phase 5: Field Synthesis
**Goal**: Create comprehensive understanding ready for writing.

**Process**:
- Synthesize across phases into coherent field understanding
- Identify the most productive gaps for contribution
- Recommend which argument-builder cluster (Gap-Filler, Theory-Extender, etc.) fits
- Create the handoff document for argument-builder

**Output**: `field-synthesis.md` completed with integrated understanding and writing recommendations (builds on sections added in Phases 2–4).

---

## Output Files

```
lit-synthesis/
├── reading-notes/            # Phase 1: Per-paper notes (kept for batch production)
│   ├── smith2020-cultural-frames.md    # Filename: author-year-short-title
│   ├── jones2019-institutional.md
│   └── ...                             # Each file has identifier frontmatter
└── field-synthesis.md        # Comprehensive synthesis with sections for theoretical map, thematic clusters, debate map
```

**Note**: Filenames use `author-year-short-title.md` for human readability, but the **frontmatter identifiers** (`citation_key`, OpenAlex ID, DOI) are the authoritative way to match notes back to source papers. The `citation_key` is preferred because it enables `[@citationKey]` Pandoc citation syntax in downstream writing skills.

## Reading Note Template

For each paper in Phase 1, notes **must include identifier frontmatter** to enable reliable retrieval across the workflow:

```markdown
---
# Required: At least one unique identifier
citation_key: smithCulturalFrames2020  # Preferred: from lit-search database or references.bib
openalex_id: W2123456789    # From lit-search database
doi: 10.1086/123456         # Digital Object Identifier

# Recommended: Additional metadata for filtering
first_author: Smith
year: 2020
short_title: cultural-frames
---

# Smith 2020 - Cultural Frames

## Bibliographic Info
- Full citation: [from references.bib or database]
- DOI: [link]
- OpenAlex: https://openalex.org/W2123456789

## Core Argument
[1-2 sentences: What is the paper arguing?]

## Theoretical Framework
- Tradition: [e.g., Bourdieusian, institutionalist, interactionist]
- Key concepts used: [list]
- How theory is deployed: [description vs. extension vs. critique]

## Empirical Strategy
- Data: [what kind]
- Methods: [how analyzed]
- Sample: [who/what]

## Key Findings
1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

## Contribution Claim
[What does the paper claim to contribute?]

## Limitations (as noted by authors)
- [Limitation 1]
- [Limitation 2]

## My Notes
[Your analytical observations, connections to other papers, questions raised]

## Key Quotes
> "[Quote 1]" (p. X)

> "[Quote 2]" (p. Y)

## Tags
[theoretical-tradition] [empirical-focus] [method] [relevant-to-my-project]
```

## Model Recommendations

| Phase | Model | Rationale |
|-------|-------|-----------|
| **Phase 0**: Corpus Audit | **Sonnet** | Data processing, statistics |
| **Phase 1**: Deep Reading | **Sonnet** | Analytical reading of converted markdown |
| **Phase 2**: Theoretical Mapping | **Opus** | Pattern recognition, intellectual history |
| **Phase 3**: Thematic Clustering | **Sonnet** | Organization, categorization |
| **Phase 4**: Debate Mapping | **Opus** | Tension identification, nuance |
| **Phase 5**: Field Synthesis | **Opus** | Integration, strategic judgment |

## Starting the Synthesis

When the user is ready to begin:

1. **Identify the corpus**:
   > "Where are your papers? A folder of PDFs? A `references.bib` from lit-search? How many papers total?"

2. **Verify local library setup**:
   > "Do you have PDFs converted to markdown in `library/markdown/`? If not, we'll run `plugins/sociology-skillset/scripts/convert-to-md.sh` on each PDF before Phase 1."

3. **Set priorities**:
   > "Which papers are most central to your project? We'll deep-read those first and skim the rest."

4. **Clarify goals**:
   > "What are you trying to understand about this field? Are you looking for gaps, debates, or a specific theoretical tradition?"

5. **Proceed with Phase 0** to audit the corpus.

## Key Reminders

- **Identifiers are essential**: Every reading note must have at least one unique identifier (`citation_key`, OpenAlex ID, or DOI) in its frontmatter. Prefer `citation_key` when available.
- **Convert before reading**: Run `plugins/sociology-skillset/scripts/convert-to-md.sh` on all PDFs before Phase 1 begins
- **Quality over quantity**: Deep reading 15 papers beats skimming 50
- **Debates are opportunities**: Every tension you find is a potential contribution space
- **This feeds argument-builder**: The outputs here become inputs there—keep that handoff in mind
