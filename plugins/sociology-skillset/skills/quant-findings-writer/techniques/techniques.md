# Writing Techniques Catalog

20 techniques observed across the 83-article corpus, ranked by frequency.

## Table of Contents

1. Statistical significance flagging (90%)
2. Magnitude contextualization (85%)
3. Coefficient interpretation in substantive terms (80%)
4. Model progression narrative (70%)
5. Visual narrative integration (70%)
6. Robustness cascade (65%)
7. Contrast with prior work (60%)
8. Subgroup stratification (55%)
9. Table walk-through (55%)
10. Attenuation tracking (50%)
11. Null finding acknowledgment (45%)
12. Interaction unpacking via predicted values (40%)
13. Concrete example from data (40%)
14. Statistical vs. practical significance distinction (35%)
15. Mechanism pathway specification (30%)
16. Temporal pattern description (25%)
17. Extended direct quotation (20%)
18. Hypothesis-to-finding mapping (15%)
19. Decomposition quantification (15%)
20. Parallel trends validation (15%)

---

## 1. Statistical significance flagging (90%)

Mark significance via asterisks, p-values, confidence intervals, or prose. Nearly universal but used with varying precision.

**Better**: "The coefficient is statistically significant (b = 0.34, p < .01, 95% CI [0.12, 0.56])."
**Worse**: "The result was significant."

## 2. Magnitude contextualization (85%)

Translate coefficients into units readers can grasp: percentages, dollars, standard deviations, or concrete comparisons.

**Pattern**: "A one-standard-deviation increase in neighborhood disadvantage is associated with a 14% increase in the odds of arrest — roughly the difference between a neighborhood at the 25th and 75th percentile."

## 3. Coefficient interpretation in substantive terms (80%)

Convert statistical outputs (log odds, hazard ratios, standardized betas) into plain-language relationships.

**Pattern**: "Moving from the lowest to the highest quartile of parental education is associated with a 2.3-year increase in completed schooling for children."

## 4. Model progression narrative (70%)

Narrate what happens as models become more complex. The trajectory of coefficients *is* the argument.

**Pattern**: "In the baseline model (Model 1), [IV] is positively associated with [DV] (b = .42, p < .001). Adding socioeconomic controls in Model 2 reduces this to .31, suggesting partial confounding. The addition of [mechanism variable] in Model 3 further attenuates the coefficient to .19, consistent with the mediation hypothesis."

## 5. Visual narrative integration (70%)

Reference figures and tables with interpretive guidance — don't let them stand alone.

**Pattern**: "As Figure 2 shows, the gap widens sharply after 2008, consistent with the recession hypothesis. The pre-2008 trends are parallel, supporting the identification strategy."

## 6. Robustness cascade (65%)

Document multiple alternative specifications systematically, organized by type.

**Pattern**: "Results are robust to (1) alternative measures of [IV] (Table A3), (2) restricting the sample to [subset] (Table A4), (3) using [alternative estimator] (Table A5), and (4) controlling for [potential confounder] (available upon request)."

## 7. Contrast with prior work (60%)

Position findings relative to existing literature — confirm, challenge, or extend.

**Pattern**: "This finding contrasts with [Author (Year)], who reported [opposite result] using [different data/method]. The divergence likely reflects [explanation]."

## 8. Subgroup stratification (55%)

Run parallel analyses within subgroups to reveal heterogeneity. Always test formally whether coefficients differ.

**Pattern**: "Table 4 presents models estimated separately for men and women. The effect of [IV] is statistically significant for women (b = .28, p < .01) but not for men (b = .08, n.s.). A Wald test confirms that these coefficients are significantly different (p < .05)."

## 9. Table walk-through (55%)

Systematically narrate through a table, interpreting key rows/columns. Selective — highlight the most important patterns rather than reading every cell.

**Pattern**: "Turning to the control variables in Table 3, education is positively associated with [DV] across all models, while age shows a curvilinear pattern (positive linear term, negative quadratic)."

## 10. Attenuation tracking (50%)

Report how a focal coefficient changes when mediators or confounders are added. Quantify the percentage reduction.

**Pattern**: "The inclusion of job characteristics reduces the gender gap from .45 to .32 — a 29% decline — suggesting that occupational segregation accounts for nearly a third of the observed disparity."

## 11. Null finding acknowledgment (45%)

Report and interpret non-significant results. Null findings are informative.

**Pattern**: "Contrary to H2, we find no significant association between [X] and [Y] (b = .03, n.s.). This null result is consistent with [Author's] argument that [mechanism] operates only under [condition]."

## 12. Interaction unpacking via predicted values (40%)

Translate complex interactions into predicted probabilities or margins at representative values.

**Pattern**: "Figure 3 plots predicted probabilities from Model 4. For respondents with high religiosity, the effect of education on tolerance is essentially flat. For those with low religiosity, each additional year of education increases predicted tolerance by 4 percentage points."

## 13. Concrete example from data (40%)

Illustrate a statistical pattern with a specific case — a city, occupation, individual, or organization from the dataset.

**Pattern**: "To put this in context, consider Detroit: with a poverty rate at the 90th percentile, the model predicts a homicide rate of [X], compared to [Y] for a city like Minneapolis at the median."

## 14. Statistical vs. practical significance distinction (35%)

Note when effects are statistically significant but small, or large but imprecise.

**Pattern**: "While the coefficient is statistically significant, the effect size is modest: a full standard deviation increase in [IV] is associated with only a 2% change in [DV] — a difference that may have limited practical import."

## 15. Mechanism pathway specification (30%)

Use X → M → Y language or sequential models to establish causal chains.

**Pattern**: "The results support the proposed mechanism: [IV] predicts [mediator] (Table 3, Panel A), [mediator] predicts [DV] controlling for [IV] (Panel B), and the indirect effect is significant in the bootstrapped mediation model (indirect effect = .08, 95% CI [.03, .15])."

## 16. Temporal pattern description (25%)

Narrate trends with dates, periods, and turning points.

**Pattern**: "Coverage shifted markedly after 2014. In the pre-period (2008-2013), the average was [X]; by 2016-2020, this had risen to [Y], representing a [Z]% increase."

## 17. Extended direct quotation (20%; 100% of content-analysis)

Use verbatim excerpts as primary evidence. Block-quote, then interpret.

**Pattern**:
> "We demand justice for our community. This isn't about politics — this is about our children's safety." (Local parent, quoted in *Tribune*, March 2019)

This quotation exemplifies the Voice template's characteristic move of centering protester testimony as legitimate civic speech.

## 18. Hypothesis-to-finding mapping (15%)

Explicitly state whether each hypothesis is supported.

**Pattern**: "Hypothesis 1, which predicted [X], is supported (b = .27, p < .01). Hypothesis 2, which predicted [Y], receives only partial support: the effect is significant for [subgroup A] but not [subgroup B]."

## 19. Decomposition quantification (15%)

Report percentage contributions from formal decomposition methods.

**Pattern**: "The Oaxaca-Blinder decomposition reveals that 62% of the Black-White gap in [outcome] is attributable to differences in observable characteristics. Of this explained portion, educational attainment accounts for the largest share (23%), followed by occupational composition (18%)."

## 20. Parallel trends validation (15%)

Test and visualize pre-treatment coefficients for causal identification.

**Pattern**: "Figure 2 plots the event study coefficients. All pre-treatment coefficients are small and statistically insignificant, supporting the parallel trends assumption. The effect emerges in the first post-treatment period and persists through year +4."
