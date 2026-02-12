# Temporal Tracker

~9/83 articles. Overrepresented in administrative-data and content-analysis. Time is the primary organizing axis.

## Defining Feature

The section follows a temporal logic — trends, periodization, event studies, or trajectories. The argument turns on *when* things changed and *how* patterns evolved.

## Canonical Arc

```
TEMPORAL → BASELINE → TEMPORAL (detailed) → SUBGROUP → ROBUSTNESS
```

## Paragraph Budget

| Move | Paragraphs | Share |
|------|-----------|-------|
| TEMPORAL (overview) | 3-5 | 20% |
| BASELINE | 2-3 | 15% |
| TEMPORAL (detailed) | 4-6 | 30% |
| SUBGROUP | 2-3 | 15% |
| ROBUSTNESS | 2-3 | 20% |

Total: 13-20 paragraphs typical.

## Opening Move

**Descriptive visualization**: Open with a time-series figure or descriptive trend before moving to models.

Example pattern:
> Figure 1 displays the trend in [DV] from [start year] to [end year]. The series reveals [pattern]: [description]. The vertical line marks [event], after which [change].

## Closing Move

**Summary of temporal pattern** or **robustness with alternative periodization**: End by synthesizing the temporal story or testing whether results hold under different time windows.

## Signature Techniques

1. **Event study design with pre/post**: Present coefficients for periods before and after a treatment/event, emphasizing the pre-period as validation and the post-period as effect.

2. **Parallel trends testing**: Show that treatment and control groups followed similar trajectories before the event — the identification assumption. Visualize with confidence intervals.

3. **Chronological narrative with periodization**: Divide the time span into meaningful eras and narrate patterns within each period.

4. **Dynamic/lagged effects**: Show how effects unfold over time — immediate, short-term, and long-term impacts.

5. **Temporal heterogeneity analysis**: Test whether the effect is stronger in early vs. late periods, or whether it fades, grows, or reverses over time.

## Theory Linking

Moderate. Temporal patterns are linked to historical events, policy changes, or theoretical predictions about social change. Theory explains *why* the timing matters.

## Table Strategy

Figure-driven or hybrid. Time-series plots and event study graphs carry much of the argument. Tables supplement with precise coefficient estimates.

## Common Pitfalls

- Presenting temporal patterns without connecting them to substantive events or theoretical mechanisms
- Showing only the post-event period without establishing the pre-event baseline
- Ignoring anticipation effects (changes before the event that suggest endogeneity)
