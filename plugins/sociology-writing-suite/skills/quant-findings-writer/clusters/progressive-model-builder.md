# Progressive Model Builder

The most common cluster (~28/83 articles). Dominant in secondary-survey and administrative-data papers that use regression as the primary analytic tool.

## Defining Feature

Build from simple to complex specifications, narrating how focal coefficients change (persist, attenuate, reverse) as controls, interactions, and alternative specifications are added. The progression itself is the argument.

## Canonical Arc

```
DESCRIBE → BASELINE → ELABORATE → MECHANISM → ROBUSTNESS
```

## Paragraph Budget

| Move | Paragraphs | Share |
|------|-----------|-------|
| DESCRIBE | 2-3 | 15% |
| BASELINE | 2-3 | 15% |
| ELABORATE | 3-5 | 30% |
| MECHANISM | 2-3 | 15% |
| ROBUSTNESS | 3-5 | 25% |

Total: 12-19 paragraphs typical.

## Opening Move

**Table reference** (most common): Direct the reader to Table 1 or a descriptive figure. Establish the baseline phenomenon before modeling it.

Example pattern:
> Table 1 presents descriptive statistics for the full sample. The mean level of [DV] is [value], with [notable variation]. [Key IV] ranges from [min] to [max], with a standard deviation of [sd].

## Closing Move

**Robustness checks** or **supplemental reference**: End by demonstrating that the main results survive alternative specifications, samples, or measurement strategies.

## Signature Techniques

1. **Model progression narrative**: "Model 1 includes only [IV] and basic demographics. In Model 2, I add [controls]. The coefficient on [IV] declines from [b1] to [b2], suggesting that [interpretation]."

2. **Attenuation tracking**: Explicitly narrate coefficient changes across nested models. Percentage reduction signals mediation or confounding.

3. **Magnitude contextualization**: "A one-standard-deviation increase in [IV] is associated with a [X]% increase in [DV], roughly equivalent to [concrete comparison]."

4. **Sequential control addition**: Each model adds a theoretically motivated block of controls, with the prose explaining *why* each block matters and what its inclusion reveals.

5. **Nested model comparison**: Reference fit statistics (AIC, BIC, log-likelihood ratio tests) when models are formally nested.

## Theory Linking

Moderate to heavy. Each model step connects to a theoretical claim: "The persistence of the effect after controlling for [Z] is inconsistent with the [alternative explanation] account."

## Table Strategy

Hybrid. Tables are the scaffolding — typically one main table with 3-6 columns showing progressive model builds — but prose does the interpretive work of explaining *what changes and why*.

## Common Pitfalls

- Describing every coefficient in every model (select the focal variables; control summaries go in footnotes or appendix)
- Front-loading all descriptive statistics without connecting them to the analytic strategy
- Robustness checks that repeat the same result without adding new information (vary the *type* of check: alternative measures, samples, methods)
