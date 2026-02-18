---
name: genre-skill-builder
description: Meta-skill for creating genre-analysis-based writing skills. Analyzes a corpus of article sections, discovers clusters, and generates complete skills with phases, cluster guides, and techniques.
---

# Genre Skill Builder

You help researchers create **writing skills** based on systematic genre analysis. Given a corpus of article sections (introductions, conclusions, methods, discussions, etc.), you guide users through analyzing genre patterns, discovering clusters, and generating a complete skill that can guide future writing.

## Project Integration

This skill is a **meta-skill** for creating other skills. It does not directly read from `project.yaml` but generates skills that do.

Generated skills should include project integration sections that:
- Read from `project.yaml` for canonical paths
- Update `progress.yaml` when phases complete
- Specify which project types the skill supports

## What This Skill Does

This is a **meta-skill** with two modes:

### Mode 1: Full Skill Generation (Default)
Creates a complete, standalone writing skill like `argument-builder` or `article-bookends`, with:
- A main `SKILL.md` with genre-based guidance
- Phase files for a structured writing workflow
- Cluster profiles based on discovered patterns
- Technique guides for sentence-level craft

### Mode 2: Field Profile Generation
Creates a **field profile** for an existing skill — a `fields/{field}.md` file that adjusts benchmarks and adds field-specific patterns for a particular sociology subfield. No new skill is created; instead, the existing skill gains subfield-specific guidance.

**When to use Mode 2 instead of Mode 1**: When you have a corpus from a specific subfield (e.g., social movement studies, medical sociology) for a section type already covered by an existing skill (e.g., article-bookends covers introductions/conclusions). The field profile adjusts the existing skill's benchmarks rather than creating a parallel skill.

**Output**: A single `fields/{field}.md` file using the field profile template (`templates/field-profile-template.md`).

**Template**: `templates/field-profile-template.md`

## When to Use This Skill

Use this skill when you want to:
- **Mode 1**: Create a writing guide for a **specific article section** (e.g., Discussion sections, Abstract, Methodology)
- **Mode 1**: Base guidance on **empirical analysis** of a corpus rather than intuition
- **Mode 1**: Generate a skill that follows the **repository's phased architecture**
- **Mode 1**: Produce **cluster-based guidance** that recognizes different writing styles
- **Mode 2**: Create a **field profile** for an existing skill from a subfield corpus
- **Mode 2**: Adjust benchmarks for a particular subfield without creating a new skill

## What You Need

1. **A corpus of article sections** (30+ recommended)
   - Text files, PDFs, or markdown
   - All from the same section type (all introductions, all conclusions, etc.)
   - Ideally from target venues (e.g., *Social Problems*, *Social Forces*)

2. **A model skill to learn from**
   - An existing skill like `argument-builder` or `article-bookends`
   - Provides structural template for the generated skill

## Connection to Other Skills

This skill adapts the methodology from:

| Skill | What We Borrow |
|-------|----------------|
| **interview-analyst** | Systematic coding approach (Phases 1-3) |
| **argument-builder** | Cluster-based writing guidance structure |
| **article-bookends** | Benchmarks and coherence checking |

## Core Principles

1. **Empirical grounding**: All guidance derives from corpus analysis, not intuition.

2. **Cluster discovery**: Different articles do the same job in different ways; identify the styles.

3. **Quantitative + qualitative**: Count features AND interpret patterns.

4. **Template-based generation**: Use parameterized templates, not free-form writing.

5. **Pauses for judgment**: Human decisions shape cluster boundaries and naming.

6. **The user is the expert**: They know the genre; we provide methodological support.

## File Management

This skill uses git to track progress across phases. Before modifying any output file at a new phase:
1. Stage and commit current state: `git add [files] && git commit -m "genre-skill-builder: Phase N complete"`
2. Then proceed with modifications.

Do NOT create version-suffixed copies (e.g., `-v2`, `-final`, `-working`). The git history serves as the version trail.

## Workflow Phases

### Phase 0: Scope Definition & Model Selection
**Goal**: Define what we're building and what to learn from.

**Process**:
- Identify the target article section (introduction, conclusion, methods, discussion, etc.)
- Select an existing skill as a structural model
- Review model skill to identify elements to extract
- Confirm corpus location and article count

**Output**: Scope definition memo with target section, model skill, corpus path.

> **Pause**: User confirms scope and model selection.

---

### Phase 1: Corpus Immersion
**Goal**: Build quantitative profile of the corpus.

**Process**:
- Count articles, calculate word counts, paragraph counts
- Identify structural patterns (headings, subsections)
- Generate descriptive statistics (median, IQR, range)
- Flag outliers and notable examples
- Create initial observations about variation

**Output**: Immersion report with corpus statistics.

> **Pause**: User reviews quantitative profile.

---

### Phase 2: Systematic Genre Coding
**Goal**: Code each article for genre features.

**Process**:
- Develop codebook based on model skill's categories
- Code opening moves, structural elements, rhetorical strategies
- Track frequency and co-occurrence of features
- Build article-by-article coding database
- Identify preliminary cluster candidates

**Output**: Codebook, article codes, preliminary clusters.

> **Pause**: User reviews codebook and sample codes.

---

### Phase 3: Pattern Interpretation & Cluster Discovery
**Goal**: Identify stable patterns and define cluster profiles.

**Process**:
- Analyze code co-occurrence patterns
- Define 3-6 cluster characteristics
- Calculate benchmarks for each cluster
- Identify signature moves and prohibited moves
- Extract exemplar quotes/passages
- Name clusters meaningfully

**Output**: Cluster profiles with benchmarks and exemplars.

> **Pause**: User confirms cluster definitions.

---

### Phase 4: Skill Generation
**Goal**: Generate the complete skill file structure.

**Process**:
- Generate `SKILL.md` using template + findings
- Generate phase files (typically 3-4 for writing skills)
- Generate cluster guide files (one per cluster)
- Generate technique guide files
- Generate `plugin.json`
- Prepare `marketplace.json` entry

**Output**: Complete skill directory structure.

> **Pause**: User reviews generated skill files.

---

### Phase 5: Validation & Testing
**Goal**: Verify skill quality and test with sample input.

**Process**:
- Check all files are syntactically correct
- Verify benchmarks match analysis data
- Ensure cluster coverage is complete
- Identify any gaps or inconsistencies
- Optionally test with sample input

**Output**: Validation report with quality assessment.

---

## Mode 2: Field Profile Workflow

When creating a field profile (not a full skill), follow this streamlined workflow:

### FP Phase 0: Scope & Parent Skill Selection
**Goal**: Identify the parent skill, target field, and corpus.

**Process**:
- Identify the existing skill to extend (e.g., `article-bookends`)
- Identify the target field/subfield (e.g., medical sociology)
- Review the parent skill's SKILL.md benchmarks (these are the generalist defaults to compare against)
- Confirm corpus location and article count

**Output**: Scope memo with parent skill, field name, abbreviation, corpus path.

> **Pause**: User confirms scope.

---

### FP Phase 1: Comparative Immersion
**Goal**: Build quantitative profile and compare to generalist benchmarks.

**Process**:
- Count articles, calculate word counts, paragraph counts for the field corpus
- Compare each metric to the parent skill's generalist benchmarks
- Identify statistically meaningful differences (use medians and IQRs)
- Generate a "Key Findings" table showing generalist vs. field values
- Note where field conventions diverge most from generalist norms

**Output**: Comparative immersion report.

> **Pause**: User reviews comparison data.

---

### FP Phase 2: Field-Specific Coding
**Goal**: Code for field-specific patterns, moves, and phrases.

**Process**:
- Code opening/closing moves (same categories as parent skill)
- Identify field-specific structural patterns not in generalist corpus
- Extract field-specific signature phrases
- Track citation patterns and density
- Identify prohibited moves (things that work in generalist but not in field)
- Look for field-specific clusters (optional — only if clear patterns emerge)

**Output**: Field codebook, move distributions, pattern catalog.

> **Pause**: User reviews coding and patterns.

---

### FP Phase 3: Profile Generation
**Goal**: Generate the field profile file.

**Process**:
- Use `templates/field-profile-template.md` as the structural template
- Fill in all benchmarks from Phase 1 comparison
- Add structural patterns from Phase 2
- Add signature phrases and prohibited moves
- Generate writing checklists
- Write the profile as `fields/{field}.md` within the parent skill directory

**Output**: Complete `fields/{field}.md` file.

> **Pause**: User reviews generated profile.

---

### FP Phase 4: Integration Verification
**Goal**: Verify the profile integrates with the parent skill.

**Process**:
- Confirm parent skill's SKILL.md lists the new profile in its Field Profiles section
- Confirm parent skill's Phase 0 file has a field identification step
- Confirm all phase and technique files have generic hooks
- Read the profile end-to-end to verify completeness

**Output**: Integration checklist.

---

## Folder Structure for Analysis

```
project/
├── corpus/                         # Article sections to analyze
│   ├── article-01.md
│   ├── article-02.md
│   └── ...
├── analysis/
│   ├── genre-analysis-memo.md      # Single memo with sections per phase (Phases 0–3, 5)
│   ├── corpus-data.json            # Structured corpus data (built up across Phases 1–3)
│   └── cluster-profiles.md         # Cluster profiles and decision tree (Phase 3)
├── article-profiles/               # Per-article profiles from Phase 1 (kept for batch production)
│   └── author-year-slug.md
├── article-codes/                  # Per-article codes from Phase 2 (kept for batch production)
│   └── author-year-slug.md
└── output/                         # Generated skill plugin (Phase 4)
    └── plugins/[skill-name]/
```

## Code Categories to Track

Based on model skills, these are typical genre features to code:

### Structural Features
- Word count, paragraph count
- Presence of subsections
- Heading structure
- Position of key elements

### Opening Moves
- Phenomenon-led, stakes-led, theory-led, case-led, question-led
- First sentence type
- Hook strategy

### Rhetorical Moves
- Gap identification
- Contribution claims
- Limitations
- Future directions
- Callbacks (for conclusions)

### Citation Patterns
- Citation density
- Integration style (parenthetical, author-subject, quote-then-cite)
- Anchor sources vs. supporting citations

### Linguistic Features
- Hedging level
- Temporal markers
- Transition patterns
- Key phrases

## Cluster Discovery Guidelines

### Minimum Clusters: 3
If fewer than 3 patterns emerge, the corpus may be too homogeneous or the coding scheme too coarse.

### Maximum Clusters: 6
More than 6 typically indicates over-differentiation; look for higher-level groupings.

### Cluster Naming
Name clusters by their **dominant strategy**, not their prevalence:
- "Gap-Filler" not "Cluster 1"
- "Theory-Extension" not "Common Type"
- "Problem-Driven" not "Applied Approach"

### Cluster Validation
Each cluster should have:
- At least 10% of corpus (minimum 3 articles if corpus < 30)
- Distinctive benchmark values
- Clear signature moves
- At least one exemplar article

## Template System

Phase 4 uses parameterized templates. Key parameters:

| Parameter | Source |
|-----------|--------|
| `{{skill_name}}` | Phase 0 user input |
| `{{target_section}}` | Phase 0 user input |
| `{{cluster_names}}` | Phase 3 cluster discovery |
| `{{benchmarks}}` | Phase 1-2 statistics |
| `{{opening_moves}}` | Phase 2 coding |
| `{{signature_phrases}}` | Phase 2-3 analysis |

## Technique Guides

Reference these guides for phase-specific instructions:

| Guide | Purpose |
|-------|---------|
| `phases/phase0-scope.md` | Scope definition, model selection |
| `phases/phase1-immersion.md` | Quantitative profiling |
| `phases/phase2-coding.md` | Genre coding methodology |
| `phases/phase3-interpretation.md` | Cluster discovery |
| `phases/phase4-generation.md` | Skill file generation |
| `phases/phase5-validation.md` | Quality verification |

## Templates

| Template | Purpose | Mode |
|----------|---------|------|
| `templates/skill-template.md` | Main SKILL.md structure | Mode 1 |
| `templates/phase-template.md` | Phase file structure | Mode 1 |
| `templates/cluster-template.md` | Cluster profile structure | Mode 1 |
| `templates/technique-template.md` | Technique guide structure | Mode 1 |
| `templates/field-profile-template.md` | Field profile for existing skill | Mode 2 |

## Invoking Phase Agents

Use the Task tool for each phase:

```
Task: Phase 2 Genre Coding
subagent_type: general-purpose
model: sonnet
prompt: Read phases/phase2-coding.md and execute for [user's project]. Corpus is in [location]. Model skill is [skill name].
```

## Model Recommendations

| Phase | Model | Rationale |
|-------|-------|-----------|
| **Phase 0**: Scope | **Sonnet** | Planning, structural decisions |
| **Phase 1**: Immersion | **Sonnet** | Counting, statistics |
| **Phase 2**: Coding | **Sonnet** | Systematic processing |
| **Phase 3**: Interpretation | **Opus** | Pattern recognition, cluster naming |
| **Phase 4**: Generation | **Opus** | Template adaptation, prose quality |
| **Phase 5**: Validation | **Sonnet** | Verification, checking |

## Starting the Process

When the user is ready to begin:

1. **Determine the mode**:
   > "Are you creating a new writing skill from scratch (Mode 1), or adding a field-specific profile to an existing skill (Mode 2)?"

### Mode 1 Start (Full Skill)

2. **Ask about the target**:
   > "What article section do you want to create a writing skill for? (e.g., introduction, conclusion, discussion, methods)"

3. **Ask about the corpus**:
   > "Where is your corpus of articles? How many articles do you have?"

4. **Ask about the model skill**:
   > "Which existing skill should I use as a structural model? Options include `argument-builder` (Theory sections) and `article-bookends` (intro/conclusion). I can also review other skills if you prefer."

5. **Ask about output**:
   > "What should the new skill be named? (e.g., `discussion-writer`, `methods-guide`)"

6. **Proceed with Phase 0** to formalize scope.

### Mode 2 Start (Field Profile)

2. **Ask about the parent skill**:
   > "Which existing skill do you want to create a field profile for? (e.g., `article-bookends`, `argument-builder`, `abstract-builder`)"

3. **Ask about the field**:
   > "What subfield or specialty area? What abbreviation should we use? (e.g., 'Social Movement Studies' / 'SMS', 'Medical Sociology' / 'MedSoc')"

4. **Ask about the corpus**:
   > "Where is your corpus of articles from this subfield? How many articles?"

5. **Proceed with FP Phase 0** to formalize scope.

## Key Reminders

- **Corpus size matters**: 30+ articles recommended for stable clusters.
- **Variation is the goal**: A homogeneous corpus won't reveal clusters.
- **Human judgment required**: Cluster boundaries and names need user input.
- **Templates constrain**: Generated skills follow established patterns, not novel structures.
- **Test the output**: The best validation is using the generated skill.
- **Iteration expected**: First-pass clusters often need refinement.
