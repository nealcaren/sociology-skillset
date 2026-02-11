# Decomposition Analyst

~11/83 articles. Overrepresented in administrative-data and secondary-survey-analysis. Centers on partitioning variance, effects, or gaps into constituent components.

## Defining Feature

The core analytic move is formal decomposition: Oaxaca-Blinder, Kitagawa, Fairlie, mediation analysis, or variance partitioning. The argument hinges on *how much* of a gap, disparity, or effect is explained by specific factors.

## Canonical Arc

```
DESCRIBE → BASELINE → DECOMPOSE → MECHANISM → ROBUSTNESS
```

## Paragraph Budget

| Move | Paragraphs | Share |
|------|-----------|-------|
| DESCRIBE | 2-3 | 15% |
| BASELINE | 2-3 | 15% |
| DECOMPOSE | 3-5 | 30% |
| MECHANISM | 2-4 | 20% |
| ROBUSTNESS | 2-3 | 20% |

Total: 11-18 paragraphs typical.

## Opening Move

**Descriptive overview**: Establish the gap or disparity to be explained. This grounds the decomposition that follows.

Example pattern:
> Figure 1 shows the racial gap in [outcome]. Black respondents report [X], compared to [Y] for white respondents — a difference of [Z] percentage points. What accounts for this gap?

## Closing Move

**Mechanism test** or **robustness checks**: End by showing which pathways explain the largest share of the gap, or by demonstrating stability across alternative decomposition specifications.

## Signature Techniques

1. **Percentage contribution quantification**: "Educational differences account for 34% of the gap, while occupational sorting explains an additional 18%."

2. **Sequential pathway testing**: Build the decomposition incrementally, adding blocks of explanatory factors to show which matter most and in what order.

3. **Suppression effect narratives**: Report cases where controlling for a factor *increases* the focal gap — the suppression reveals a hidden offsetting mechanism.

4. **Between vs. within decomposition**: Separate the "characteristics effect" (groups differ in X) from the "coefficients effect" (groups get different returns to X).

5. **Visual pie/bar charts of contribution shares**: Figures showing the relative importance of different factors in explaining the gap.

## Theory Linking

Moderate to heavy. Decomposition results are interpreted as evidence for or against specific causal pathways proposed by the theory section. Each decomposition component maps to a theoretical mechanism.

## Table Strategy

Hybrid. Tables show decomposition components (with both absolute and percentage contributions), but prose interprets the substantive meaning of each pathway.

## Common Pitfalls

- Presenting raw decomposition output without substantive interpretation of each component
- Ignoring the unexplained portion of the gap — this is often the most theoretically interesting part
- Failing to test sensitivity of decomposition results to ordering of variables (when order matters)
