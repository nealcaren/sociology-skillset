# Quant-Anchored Elaborator

Second most common cluster (28/84 articles, 33%). Quantitative findings come first and establish core empirical claims; qualitative evidence follows to explain mechanisms, flesh out meanings, or reveal processes that the numbers cannot capture. Also includes the **model-progression variant** (2 articles) where heavy model-building with systematic specification changes is followed by minimal qualitative illustration.

## Defining Feature

A two-phase structure: the first half presents quantitative results (regressions, descriptive statistics, formal models), and the second half uses qualitative evidence to elaborate on those results. The quantitative findings are the scaffolding; the qualitative evidence is the interpretive architecture built upon it. A clear TRANSITION move marks the shift between phases.

## Canonical Arc

```
SETUP → BASELINE → ELABORATE → VISUAL → ROBUSTNESS →
TRANSITION → THEMATIC → ILLUSTRATE → MECHANISM
```

**Model-progression variant:**
```
DESCRIBE → BASELINE → ELABORATE → ELABORATE → ROBUSTNESS →
TRANSITION → ILLUSTRATE → SUMMARY
```

In the variant, the quantitative section dominates (70-80% of space), and qualitative evidence is limited to 2-4 illustrative quotations or brief case descriptions.

## Paragraph Budget

| Move | Paragraphs | Share | Method |
|------|-----------|-------|--------|
| SETUP | 1-2 | 5% | Quant |
| BASELINE | 3-4 | 15% | Quant |
| ELABORATE | 3-5 | 20% | Quant |
| VISUAL | 1-2 | 5% | Quant |
| ROBUSTNESS | 2-3 | 10% | Quant |
| TRANSITION | 1 | 5% | Bridge |
| THEMATIC | 3-5 | 20% | Qual |
| ILLUSTRATE | 2-3 | 10% | Qual |
| MECHANISM | 1-2 | 10% | Mixed |

Total: 17-27 paragraphs typical. Quantitative block: ~55% of paragraphs. Qualitative block: ~40%. Transition: ~5%.

## Opening Move

**Table reference** or **main finding first** (78% combined).

Table reference pattern:
> Table 2 presents OLS regression results predicting [outcome]. Model 1 includes [basic controls]; Model 2 adds [focal variable]. Across all specifications, [focal variable] is significantly associated with [outcome] (b = .34, p < .001).

Main finding first pattern:
> The central finding is clear: [variable] significantly predicts [outcome], and this relationship persists across alternative model specifications, samples, and measurement strategies. We detail this evidence below before turning to interview data that illuminate the mechanisms underlying this pattern.

## Closing Move

**Qualitative synthesis** or **mechanism test** (64% combined).

Qualitative synthesis pattern:
> The interviews thus reveal that the statistical association between [X] and [Y] operates through two primary pathways. Respondents in [condition A] described [process], while those in [condition B] emphasized [alternative process]. Both pathways are consistent with the quantitative evidence but could not have been identified from the regression results alone.

Mechanism test pattern:
> The qualitative evidence supports the proposed mechanism linking [X] to [Y] through [M]. Across 23 interviews, respondents consistently described a sequence in which [process step 1] led to [process step 2], ultimately producing [outcome]. This process-tracing evidence, combined with the significant indirect effect in the mediation model (Table 5), provides converging evidence for the [theoretical framework] account.

## Signature Techniques

1. **Model progression narrative**: Narrate what happens as models become more complex. "Model 1 includes only demographics. In Model 2, adding [variable] reduces the focal coefficient from .42 to .31, consistent with partial mediation."

2. **Transition paragraph**: A dedicated paragraph marking the shift from quantitative to qualitative evidence. This is the most important paragraph in the cluster. It must do three things: (a) summarize what the quant evidence established, (b) name what it *cannot* explain, and (c) state what the qual evidence will add. "Having established that [X predicts Y] using regression models, we now turn to our interview data to examine *how* this process unfolds in practice." The transition should make clear whether the qualitative phase will *elaborate* (deepen understanding of the same question) or *extend* (address a new question raised by the quantitative findings).

3. **Quant-qual juxtaposition**: After presenting a statistical finding, immediately follow with qualitative evidence. "The regression coefficient suggests a .34 SD increase, but what does this look like in lived experience? Respondents described..."

4. **Magnitude contextualization**: Translate coefficients into substantive terms. "A one-standard-deviation increase in [variable] corresponds to a [X]% change in [outcome] -- roughly the difference between [concrete comparison]."

5. **Process-tracing**: In the qualitative section, trace the causal chain that connects the quantitative variables. Map interview evidence onto the X -> M -> Y pathway identified in statistical models.

## Method Integration Pattern

**Elaboration** (primary). Quantitative evidence answers "what" and "how much"; qualitative evidence answers "how" and "why." The integration is sequential rather than simultaneous -- methods occupy distinct blocks -- but the qualitative section explicitly references and builds on the quantitative findings.

## Theory Linking Density

**Moderate.** Theory is invoked at the beginning (framing hypotheses), at the transition point (connecting quant findings to qualitative expectations), and in the closing mechanism discussion. Less continuously present than in the Thematic Integrator.

## Table/Figure Strategy

**Table-driven** in the quantitative section; **narrative-driven** in the qualitative section. The quantitative block typically references 2-4 tables (descriptive statistics, main models, robustness checks) and 1-2 figures. The qualitative block may reference a coding table but primarily relies on block quotations and narrative.

## Subsection Structure

Typically **by method** at the top level, with thematic sub-organization within the qualitative block:
- "Quantitative Results" (or "Regression Results" / "Statistical Findings")
  - Subsections by model or outcome variable
- "Qualitative Findings" (or "Interview Evidence" / "Mechanisms")
  - Subsections by theme or process stage

Some articles use a flat structure with the TRANSITION paragraph as the only structural marker.

## Common Pitfalls

- **Afterthought qualitative section**: The qualitative block feels tacked on rather than integral. Prevent this by having the qualitative evidence address specific questions raised by the quantitative results.
- **Missing the transition**: Jumping from robustness checks to interview quotes without a paragraph bridging the two. The transition paragraph is the most important paragraph in this cluster.
- **Redundant illustration**: Using qualitative evidence only to re-state what the numbers already showed ("Consistent with the regression results, interviewees reported...") rather than adding new dimensions. Apply the "more than sum of parts" test: if the qualitative evidence could be removed without losing any insight, the integration is too shallow.
- **Suppressing divergence**: When qualitative evidence complicates or contradicts a quantitative finding, report this transparently. Divergence is analytically productive -- it can reveal boundary conditions, countervailing processes, or measurement limitations.
- **Asymmetric rigor**: Applying strict evidentiary standards to quantitative claims (robustness, alternative specifications) but accepting qualitative claims from a single interview excerpt. Show breadth: cite multiple informants.
- **Coefficient overload in quant section**: Reporting every coefficient in every model. Focus on focal variables; relegate controls to table notes.
