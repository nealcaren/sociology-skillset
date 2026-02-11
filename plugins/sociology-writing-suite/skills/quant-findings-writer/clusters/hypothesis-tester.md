# Hypothesis Tester

~12/83 articles. Appears across method types but overrepresented in secondary-survey-analysis. Defines structure through explicit numbered predictions.

## Defining Feature

The section is organized around testing pre-stated hypotheses (H1, H2, H3...). Each hypothesis gets its own subsection or paragraph block. Results are framed as "supported," "partially supported," or "not supported."

## Canonical Arc

```
SETUP → BASELINE → ELABORATE (interactions) → SUBGROUP → SUMMARY
```

## Paragraph Budget

| Move | Paragraphs | Share |
|------|-----------|-------|
| SETUP | 1-2 | 10% |
| BASELINE (H1, H2) | 4-6 | 35% |
| ELABORATE (H3, interactions) | 2-4 | 25% |
| SUBGROUP | 2-3 | 15% |
| SUMMARY | 1-2 | 15% |

Total: 10-17 paragraphs typical.

## Opening Move

**Hypothesis restatement**: Briefly restate the predictions before testing. Can be a single sentence or a short paragraph.

Example pattern:
> Recall that Hypothesis 1 predicted that [X] would be positively associated with [Y]. Table 2 presents results from OLS models testing this prediction.

## Closing Move

**Summary paragraph**: Synthesize which hypotheses were supported, partially supported, or not supported. This provides a clean transition to the Discussion.

Example pattern:
> In sum, the results provide strong support for H1 and H3 but only partial support for H2. The predicted interaction effect (H4) reached significance only for [subgroup].

## Signature Techniques

1. **Explicit hypothesis-to-finding mapping**: Every hypothesis gets a verdict. Use clear language: "consistent with H1," "contrary to our expectation."

2. **Interaction effects for moderators**: Higher-numbered hypotheses often test boundary conditions via interactions. Unpack with predicted values or marginal effects.

3. **Systematic model progression tied to hypothesis sequence**: Models are sometimes labeled by hypothesis (Model H1, Model H2) or the table columns map to hypotheses.

4. **Visual presentation of interactions**: Predicted value plots with confidence intervals to interpret complex interaction patterns.

5. **Direct support/contradiction statements**: Unlike the Progressive Model Builder (which narrates what happens), the Hypothesis Tester renders verdicts.

## Theory Linking

Heavy. This is the most theory-linked cluster. Every finding is explicitly mapped to a theoretical prediction. The prose continuously references the theoretical framework.

## Table Strategy

Table-driven. Tables are often labeled by hypothesis. Prose walks through the table systematically, hypothesis by hypothesis.

## Common Pitfalls

- Treating unsupported hypotheses as failures rather than informative findings (explain what the null result *means* theoretically)
- Mechanical listing ("H1 was supported. H2 was supported. H3 was not supported.") without interpretive texture
- Forgetting to test boundary conditions when main effects are significant
