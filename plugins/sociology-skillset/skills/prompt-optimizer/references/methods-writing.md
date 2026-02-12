# Methods Narrative Writing Guide

How to synthesize the phase memos into a journal-quality description of the prompt optimization and classification process. This text typically appears in the Methods section of a research article or in supplementary materials.

## What Reviewers Want to See

Reviewers evaluating LLM-based classification need to trust that the process was systematic and that the results are credible. The methods narrative should demonstrate:

1. **The coding scheme was well-defined.** Categories had clear definitions, and ambiguous boundaries were identified and addressed.
2. **The classification was validated.** Performance was measured on labeled data with appropriate metrics, using a held-out test set.
3. **The process was iterative and evidence-driven.** The prompt was not guessed at — it was developed through systematic evaluation and refinement.
4. **Remaining ambiguities are acknowledged.** The researcher knows where the classifier struggles and has a principled account of why.
5. **The process is reproducible.** Another researcher could use the same prompt and expect similar results.

## Narrative Structure

### Opening: The Classification Task

What was classified, into what categories, and why. Keep this brief — the coding scheme is usually described elsewhere in the paper. Here, just establish what the LLM was asked to do.

```
We used [model] to classify [N] [text type] along [number] dimensions:
[dimension 1] ([labels]), [dimension 2] ([labels]), etc. Classification
was performed at the [sentence/paragraph/document] level.
```

If the project has multiple dimensions, briefly note whether they were classified by separate prompts or a single combined prompt, and why.

### Prompt Development Process

This is the core of the narrative. Describe the process, not just the outcome.

**Initial immersion.** Note that the prompt was grounded in qualitative reading of sample texts before definitions were written. This signals methodological care — the researcher did not simply hand a codebook to the model.

```
Before constructing the classification prompt, we read [N] sample texts
to understand how each category manifests in practice. This immersion
step revealed [key observation, e.g., "that the rationale categories
are distinguished by rhetorical frame rather than topical content"],
which informed the label definitions used in the prompt.
```

**Iterative optimization.** Describe the optimization loop without exhaustive detail. Reviewers want to know the process existed and was systematic, not the specifics of every iteration.

```
We evaluated the initial prompt against [N] hand-coded [text type]
(dev set, [N]; held-out test set, [N]) and iteratively refined the
prompt over [N] iterations. Each iteration involved examining
misclassified texts, diagnosing error patterns (e.g., confusion
between [category A] and [category B]), and making targeted
modifications to the label definitions. [Metric] improved from
[baseline] to [final] on the dev set across these iterations.
```

**Focused re-immersion (if used).** This is worth calling out explicitly because it demonstrates that the researcher engaged with substantive coding questions, not just engineering problems.

```
When optimization stalled on the [dimension] dimension — specifically,
persistent confusion between [category A] and [category B] — we
conducted a focused re-examination of [N] texts from each side of the
boundary, including both correctly and incorrectly classified examples.
This revealed [substantive finding, e.g., "that compound sentences
containing both a biological claim and a normative conclusion were
consistently coded by the gold standard based on the premise rather
than the conclusion"]. We revised the label definitions to incorporate
this distinction.
```

**Alternative strategies (if Phase 4 was used).** Briefly note that multiple prompt architectures were tested.

```
We also tested [N] alternative prompt strategies, including [brief
descriptions]. [Strategy X] performed best overall and was selected
for the final prompt.
```

### Validation

Report test-set performance. This is where the numbers go.

```
The final prompt was evaluated on the held-out test set ([N] [text type]).

| Dimension | Macro-F1 | Accuracy | Per-class F1 range |
|-----------|----------|----------|--------------------|
| [dim 1]   | X.XX     | XX%      | X.XX – X.XX        |
| [dim 2]   | X.XX     | XX%      | X.XX – X.XX        |
```

If relevant, note how this compares to human inter-rater reliability:

```
For comparison, inter-coder agreement on [dimension] was [kappa/F1],
suggesting the classifier approaches human-level performance on this
task.
```

### Remaining Ambiguities

Acknowledge what the classifier does not handle well. This is a strength, not a weakness — it shows the researcher understands the limits.

```
The remaining classification errors cluster around [N] boundary zones:
[brief description of each]. These reflect genuine ambiguities in the
coding scheme — cases where [the distinction depends on X, which is
inherently difficult to operationalize at the sentence level]. We
addressed these by [flagging low-confidence cases for human review /
accepting the performance as near the reliability ceiling / revising
the coding scheme to merge categories X and Y].
```

### Deployment Details

Brief note on the technical setup.

```
Classification was performed using [model] via the [API] with
[temperature/parameters]. Each [text type] was classified independently.
The total classification cost was approximately $[X] for [N] texts.
The prompt and batch processing code are available at [repository/DOI].
```

## Tone and Framing

**Write as a methods description, not a technical report.** The audience is social scientists, not ML engineers. Emphasize the substantive decisions (how categories were defined, what ambiguities were discovered, how they were resolved) over the technical ones (JSON output format, rate limiting, API parameters).

**Frame the process as coding, not engineering.** The prompt optimization process is analogous to iterative codebook refinement in manual content analysis. The researcher examines cases, identifies where the coding scheme is unclear, and revises definitions. The fact that the "coder" is an LLM does not change the logic.

**Report what was learned about the data.** The most credible methods narratives are those where the classification process itself produced substantive insights. If the re-immersion revealed that "harm" in the coding scheme is broader than physical harm, or that "distrust" is about the actor rather than the act, say so — these findings demonstrate engagement with the material.

**Be transparent about limitations.** Note the model used, the date, and the fact that performance may vary with different models or updated model versions. If the classifier was validated on one type of text, note that generalization to other text types is not guaranteed.

## What NOT to Include

- Exhaustive prompt text in the main article (put it in supplementary materials or a repository)
- Every iteration's metrics (summarize the trajectory: "improved from X to Y over N iterations")
- Technical API details beyond model name and basic parameters
- Jargon that the target audience will not understand ("macro-F1" is fine for most social science audiences; "Pareto-optimal prompt candidates" is not)

## Example: Compact Methods Paragraph

For papers with tight word limits, the entire classification process can be described in a single paragraph:

```
We classified [N] [text type] along [N] dimensions using [model].
The classification prompt was developed through an iterative process:
we first read [N] sample texts to ground label definitions in the
observed data, then tested the prompt against [N] hand-coded examples
and refined the definitions over [N] iterations based on error
analysis. When persistent confusion between [categories] could not
be resolved through prompt refinement, we conducted a focused
re-examination of boundary cases, which revealed [key finding] and
led to revised definitions. The final prompt achieved [metric] = X.XX
on a held-out test set of [N] texts, comparable to inter-coder
reliability of X.XX. The prompt, validation data, and processing
code are available at [link].
```

## Example: Extended Methods Subsection

For papers with space for a full methods subsection on the classification process (or for supplementary materials), use the full narrative structure above. Typically 400-800 words covering task definition, prompt development (with immersion and re-immersion noted), validation results with a performance table, and remaining ambiguities.

---

## Prompt Book Appendix

The prompt is the classification instrument. Just as a survey researcher publishes the questionnaire and an interview researcher publishes the interview guide, an LLM-based classification study should publish the prompt. The prompt book is a self-contained appendix (typically supplementary materials) that enables evaluation, replication, and adaptation.

### Structure

For each classification dimension, include the following sections:

**1. Task Description**

One paragraph: what is being classified, the unit of analysis, and the categories.

**2. Full Prompt Text**

The complete prompt as sent to the model, clearly formatted. Separate the system prompt from the user message template. Use a monospace code block. Do not paraphrase or abbreviate — this is the instrument, and it should be reproduced exactly.

```
System prompt:
[full system prompt text]

User message:
[full user message template, with {text} placeholder]
```

**3. Label Definitions**

The label definitions as they appear in the prompt, reproduced here for easy reference. If the definitions evolved during optimization, present only the final versions — the optimization history goes in the next section.

**4. Output Format**

The expected output format (e.g., JSON schema) and how it was parsed.

**5. Model and Parameters**

- Model name and version (e.g., claude-sonnet-4-5-20250929)
- Temperature and any other generation parameters
- API version and date of classification runs
- Note: model behavior may change with updates; results were validated with the version listed above

**6. Validation Performance**

A table with dev-set and test-set performance:

```
| Metric              | Dev set (N=X) | Test set (N=X) |
|---------------------|---------------|----------------|
| Overall accuracy    | XX.X%         | XX.X%          |
| Macro-F1            | X.XX          | X.XX           |
| [Class A] F1        | X.XX          | X.XX           |
| [Class B] F1        | X.XX          | X.XX           |
| ...                 | ...           | ...            |
| Cohen's kappa       | X.XX          | X.XX           |
```

Include the test-set confusion matrix.

**7. Optimization Summary**

A brief account of how the prompt was developed. Not every iteration — just the key moves:
- How many iterations of optimization
- The most important changes and why they were made
- Any focused re-immersion: what boundary ambiguity was investigated, what was found, how the definitions were revised
- Trajectory: baseline performance → final performance

This section provides the rationale behind the prompt's design. A reader should understand not just what the prompt says but *why* it says it that way — what coding decisions are embedded in specific phrasings.

**8. Known Limitations**

Which category pairs remain most confused and why. What types of texts the classifier handles poorly. Any boundary ambiguities that were identified but could not be fully resolved. This helps other researchers who adapt the prompt know where to watch for errors.

### Formatting Notes

- The prompt book should be self-contained: a reader should not need to read the methods section to understand it.
- Use clear section headers so readers can navigate directly to the prompt text or the performance metrics.
- For multi-dimension projects, repeat the full structure for each dimension. Each dimension's prompt book section should be independently readable.
- If the prompt book is long (multiple dimensions, extended optimization histories), consider structuring it as a separate supplementary document rather than an inline appendix.
