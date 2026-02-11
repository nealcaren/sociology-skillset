---
name: mixed-methods-findings-writer
description: >
  Draft publication-ready Results/Findings sections for mixed-methods sociology articles.
  Guides cluster selection, arc construction, method integration, and writing techniques
  based on genre analysis of 84 Social Forces/Social Problems articles (~2018-2024) that
  combine quantitative and qualitative evidence. Use when the user wants to write, draft,
  or revise a Results/Findings section for a mixed-methods paper. Also use when the user
  asks for help integrating qualitative and quantitative evidence, structuring findings
  across methods, or translating both statistical output and interview/fieldwork data into
  publication-ready prose.
---

# Mixed-Methods Findings Writer

Draft Results/Findings sections for mixed-methods sociology articles using structural patterns discovered in 84 Social Forces and Social Problems articles.

## Project Integration

This skill reads from `project.yaml` when available:

```yaml
# From project.yaml
type: mixed  # This skill is for mixed methods projects
paths:
  drafts: drafts/sections/
  tables: output/tables/
  figures: output/figures/
  quotes: analysis/outputs/
```

**Project type:** This skill is designed for **mixed methods** projects.

Consumes output from both qualitative analysis (**interview-analyst**) and quantitative analysis (**r-analyst** or **stata-analyst**).

Updates `progress.yaml` when complete:
```yaml
status:
  integration_draft: done
artifacts:
  findings_section: drafts/sections/findings-section.md
```

## Connection to Other Skills

| Skill | Relationship | Details |
|-------|-------------|---------|
| **interview-analyst** | Upstream (qual) | Produces quote database, participant profiles |
| **r-analyst** | Upstream (quant) | Produces tables, figures, interpretation memos |
| **stata-analyst** | Upstream (quant) | Same as r-analyst but for Stata |
| **article-bookends** | Downstream | Takes findings section as input for framing |
| **methods-writer** | Parallel | Methods section written alongside or before findings |
| **lit-synthesis** | Upstream | Provides theoretical framework for integration |

## Workflow

### Phase 1: Orient

Gather from the user:
1. **Quantitative component**: regression output, descriptive statistics, surveys, admin data
2. **Qualitative component**: interviews, field notes, archival documents, ethnographic observations
3. **Integration rationale**: Is this *elaboration* (vertical -- both methods address the same question at different depths) or *extension* (horizontal -- each method addresses a different question)? Or triangulation (independent validation)?
4. **Theoretical predictions**: hypotheses, expectations, or sensitizing concepts
5. **Target length**: typical is 15-30 paragraphs (3,000-7,000 words; median 4,895)

If the user has already written a draft, read it and assess which cluster it most resembles before suggesting revisions.

### Phase 2: Select Cluster

Present the 5 clusters. Recommend 1-2 based on integration goal and analytic strategy:

| Cluster | Share | Best for | Arc |
|---------|-------|----------|-----|
| **Thematic Integrator** | 42% | Concept-driven papers weaving both methods within themes | THEMATIC > ILLUSTRATE > BASELINE > ELABORATE > COMPARISON > MECHANISM |
| **Quant-Anchored Elaborator** | 33% | Papers where quant establishes claims, qual explains why | BASELINE > ELABORATE > ROBUSTNESS > TRANSITION > THEMATIC > ILLUSTRATE > MECHANISM |
| **Alternating Validator** | 10% | Papers using methods to cross-validate each other | BASELINE > ILLUSTRATE > VISUAL > THEMATIC > COMPARISON > BASELINE > ILLUSTRATE |
| **Sequential Study Design** | 7% | Multi-study papers (Study 1, Study 2, Study 3) | SETUP > BASELINE > ELABORATE > SUMMARY > TRANSITION > SETUP > BASELINE > MECHANISM |
| **Qual-Dominant Quantifier** | 6% | Qualitative analysis with sparse descriptive statistics | QUALITATIVE-VIGNETTE > THEMATIC > ILLUSTRATE > BASELINE > THEMATIC > COMPARISON |

**Selection heuristics:**
- Concept-driven analysis + both methods throughout --> Thematic Integrator
- Regression/models as core claims + interviews/fieldwork explaining mechanisms --> Quant-Anchored Elaborator
- Two data sources answering the same question --> Alternating Validator
- Distinct study phases (e.g., survey then interviews) --> Sequential Study Design
- Ethnography/interviews as primary + descriptive stats as context --> Qual-Dominant Quantifier
- Heavy model-building with minimal qualitative --> Quant-Anchored Elaborator (model-progression variant)

**Integration rationale and cluster fit:**
- *Elaboration* (vertical integration: same question, different depth) → Thematic Integrator or Quant-Anchored Elaborator. Qual deepens quant or vice versa. The two methods produce "more than the sum of parts" because together they address both magnitude and mechanism.
- *Extension* (horizontal integration: different questions, combined for a fuller picture) → Sequential Study Design or Alternating Validator. Each study answers its own question; cross-study transitions must explain how the questions connect.
- *Triangulation* (independent validation) → Alternating Validator. Both methods reach the same conclusion independently, strengthening credibility.
- Mixed rationales are common: a paper may use elaboration within themes and extension across them.

After selection, read the matching guide from `clusters/{cluster-name}.md`.

### Phase 3: Build the Arc

Using the cluster guide, construct a section outline:

1. Map each major finding to a MOVE from the vocabulary below
2. Sequence moves following the cluster's canonical arc
3. Allocate paragraphs using the cluster's paragraph budget
4. Plan method transitions -- where does the evidence type shift?
5. Identify the opening and closing moves

**Standardized move vocabulary (16 moves):**

| Move | Function |
|------|----------|
| DESCRIBE | Descriptive statistics, sample overview, bivariate patterns |
| SETUP | Methodological restatement, analytic strategy recap |
| BASELINE | Initial models, main quantitative effects |
| ELABORATE | Add complexity: interactions, controls, mediators |
| THEMATIC | Qualitative theme with interpretive analysis |
| ILLUSTRATE | Extended quotation or case example supporting a claim |
| MECHANISM | Process-tracing, mediation, causal pathway evidence |
| SUBGROUP | Heterogeneity analysis by subgroup |
| COMPARISON | Cross-group or cross-context comparison |
| ROBUSTNESS | Sensitivity analysis, alternative specifications |
| TEMPORAL | Over-time patterns, periodization |
| VISUAL | Figure or visualization driving narrative |
| SUMMARY | Brief recap paragraph |
| TRANSITION | Bridge between method blocks or to discussion |
| DECOMPOSE | Formal decomposition (Oaxaca-Blinder, mediation) |
| QUALITATIVE-VIGNETTE | Opening narrative scene-setting from fieldwork |

Present the arc as a numbered outline with paragraph counts and method labels per move.

### Phase 4: Draft

Write each move following corpus norms. Consult `techniques/techniques.md` for the full catalog.

**Opening paragraph** (choose one based on cluster):
- *Qualitative vignette* (16%): scene-setting narrative from fieldwork or interview
- *Hypothesis restatement* (29%): "Recall that we expected..."
- *Table reference* (22%): "Table 2 presents results from..."
- *Main finding first* (13%): lead with the most important result
- *Methodological setup* (7%): "To examine this, we draw on..."

**Method integration** (the core challenge):
- **Elaboration** (47%): qual evidence explains or deepens quant findings -- *vertical* integration where both methods address the same question at different depths
- **Complementarity** (25%): each method addresses different facets of the question -- may be *vertical* (same question, different aspects) or *horizontal* (different questions combined)
- **Illustration** (13%): qual examples make quant patterns concrete -- weakest form; aim for elaboration instead
- **Sequential** (13%): one method's findings inform the next method's analysis -- *horizontal* integration where later methods address questions raised by earlier ones

The "more than sum of parts" test: at each integration point, ask whether the combined evidence yields an insight that neither method alone could produce. If qual merely restates what quant already showed, the integration is illustrative, not elaborative.

**Body paragraphs -- cross-cutting norms:**
- Qualitative evidence occupies 60-75% of paragraph space even when quant establishes core claims
- Extended quotations (50+ words) function as analytical anchors, not mere illustration (61%)
- Transition sentences between methods appear in only 17% of articles -- add them deliberately
- Connect to theory at heavy (53%) or moderate (45%) density
- Use subgroup analysis as a bridge device between methods (38%)

**Closing paragraph** (choose one):
- *Qualitative synthesis* (21%): return to qualitative evidence to frame the takeaway
- *Integration summary* (20%): weave both methods into a unified conclusion
- *Transition to discussion* (16%): bridge paragraph
- *Summary paragraph* (10%): recap all findings
- *Mechanism test* (9%): close with process evidence

### Phase 5: Calibrate

After drafting, check against cluster norms:
- Does the arc match the canonical sequence for the selected cluster?
- Is the paragraph budget balanced across moves?
- Are method transitions smooth -- or do quant and qual blocks feel disconnected?
- Is qualitative evidence doing analytical work, not just illustrating?
- Are extended quotations introduced and interpreted, not left to speak for themselves?
- Is theory linking at the right density (heavy for Thematic Integrator/Qual-Dominant; moderate for others)?
- For quant claims: are coefficients translated into substantive terms?
- For qual claims: is there enough evidence breadth (multiple informants/cases)?
- **"More than sum of parts" test**: at each integration point, does the combined evidence produce an insight that neither method alone could yield? If qual only restates what quant showed, revise toward elaboration.
- **Disconfirming evidence**: when quant and qual findings diverge, is the divergence reported transparently and interpreted analytically? Suppressing divergence undermines mixed-methods credibility. Treat divergence as an analytic opportunity (e.g., "The regression shows X, but interviews reveal a countervailing process...").
- **Computational methods note**: if the paper uses NLP, topic models, or automated text analysis alongside interviews or fieldwork, this counts as mixed-methods. Apply the same integration norms: the computational results need qualitative interpretation, not just validation.

Present the draft with a brief calibration note.

## Reference Files

- **Cluster guides** (read the one matching the selected cluster):
  - `clusters/thematic-integrator.md`
  - `clusters/quant-anchored-elaborator.md`
  - `clusters/alternating-validator.md`
  - `clusters/sequential-study-design.md`
  - `clusters/qual-dominant-quantifier.md`
- `techniques/techniques.md` -- 19 writing techniques with descriptions and frequency data
- `references/corpus-statistics.md` -- summary statistics from the 84-article analysis corpus
