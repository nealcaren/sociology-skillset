# Subgroup Comparator

~16/83 articles. Appears across all method types. Organizes findings around systematic comparison across predefined groups.

## Defining Feature

The central question is *for whom* or *in what contexts* an effect operates differently. The section is structured around presenting parallel analyses across theoretically meaningful subgroups (race, gender, class, institutional type, national context).

## Canonical Arc

```
DESCRIBE → BASELINE → SUBGROUP → COMPARISON → ROBUSTNESS
```

## Paragraph Budget

| Move | Paragraphs | Share |
|------|-----------|-------|
| DESCRIBE | 2-3 | 15% |
| BASELINE | 2-3 | 15% |
| SUBGROUP | 5-8 | 35% |
| COMPARISON | 2-3 | 15% |
| ROBUSTNESS | 1-2 | 10% |

Total: 12-19 paragraphs typical.

## Opening Move

**Sample description**: Establish group composition and baseline differences across groups before turning to models.

Example pattern:
> Table 1 presents descriptive statistics separately by [grouping variable]. Notable differences emerge: [Group A] reports significantly higher levels of [DV] than [Group B] (p < .001), and the groups also differ on several key covariates.

## Closing Move

**Subgroup synthesis** or **summary paragraph**: End by synthesizing the pattern of heterogeneity — for which groups do effects hold, and what does this pattern reveal?

## Signature Techniques

1. **Stratified analysis with parallel specifications**: Run identical models within each subgroup. Present side-by-side in tables with columns labeled by group.

2. **Interaction effects unpacking**: When using pooled models with interactions, unpack with predicted values or marginal effects at representative values of the moderator.

3. **Cross-group coefficient tests**: Formally test whether coefficients differ across groups using Wald tests, Chow tests, or z-tests for cross-equation coefficient equality.

4. **Group-specific narrative interpretation**: Dedicate separate paragraphs to each group's results before comparing. Resist the urge to compare prematurely.

5. **Comparative synthesis paragraphs**: After presenting each group, write a dedicated comparison paragraph: "The divergent patterns across [groups] suggest that..."

## Theory Linking

Moderate. Subgroup differences are interpreted as evidence for group-specific mechanisms or boundary conditions predicted by theory.

## Table Strategy

Hybrid to table-driven. Tables with parallel columns (one per subgroup) are the workhorse. Prose highlights the key differences rather than narrating every cell.

## Common Pitfalls

- Comparing coefficients across groups without formal statistical tests (cross-group differences may not be significant even if one coefficient is significant and the other is not)
- Presenting too many subgroup breakdowns without theoretical motivation
- Failing to discuss why groups differ, not just that they differ
