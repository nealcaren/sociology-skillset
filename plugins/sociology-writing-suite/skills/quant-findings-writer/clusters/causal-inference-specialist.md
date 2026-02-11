# Causal Inference Specialist

~12/83 articles. Heavily overrepresented in administrative-data (9/12). Defined by quasi-experimental identification strategy.

## Defining Feature

The section foregrounds causal identification: the argument is not just about *whether* X affects Y, but about *why we should believe* the estimate is causal. Heavy emphasis on identification assumptions, falsification tests, and multiple robustness checks. Robustness is not an afterthought — it typically consumes 30-40% of the section.

## Canonical Arc

```
SETUP → BASELINE → ELABORATE (main causal estimate) → ROBUSTNESS (extensive) → MECHANISM
```

## Paragraph Budget

| Move | Paragraphs | Share |
|------|-----------|-------|
| SETUP | 2-3 | 10% |
| BASELINE | 3-5 | 20% |
| ELABORATE | 2-3 | 15% |
| ROBUSTNESS | 5-8 | 35% |
| MECHANISM | 1-2 | 10% |

Total: 13-21 paragraphs typical.

## Opening Move

**Methodological setup**: Briefly restate the identification strategy before presenting results. This is more common here than in any other cluster.

Example pattern:
> To identify the causal effect of [treatment] on [outcome], I exploit [source of variation]. The key identifying assumption is that [assumption]. I first present OLS estimates, then turn to the [IV/DiD/RDD] specification.

## Closing Move

**Extensive robustness section**: End with a cascade of sensitivity analyses, placebo tests, and alternative specifications. Often references a supplemental appendix with additional tests.

## Signature Techniques

1. **Parallel trends testing**: Show pre-treatment coefficients are null — the foundational validity check for DiD designs. Always visualize with event study plots.

2. **Instrumental variable diagnostics**: Report first-stage F-statistics, overidentification tests, and reduced-form estimates alongside 2SLS.

3. **Placebo/falsification tests**: Apply the treatment to outcomes it should *not* affect, or to periods/groups it should *not* reach. Null results here strengthen the causal claim.

4. **Multiple robustness specifications**: Systematically vary bandwidths, functional forms, control sets, sample definitions, and clustering levels. Present in a dedicated table.

5. **Explicit discussion of identification threats**: Name specific threats to validity (selection, anticipation, spillovers, SUTVA violations) and explain how each is addressed.

## Theory Linking

Moderate. Less theory-to-finding linking than other clusters because the narrative energy goes toward identification credibility. Theory appears mainly in interpreting mechanism tests at the end.

## Table Strategy

Hybrid. Main estimates table plus a separate robustness table (or robustness appendix). Prose narrates the identification logic and interprets what each robustness check demonstrates.

## Common Pitfalls

- Presenting the causal estimate without first establishing the identification strategy's credibility
- Piling up robustness checks without organizing them (group by type: alternative samples, alternative measures, alternative methods, placebo tests)
- Neglecting to discuss the *substantive magnitude* of the causal effect — it's not enough to show it's significant and identified
- Claiming causality too broadly when identification is local (LATE, complier populations, specific bandwidth)
