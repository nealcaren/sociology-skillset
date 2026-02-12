---
name: quant-findings-writer
description: >
  Draft publication-ready Results/Findings sections for quantitative sociology articles.
  Guides cluster selection, arc construction, paragraph-level moves, and writing techniques
  based on genre analysis of 83 Social Problems/Social Forces articles across secondary-survey,
  administrative-data, and content-analysis methods. Use when the user wants to write,
  draft, or revise a Results section for a quantitative or content-analysis paper. Also
  use when the user asks for help structuring findings, organizing results, or translating
  statistical output into publication-ready prose.
---

# Quantitative Findings Writer

Draft Results/Findings sections for quantitative sociology articles using structural patterns discovered in 83 Social Problems and Social Forces articles.

## Project Integration

This skill reads from `project.yaml` when available:

```yaml
# From project.yaml
type: quantitative  # This skill is for quantitative projects
paths:
  drafts: drafts/sections/
  tables: output/tables/
  figures: output/figures/
```

**Project type:** This skill is designed for **quantitative** projects.

Consumes output from **r-analyst** or **stata-analyst** (tables, figures, interpretation memos from Phase 5).

Updates `progress.yaml` when complete:
```yaml
status:
  results_draft: done
artifacts:
  results_section: drafts/sections/results-section.md
```

## Connection to Other Skills

| Skill | Relationship | Details |
|-------|-------------|---------|
| **r-analyst** | Upstream | Produces tables, figures, interpretation memos (Phase 5 output) |
| **stata-analyst** | Upstream | Same as r-analyst but for Stata |
| **article-bookends** | Downstream | Takes results section as input for framing |
| **methods-writer** | Parallel | Methods section written alongside or before results |
| **lit-synthesis** | Upstream | Provides theoretical framework for theory-linking |

## Workflow

### Phase 1: Orient

Gather from the user:
1. **Method type**: secondary-survey-analysis, administrative-data, or content-analysis
2. **Key results**: tables, model output, or thematic findings to present
3. **Theoretical predictions**: hypotheses or expectations the results address
4. **Target length**: typical is 12-25 paragraphs (2,000-5,000 words)

If the user has already written a draft, read it and assess which cluster it most resembles before suggesting revisions.

### Phase 2: Select Cluster

Present the 7 clusters with their canonical arcs. Recommend 1-2 based on method type and analytic strategy:

| Cluster | Best for | Arc |
|---------|----------|-----|
| **Progressive Model Builder** | Regression-heavy papers building from simple to complex specs | DESCRIBE → BASELINE → ELABORATE → MECHANISM → ROBUSTNESS |
| **Hypothesis Tester** | Papers with numbered H1/H2/H3 predictions | SETUP → BASELINE → ELABORATE → SUBGROUP → SUMMARY |
| **Decomposition Analyst** | Gap/disparity papers using Oaxaca-Blinder, mediation | DESCRIBE → BASELINE → DECOMPOSE → MECHANISM → ROBUSTNESS |
| **Subgroup Comparator** | Heterogeneity-focused papers (by race, gender, class) | DESCRIBE → BASELINE → SUBGROUP → COMPARISON → ROBUSTNESS |
| **Temporal Tracker** | Event studies, trend analysis, periodization | TEMPORAL → BASELINE → TEMPORAL → SUBGROUP → ROBUSTNESS |
| **Thematic Explorer** | Content analysis with qualitative themes/frames | THEMATIC → THEMATIC → THEMATIC → SUMMARY |
| **Causal Inference Specialist** | DiD, IV, RDD, matching designs | SETUP → BASELINE → ELABORATE → ROBUSTNESS → MECHANISM |

**Selection heuristics:**
- Survey data + model progression → Progressive Model Builder
- Admin data + quasi-experimental design → Causal Inference Specialist
- Admin data + inequality decomposition → Decomposition Analyst
- Any method + explicit hypotheses → Hypothesis Tester
- Any method + group comparisons as central question → Subgroup Comparator
- Content analysis + thematic coding → Thematic Explorer
- Panel/longitudinal + change over time → Temporal Tracker

After the user selects a cluster, read the matching guide from `clusters/{cluster-name}.md` for detailed arc, paragraph budget, signature techniques, and exemplar patterns.

### Phase 3: Build the Arc

Using the cluster guide, construct a section outline:

1. Map each major finding/table to a MOVE from the standardized vocabulary
2. Sequence moves following the cluster's canonical arc
3. Allocate paragraphs using the cluster's paragraph budget
4. Identify the opening and closing moves

**Standardized move vocabulary:**

| Move | Function |
|------|----------|
| DESCRIBE | Descriptive statistics, sample overview, bivariate patterns |
| SETUP | Methodological restatement, analytic strategy recap |
| BASELINE | Initial/simple models, main effects without interactions |
| ELABORATE | Add complexity: interactions, nonlinearities, mediators |
| DECOMPOSE | Formal decomposition (Oaxaca-Blinder, mediation, etc.) |
| SUBGROUP | Heterogeneity by subgroups (race, gender, class) |
| MECHANISM | Mediation, mechanism tests, process tracing |
| ROBUSTNESS | Sensitivity analysis, alternative specs, placebo tests |
| THEMATIC | Substantive theme/topic analysis |
| TEMPORAL | Over-time patterns, periodization, event studies |
| COMPARISON | Cross-group or cross-context comparison |
| VISUAL | Key figure/visualization driving the narrative |
| SUMMARY | Brief recap paragraph |
| TRANSITION | Bridge to discussion section |

Present the arc to the user as a numbered outline with paragraph counts per move.

### Phase 4: Draft

Write each move following corpus norms. Consult `techniques/techniques.md` for the full technique catalog.

**Opening paragraph** (choose one based on cluster):
- *Table reference* (58% of corpus): "Table 2 presents results from..."
- *Sample description* (20%): "Before turning to multivariate models, I describe..."
- *Hypothesis restatement* (14%): "Recall that H1 predicted..."
- *Methodological setup* (5%): "To estimate the causal effect, I use..."

**Body paragraphs:**
- Lead with the finding, not the method
- Translate every key coefficient into substantive terms (85% of corpus does this)
- Use attenuation tracking when adding controls: "the coefficient falls from .34 to .21"
- Connect to theory at moderate density: ~1 theory reference per 3-4 paragraphs for most clusters
- Report null findings transparently (45% of corpus does this)

**Closing paragraph** (choose one):
- *Robustness cascade* (18%): "Results are robust to..."
- *Strongest finding* (18%): save the most important result for the end
- *Subgroup analysis* (17%): end with heterogeneity
- *Supplemental reference* (14%): "Additional specifications in Appendix Table A3..."
- *Summary* (11%): brief recap of all findings

**Cross-cutting norms:**
- Median section length: ~18 paragraphs, 3 tables/figures referenced
- 75% use hybrid table strategy: tables anchor the narrative but prose interprets
- 55% link results to theory heavily; 40% moderately; only 5% minimally
- Distinguish statistical from practical significance when warranted

### Phase 5: Calibrate

After drafting, check against cluster norms:
- Does the arc match the canonical sequence?
- Is the paragraph budget balanced?
- Are tables referenced with interpretive guidance, not just pointed at?
- Is theory linking at the right density for the cluster?
- Are robustness checks present if the cluster expects them?
- Are null findings acknowledged rather than buried?

Present the draft with a brief calibration note.

## Reference Files

- **Cluster guides** (read the one matching the selected cluster):
  - `clusters/progressive-model-builder.md`
  - `clusters/hypothesis-tester.md`
  - `clusters/decomposition-analyst.md`
  - `clusters/subgroup-comparator.md`
  - `clusters/temporal-tracker.md`
  - `clusters/thematic-explorer.md`
  - `clusters/causal-inference-specialist.md`
- `techniques/techniques.md` — 20 writing techniques with descriptions and frequency data
- `references/corpus-statistics.md` — summary statistics from the 83-article analysis corpus
