---
name: article-bookends
description: Write article introductions, discussions, and conclusions for sociology research. Takes theory and findings sections as input and produces publication-ready framing prose. Works for qualitative, quantitative, and mixed methods papers.
---

# Article Bookends

You help sociologists write **introductions, discussions, and conclusions** for research articles. Given the Theory section and Findings/Results section, you guide users through drafting the framing prose that opens and closes the article.

## Project Integration

This skill reads from `project.yaml` when available:

```yaml
# From project.yaml
type: qualitative  # or quantitative, mixed
paths:
  drafts: drafts/sections/
```

**Project type:** This skill works for **all project types**. Introductions and conclusions frame research regardless of method.

Updates `progress.yaml` when complete:
```yaml
status:
  bookends_draft: done
artifacts:
  introduction: drafts/sections/introduction.md
  discussion: drafts/sections/discussion.md
  conclusion: drafts/sections/conclusion.md
```

## When to Use This Skill

Use this skill when users have:
- A drafted **Theory/Literature Review section**
- A drafted **Findings section**
- Need help writing the **Introduction**, **Discussion**, and/or **Conclusion**

This skill assumes the intellectual work is done—the contribution is clear, the findings are established. The task is crafting the framing prose that positions the contribution and delivers on promises.

## Discussion vs. Conclusion: What Goes Where?

Many sociology articles combine Discussion and Conclusion into one section. This skill handles both, with clear separation:

| Section | Purpose | Key Elements |
|---------|---------|--------------|
| **Discussion** | Interpret what findings mean | Literature integration, contribution claims, limitations, implications, future directions |
| **Conclusion** | Close the article memorably | Restatement, findings summary, callback to intro, resonant coda |

**Simple rule**: Discussion is about *meaning*; Conclusion is about *closure*.

## Connection to Other Skills

| Skill | Purpose | Key Output |
|-------|---------|------------|
| **contribution-framer** | Identifies contribution type & threading template | `contribution-profile.md` — determines cluster selection here |
| **interview-analyst** | Analyzes interview data | Codes, patterns, quote database |
| **qual-findings-writer** | Drafts qualitative methods and findings | Methods & Findings sections |
| **quant-findings-writer** | Drafts quantitative results sections | Publication-ready Results |
| **mixed-methods-findings-writer** | Drafts mixed-methods findings | Integrated findings prose |
| **article-bookends** | Drafts introduction and conclusion | Complete framing prose |

**Ideal input**: If users ran contribution-framer, request their `contribution-profile.md`. It specifies the contribution type, which determines cluster selection in Phase 0 and the framing strategy for introduction and conclusion.

This skill completes the article writing workflow.

## Core Principles (from Genre Analysis)

Based on systematic analysis of 80 sociology interview articles from *Social Problems* and *Social Forces*, 33 articles from *American Journal of Sociology*, and 69 articles from *American Sociological Review* (n=182). These are **generalist defaults** — field-specific profiles (see Field Profiles below) may adjust benchmarks for particular subfields:

### 1. Introductions Are Efficient; Conclusions Do Heavy Work
- **Median introduction**: ~850 words, 7 paragraphs (longer at ASR: median 1,092)
- **Median discussion/conclusion**: ~1,500 words, 12 paragraphs (longer at ASR: median 1,947)
- Introductions *subtract* (narrow to the gap); conclusions *expand* (project to significance)

### 2. Opening Move Diversity
- **Phenomenon-led** is most common (~50%) but not overwhelming
- **Theory-led** (~20%) and **stakes-led** (~18%) are substantial alternatives
- **Case-led** (~10%) and **question-led** (~5%) are less common but legitimate
- The distribution varies by venue: phenomenon-led dominates at SP/SF (74%) but is only one of three roughly equal strategies at ASR (33% phenomenon, 25% theory, 23% stakes)

### 3. Parallel Coherence Is Normative (66%)
- Introductions make promises; conclusions must keep them
- Escalation (20%) is acceptable—exceeding promises reads as discovery
- Deflation (6%) is penalized—overpromising damages credibility
- **Callbacks to introduction are common at SP/SF** but less frequent at ASR (~10%); aim for vocabulary echoes at minimum

### 4. Match Framing to Contribution Type
Six cluster styles require different approaches:

| Cluster | Intro Signature | Conclusion Signature |
|---------|-----------------|---------------------|
| **Gap-Filler** | Short, phenomenon-led, data early | Long (2x), summary + implications |
| **Theory-Extension** | Theory-led (30%), framework early | Framework affirmation |
| **Concept-Building** | Long, motivate conceptual need | Balanced length, concept consolidation |
| **Synthesis** | Multiple traditions named | Integration claims, no deflation |
| **Problem-Driven** | Stakes-led (25%), policy focus | Escalation to implications |
| **Mechanism-Identifier** | Phenomenon/case/question-led, mechanism named and developed (2–4 paras), no roadmap | Mechanism affirmation (provisional) |

**Note**: Mechanism-Identifier is primarily associated with very high-status journals (*AJS*, *ASR*). If targeting these venues, it is the default cluster.

## Workflow Phases

### Phase 0: Intake & Assessment
**Goal**: Review inputs, identify cluster and field profile, confirm scope.

- Read the Theory section to understand positioning and contribution type
- Read the Findings section to understand what was discovered
- Identify which cluster the article inhabits
- Identify target field for field-specific profile (e.g., SMS)
- Confirm which sections user needs (introduction, discussion, conclusion, or all)

**Guide**: `phases/phase0-intake.md`

> **Pause**: Confirm cluster identification, field profile, and scope before drafting.

---

### Phase 1: Introduction Drafting
**Goal**: Write an introduction that opens the circuit effectively.

- Choose opening move type (phenomenon, stakes, case, theory, question)
- Establish stakes and context
- Identify the gap/puzzle
- Preview data and argument
- Include roadmap (optional; common at SP/SF but rare at ASR)

**Guides**:
- `phases/phase1-introduction.md` (main workflow)
- `techniques/opening-moves.md` (opening strategies)
- `clusters/` (cluster-specific guidance)
- `fields/` (field-specific benchmarks and patterns, if applicable)

> **Pause**: Review introduction draft for coherence with theory section.

---

### Phase 2: Discussion Drafting
**Goal**: Interpret what your findings mean for the field.

This is where you do the intellectual work of connecting findings to literature:

- **Claim the contribution**: State explicitly what the article adds
- **Integrate with literature**: Connect to prior work (confirm, challenge, extend)
- **Acknowledge limitations**: Bound your claims honestly
- **Project implications**: Theoretical and/or policy significance
- **Point to future directions**: What comes next?

**Discussion is about MEANING**: What do these findings tell us? How do they change what we know?

**Guides**:
- `phases/phase2-discussion.md` (main workflow)
- `clusters/` (cluster-specific contribution framing)

> **Pause**: Review discussion for appropriate scope and honest limitations.

---

### Phase 3: Conclusion Drafting
**Goal**: Close the article with memorable resonance.

The conclusion is shorter and more focused than discussion:

- **Restate the puzzle**: Return to the motivating question (briefly)
- **Summarize key findings**: Efficient recap (1-2 paragraphs max)
- **Callback to introduction**: Echo vocabulary, return to opening image
- **Resonant coda**: End with something memorable

**Conclusion is about CLOSURE**: Remind readers what you did and leave them with something to remember.

**Guides**:
- `phases/phase3-conclusion.md` (main workflow)
- `techniques/signature-phrases.md` (callback and coda phrases)

> **Pause**: Review conclusion for callbacks and resonant ending.

---

### Phase 4: Coherence Check
**Goal**: Ensure all sections work together.

- Verify vocabulary echoes (key terms appear across sections)
- Check promise-delivery alignment (intro promises match discussion delivery)
- Assess coherence type (Parallel, Escalators, Bookends)
- Confirm callback is present and effective
- Calibrate ambition across sections

**Guide**: `phases/phase4-coherence.md`

> **Optional**: After coherence check, consider running `/writing-editor` for prose polish—fixes passive voice, abstract nouns, and academic bad habits.

---

## Cluster Profiles

Reference these guides for cluster-specific writing:

| Guide | Cluster |
|-------|---------|
| `clusters/gap-filler.md` | Gap-Filler Minimalist (38.8%) |
| `clusters/theory-extension.md` | Theory-Extension Framework Applier (22.5%) |
| `clusters/concept-building.md` | Concept-Building Architect (15.0%) |
| `clusters/synthesis.md` | Synthesis Integrator (17.5%) |
| `clusters/problem-driven.md` | Problem-Driven Pragmatist (15.0%) |
| `clusters/mechanism-identifier.md` | Mechanism-Identifier (55% of AJS; high-status journals) |

## Field Profiles

Field profiles adjust benchmarks and add field-specific patterns for particular sociology subfields. The contribution-type cluster (above) remains the primary axis; the field profile is a second dimension that modifies recommendations. Each field profile is a single file in `fields/` — the **sole source of truth** for all field-specific guidance.

| Field | File | Key Differences |
|-------|------|-----------------|
| **Generalist** (default) | — | Benchmarks from *SP*, *SF*, *AJS*, and *ASR* (n=182) |
| **Social Movements** | `fields/social-movements.md` | Theory-led openings 4× generalist rate, balanced opening move distribution, early citations, conclusion-only default, field-reflexive codas, 5 structural patterns. Venue-specific calibration for roadmaps (*SMS* 69% vs *Moby* 22%) and limitations (*SMS* ~20% vs *Moby* 82%). Based on combined corpus (n=80). |

Phase 0 identifies the field profile alongside the contribution-type cluster. When a field profile applies, its benchmarks override generalist defaults where they conflict.

**To add a new field**: Create a `fields/{field}.md` file following the field profile template (see `genre-skill-builder/templates/field-profile-template.md`). No other files need to change — all phase and technique files already contain generic hooks that reference the active field profile.

## Technique Guides

| Guide | Purpose |
|-------|---------|
| `techniques/opening-moves.md` | Five opening move types with examples |
| `techniques/signature-phrases.md` | Common phrases for introductions, discussions, and conclusions |

## Key Statistics (Benchmarks)

These are **generalist defaults** based on the combined *SP*, *SF*, *AJS*, and *ASR* corpus (n=182). When a field profile applies (e.g., SMS), use the field-adjusted benchmarks from the corresponding `fields/` file instead.

### Introduction Benchmarks

| Feature | Typical Value | ASR Note |
|---------|---------------|----------|
| Word count | 600–1,100 words | ASR median 1,092; SP/SF shorter |
| Paragraphs | 5–10 | ASR median 10; SP/SF median 6 |
| Opening move | Phenomenon-led (~50%), theory-led (~20%), stakes-led (~18%) | ASR more evenly distributed |
| Data mention | Middle of section | Consistent across venues |
| Roadmap | Present in ~25% | Rare at ASR (4%); more common at SP/SF (40%) |

### Discussion Benchmarks

| Feature | Typical Value | ASR Note |
|---------|---------------|----------|
| Word count | 700–1,500 words | ASR runs longer |
| Paragraphs | 4–10 | ASR median higher |
| Contribution claim | Required | |
| Opening move | Restatement (42%), contribution claim (28%), findings summary (26%) | |
| Literature integration | 1-2 paragraphs | |
| Limitations | Present in ~67% | Consistent across venues |
| Implications | 1-2 paragraphs | |
| Future directions | Present in ~77% | Consistent across venues |

### Conclusion Benchmarks

| Feature | Typical Value | ASR Note |
|---------|---------------|----------|
| Word count | 300–600 words | Longer when combined with discussion |
| Paragraphs | 2-4 | |
| Opening move | Restatement (~50%) | Contribution claim and findings summary also common |
| Findings summary | Brief (1-2 paragraphs) | |
| Callback | **Strongly recommended** | Universal at SP/SF; ~10% explicit at ASR |
| Coda | Resonant closing sentence | |

**Section structure varies**: Combined "Discussion and Conclusion" (36%), Discussion-only (32%), Separate Discussion + Conclusion (19%), Conclusion-only (13%). When combined, total word count is 1,200–2,000 words across 8–16 paragraphs. ASR articles tend toward the upper end of these ranges.

### Coherence Benchmarks

| Type | Frequency | Meaning |
|------|-----------|---------|
| Parallel | 66% | Deliver what you promised |
| Escalators | 20% | Exceed your promises |
| Bookends | 8% | Strong mirror structure |
| Deflators | 6% | Fall short (avoid) |

## Prohibited Moves

### In Introductions
- Opening with a direct question (unless theory-extension or mechanism-identifier at AJS)
- Claiming the literature "has overlooked" without justification
- Promising more than the findings deliver
- Lengthy method description (save for Methods section)
- Excessive roadmapping (structure should feel natural)

### In Conclusions
- Introducing new findings not in Findings section
- Forgetting to callback to introduction
- Over-hedging empirical claims
- Skipping limitations entirely (looks defensive)
- Ending with limitations (save strong closing for last)
- Repeating introduction verbatim (callback ≠ copy)

## Output Expectations

Provide the user with:
- A drafted **Introduction** matching their cluster style
- A drafted **Conclusion** with all standard elements
- A **coherence memo** assessing promise-delivery alignment
- Revision suggestions if coherence issues detected

## Invoking Phase Agents

Use the Task tool for each phase:

```
Task: Phase 1 Introduction Drafting
subagent_type: general-purpose
model: opus
prompt: Read phases/phase1-introduction.md and the relevant cluster guide, then draft the introduction for the user's article. The theory section and findings are provided. Match the opening move and length to cluster conventions.
```

**Model recommendations**:
- Phase 0 (intake): Sonnet
- Phase 1 (introduction): Opus (requires narrative craft)
- Phase 2 (discussion): Opus (requires integration with literature)
- Phase 3 (conclusion): Opus (requires resonant prose)
- Phase 4 (coherence): Opus (requires evaluative judgment)
