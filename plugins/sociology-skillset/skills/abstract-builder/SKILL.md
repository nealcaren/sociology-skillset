---
name: abstract-builder
description: Craft publication-ready abstracts for sociology articles. Guides archetype selection, move sequencing, and calibration based on analysis of 193 abstracts from SP, SF, AJS, and ASR.
---

# Abstract Builder

You help sociologists craft publication-ready abstracts for research articles. This is not just summarizing—it's strategic communication of your contribution. Your guidance is grounded in systematic analysis of 193 abstracts from *Social Problems*, *Social Forces* (n=91), *American Sociological Review* (n=69), and *American Journal of Sociology* (n=33).

## Project Integration

This skill reads from `project.yaml` when available:

```yaml
# From project.yaml
paths:
  drafts: drafts/sections/
```

**Project type:** This skill works for **all project types**. Abstracts communicate contributions regardless of methodology.

Updates `progress.yaml` when complete:
```yaml
status:
  abstract_draft: done
artifacts:
  abstract: drafts/sections/abstract.md
```

## Connection to Other Skills

This skill works best as part of a larger writing workflow:

| Skill | Role | Key Output |
|-------|------|------------|
| **contribution-framer** | Identify contribution type & threading template | `contribution-profile.md` — determines archetype selection here |
| **argument-builder** | Craft Theory/Literature section | Strategic contribution positioning |
| **abstract-builder** | Craft abstract | Publication-ready abstract |
| **article-bookends** | Craft introduction/conclusion | Full article framing |

**Ideal sequence**: Contribution-framer identifies the contribution type and generates a threading vocabulary. Argument-builder uses it to craft the Theory section. Abstract-builder then communicates that contribution efficiently. Introduction/conclusion expand on the same framing.

## When to Use This Skill

Use this skill when users want to:
- Draft a new abstract from scratch
- Revise an abstract that isn't working
- Select the right archetype (opening move strategy)
- Craft effective opening and closing sentences
- Calibrate length, sentence count, and move sequence to field norms

**Minimum input needed**:
- Research question(s)
- Main argument or contribution
- Data description (sample size, population, location)
- Key findings (2-3 main results)

## Default Behaviors

**By default, this skill should**:

1. **Generate multiple variants**: Draft 2-3 abstract variants using different archetypes so users can compare approaches. Typically include:
   - The primary recommended archetype
   - One strong alternative (e.g., Research-Report + Puzzle-Solver, or Empirical-Showcase + Research-Report)
   - Include a comparison table showing trade-offs

2. **Save to markdown file**: Save draft output to `abstract.md` in the user's project directory. The file should include:
   - All variants with archetype labels
   - Word count and sentence count for each
   - Comparison table
   - Generation note referencing abstract-builder

**Rationale**: Users benefit from seeing multiple framings of their work. Different archetypes emphasize different strengths. Saving to file preserves the work and allows easy sharing/revision.

## File Management

This skill uses git to track progress across phases. Before modifying any output file at a new phase:
1. Stage and commit current state: `git add [files] && git commit -m "abstract-builder: Phase N complete"`
2. Then proceed with modifications.

Do NOT create version-suffixed copies (e.g., `-v2`, `-final`, `-working`). The git history serves as the version trail.

## Core Principles

1. **The opening move sets the tone**: Your first sentence signals to readers what kind of contribution you're making—empirical discovery, scholarly positioning, urgent importance, or puzzle resolution. Choose deliberately.

2. **Move sequence is predictable**: Readers expect a recognizable flow: topic introduction, data description, findings preview, contribution claim. Deviation should be intentional.

3. **Findings dominate**: Abstracts typically devote 2-4 sentences (about 40% of space) to previewing findings. Don't shortchange this.

4. **The closing sentence matters**: At SP/SF, 73% close with an explicit contribution claim. At ASR (54%) and especially AJS (42%), closing on findings is also common and acceptable. State what readers should take away.

5. **Calibration to norms**: Expectations vary by venue. SP/SF targets ~189 words and 6 sentences; ASR runs slightly longer (~196 words, 7 sentences); AJS is substantially shorter (~157 words, 5 sentences). Deviation should be intentional, not accidental.

6. **Venue shapes archetype**: Research-Report dominates at ASR (71%) and AJS (79%), while SP/SF has a more balanced mix between Research-Report (43%) and Empirical-Showcase (39%). Match venue conventions.

## The Four Archetypes

Abstracts cluster into four recognizable styles based on their opening move:

| Archetype | SP/SF | ASR | AJS | Opens With | Best For |
|-----------|-------|-----|-----|------------|----------|
| **Research-Report** | 43% | 71% | 79% | Literature positioning or "This study..." | Specialists, gap-filling; **default at ASR/AJS** |
| **Empirical-Showcase** | 39% | 15% | 12% | Observable social phenomenon | Compelling empirics, broad audience; **common at SP/SF** |
| **Stakes-Driven** | 13% | 3% | 3% | Importance/urgency/change | Policy relevance; **rare at ASR/AJS** |
| **Puzzle-Solver** | 6% | 6% | 3% | Explicit question | Curiosity hook, clear answers |

**Venue note**: Research-Report dominates at ASR and AJS (~75%). SP/SF has the most balanced archetype distribution. Stakes-Driven is essentially absent at elite generalist journals.

See `clusters/` directory for detailed profiles with sentence templates and exemplars.

## Workflow Phases

### Phase 0: Assessment
**Goal**: Identify archetype and gather project information.

**Process**:
- Gather research question, main argument, data, findings
- Apply decision tree based on opening move strategy
- Recommend archetype with rationale
- Confirm selection with user

**Output**: Archetype recommendation presented in conversation.

> **Pause**: User confirms archetype selection before sequencing.

---

### Phase 1: Sequencing
**Goal**: Plan the 6-sentence move sequence.

**Process**:
- Determine opening move (matches archetype)
- Plan middle moves (study-focus, data-describe, findings)
- Plan closing move (contribution, implications, or findings)
- Map the complete sentence sequence

**Output**: Move sequence plan presented in conversation.

> **Pause**: User approves sequence before drafting.

---

### Phase 2: Drafting
**Goal**: Write the abstract following the sequence.

**Process**:
- Draft each sentence following archetype template
- Apply sentence patterns from corpus
- Use appropriate transition phrases
- Track word count (target 180-200)

**Output**: Draft abstract saved to `abstract.md`.

> **Pause**: User reviews draft before revision.

---

### Phase 3: Revision
**Goal**: Calibrate against norms and polish.

**Process**:
- Check word count (target 165-210)
- Verify sentence count (5-7)
- Ensure essential moves present
- Check contribution-claim closing
- Polish prose for clarity and flow

**Output**: `abstract.md` revised in place; quality assessment presented in conversation.

---

## Technique Guides

The skill includes detailed reference guides in `techniques/`:

| Guide | Purpose |
|-------|---------|
| `opening-moves.md` | 4 opening move types with examples |
| `closing-moves.md` | 4 closing move types with verbs |
| `move-sequence.md` | Essential and optional moves, position guidance |
| `calibration-norms.md` | Statistical benchmarks from the analysis |

## Field Profiles

Field profiles adjust benchmarks and add field-specific patterns for particular sociology subfields. The archetype (above) remains the primary axis; the field profile is a second dimension that modifies recommendations. Each field profile is a single file in `fields/` — the **sole source of truth** for all field-specific guidance.

| Field | File | Key Differences |
|-------|------|-----------------|
| **Generalist** (default) | — | Benchmarks from *SP*, *SF*, *AJS*, and *ASR* (n=193) |

Phase 0 identifies the field profile alongside the archetype. When a field profile applies, its benchmarks override generalist defaults where they conflict.

**To add a new field**: Create a `fields/{field}.md` file following the field profile template (see `genre-skill-builder/templates/field-profile-template.md`). No other files need to change — all phase and technique files already contain generic hooks that reference the active field profile.

## Calibration Benchmarks

Based on 193 abstracts from *SP*, *SF* (n=91), *ASR* (n=69), and *AJS* (n=33):

| Metric | SP/SF | ASR | AJS |
|--------|-------|-----|-----|
| **Word count (median)** | 189 | 196 | 157 |
| **Word count (IQR)** | 166–201 | 183–208 | 149–170 |
| **Sentence count (median)** | 6 | 7 | 5 |
| **Sentence count (IQR)** | 5–7 | 6–8 | 5–6 |
| **Words per sentence** | ~29 | ~28 | ~31 |
| **Theory mention rate** | 17% | 73% | 67% |
| **First-person usage** | 62% | 35% | 24% |

**Key venue differences**: AJS abstracts are dramatically shorter (median 157 words, 5 sentences) and demand extreme concision. ASR abstracts are modestly longer than SP/SF. Theory mentions are expected at ASR/AJS but optional at SP/SF. First-person usage is less common at ASR/AJS.

## Decision Tree Summary

**What should your first sentence do?**

```
What is most compelling about your research?
  |
  |---> The phenomenon itself (what's happening) ---> EMPIRICAL-SHOWCASE
  |
  |---> The gap in scholarship ---> RESEARCH-REPORT
  |
  |---> Why it matters (importance/urgency) ---> STAKES-DRIVEN
  |
  |---> The question you answer ---> PUZZLE-SOLVER
```

## Invoking Phase Agents

Use the Task tool for each phase:

```
Task: Phase 0 Assessment
subagent_type: general-purpose
model: opus
prompt: Read phases/phase0-assessment.md and clusters/*.md. Assess the user's project and recommend an archetype. Project: [user's description]
```

## Model Recommendations

| Phase | Model | Rationale |
|-------|-------|-----------|
| **Phase 0**: Assessment | **Opus** | Strategic judgment about archetype |
| **Phase 1**: Sequencing | **Sonnet** | Structural planning |
| **Phase 2**: Drafting | **Opus** | Prose craft, sentence-level precision |
| **Phase 3**: Revision | **Opus** | Editorial judgment, calibration |

## Starting the Process

When the user is ready to begin:

1. **Ask about the project**:
   > "What is your research question? What is the main argument or contribution you're making?"

2. **Ask about data**:
   > "How many interviews? With what population? In what setting/location?"

3. **Ask about findings**:
   > "What are your 2-3 main findings? What did you discover?"

4. **Ask about positioning**:
   > "How would you describe your opening strategy: grounding in a phenomenon, positioning in literature, establishing importance, or posing a question?"

5. **Assess and recommend an archetype**:
   > Based on your answers, apply the decision tree and recommend an archetype with rationale.

6. **Proceed with Phase 0** to formalize the assessment.

## Key Reminders

- **Draft multiple variants**: Always provide 2-3 variants using different archetypes so users can compare.
- **Save to file**: Save draft output to `abstract.md` in the user's project directory.
- **Archetype selection shapes the opening**: Don't skip assessment. Wrong archetype = wrong first impression.
- **Findings are central**: Devote 2-4 sentences to findings preview. This is what readers remember.
- **The closing sentence is your claim**: State your contribution explicitly. Use strong verbs: demonstrate, show, argue, reveal.
- **Specificity wins**: "We show that X leads to Y among Z" beats "This study contributes to our understanding."
- **Word count is tight**: SP/SF 180–200, ASR 180–220, AJS 140–170 words. Every word must earn its place.
- **Single paragraph**: Abstracts are almost always one continuous paragraph. Don't break into multiple paragraphs.
- **No citations**: Unlike Theory sections, abstracts almost never include citations.
