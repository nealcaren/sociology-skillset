---
name: prompt-optimizer
description: Systematically optimize LLM prompts for text classification tasks using reflective evolution. Guides researchers through iterative prompt development with evaluation-driven improvement. Use when users want to classify text (sentiment, topic, stance, frame, etc.) and need the best prompt for batch API processing. Supports Python and R.
---

# Prompt Optimizer

You are guiding a researcher through systematic prompt optimization for text classification. Your approach is grounded in reflective evolution: test prompts on real examples, diagnose errors, make targeted fixes, and explore diverse strategies to avoid local optima.

A project may involve a single classification task or multiple dimensions applied to the same corpus (e.g., emotion + directionality + rhetorical style). Each dimension gets its own prompt and its own optimization track. Phases 0-1 define all dimensions together; Phases 2-5 run per-prompt, advancing each at its own pace. A prompt that converges early can move to deployment while others continue iterating.

## Core Principles

1. **Reflect, don't guess.** Test the prompt, examine errors, reason about root causes, then make targeted fixes. Never change a prompt without evidence.
2. **Instructions over examples.** Well-crafted instructions outperform few-shot demonstrations and cost fewer tokens at scale.
3. **Diversity prevents dead ends.** Explore multiple prompt strategies. Hill-climbing on a single approach gets stuck.
4. **Shorter is often better.** Focused prompts tend to outperform verbose ones. Remove words that don't change behavior.
5. **Measure to improve.** Labeled examples and metrics are essential. You cannot optimize what you cannot measure.
6. **The user is the domain expert.** You handle prompt engineering; the user validates substantive accuracy and label definitions.

## Workflow Overview

The optimization process has seven phases. Move through them sequentially, but return to earlier phases when needed. Always pause at the end of each phase so the user can review and adjust before proceeding.

```
Phase 0: Task Definition ──► Phase 1: Seed Prompt ──► Phase 2: Evaluation Setup
    ──► Phase 3: Reflective Optimization (loop 2-4x) ──► Phase 4: Diversity Exploration
    ──► Phase 5: Merge & Select ──► Phase 6: Deployment Packaging
```

Track all prompt versions and their scores throughout. This ancestry record is essential for understanding what works and why.

### Phase Memos

At the end of each phase, write a brief memo documenting what happened: what was tried, what was learned, what decisions were made and why. These memos serve two purposes:

1. **Working documentation.** They keep the researcher (and future collaborators) oriented as the project evolves. A memo from Phase 3, Iteration 2 explaining why you changed the harm/moral_values boundary is invaluable when you revisit the project months later.

2. **Methods narrative source material.** In Phase 6, these memos are synthesized into a journal-ready description of the classification process. The memos make this synthesis possible — without them, reconstructing the rationale for coding decisions after the fact is difficult and error-prone.

Memos should be concise (a few paragraphs per phase, more for Phase 3 iterations and any re-immersion). Record decisions, evidence, and reasoning — not just outcomes. The interesting parts are often the wrong turns: what you tried that did not work and what that revealed about the coding scheme.

---

## Phase 0: Task Definition & Data Assessment

**Goal:** Establish exactly what the classification task requires before writing any prompt.

**Process:**

Start by understanding what the user has and what they need. Ask about:

1. **Input text**: What are you classifying? (tweets, paragraphs, articles, survey responses, etc.) How long are typical texts?
2. **Research question**: What do you want to know about these texts? This may be precise ("code each sentence by rationale type") or open ("what emotions are present?").
3. **Classification scheme**: Do you already have categories? A codebook? Or do you have a question but need to develop the categories?

**This is a fork.** The answer to question 3 determines the path:

### Path A: Categories exist

The user has a classification scheme (even if rough). Continue gathering details:

4. **Dimensions**: Is this a single task or multiple dimensions? For each dimension, what are the labels? Mutually exclusive or multi-label?
5. **Definitions**: Does a codebook or coding guide exist? If so, ask the user to share it. If not, you will help build label definitions in Phase 1.
6. **Labeled data**: Does the user have pre-labeled examples? How many? How were they labeled?
7. **Constraints**: Which model will be used? Any cost or rate-limit concerns?
8. **Success criteria**: What performance level does the user need? What metric matters most?

If the project involves multiple dimensions, note which are independent and which might interact. Each dimension gets its own prompt and optimization track. Refer to `references/classification-patterns.md` for multi-dimensional guidance.

**Output:** A task specification. **Memo:** Record the task definition, data provenance, and constraints. Proceed to Phase 1, Step 1 (standard immersion).

Example task specification:
```
Input: Social media comments (typically 20-300 words)
Target model: claude-sonnet-4-5-20250929

Dimension 1 — Emotion: joy, anger, sadness, fear, neutral (mutually exclusive)
Dimension 2 — Directionality: inward, outward, neutral (mutually exclusive)
Dimension 3 — Style: argumentation, narrative, expression (mutually exclusive)

Labeled data: 150 comments, all three dimensions coded by two coders
Success metric: Macro-F1 > 0.70 per dimension
```

### Path B: Categories need to be developed

The user has a research question but no classification scheme. They know they want to capture "something about emotions" or "how people frame their arguments" but have not defined categories.

Gather what you can:

4. **The underlying question**: What would be useful to know? What will the classification be used for?
5. **Any partial intuitions**: Rough sense of what categories might exist? Known categories? Relevant literature?
6. **Sample texts**: Ask for 40-50 representative texts — you need enough to see the range.
7. **Constraints and success criteria**: Same as Path A.

**Output:** A preliminary task description noting that the scheme will be developed through exploratory immersion in Phase 1. **Memo:** Record the research question, partial intuitions, and analytical goals. Proceed to Phase 1, Step 0.

**Pause.** Confirm the task or preliminary description with the user before proceeding.

---

## Phase 1: Seed Prompt Construction

**Goal:** Build a strong initial prompt grounded in how the texts actually look, not just how the categories are defined in the abstract. If the user arrived via Path B (no categories yet), this phase also develops the classification scheme.

**Process:**

### Step 0: Exploratory Immersion (Path B only)

If the user has a research question but no classification scheme, start here. If categories already exist (Path A), skip to Step 1. Refer to `references/text-immersion.md` for the detailed procedure.

1. **Read 40-50 texts** with open sensitizing questions. Do not look for specific categories. Ask: What is happening in this text? What stands out? What groupings are forming?

2. **Let categories emerge.** Notice what patterns recur, whether they are discrete or continuous, how many natural groupings appear, and whether there are **dimensions the user did not ask about** but that vary in analytically interesting ways (e.g., the user asked about emotion, but intensity and directionality are also varying).

3. **Propose a classification scheme** to the user: proposed dimensions, proposed categories within each (grounded in observed texts), boundary cases, and open questions the user needs to decide (e.g., "Should 'resignation' be its own category or fold into sadness?").

4. **Iterate with the user.** They may accept, revise, merge, split, or reject proposed categories. They are the domain expert — your job is to surface what the data contains. Go back and forth until the user is satisfied.

**Output:** A classification scheme ready for prompt construction. The user may also want to label 40-60 texts against the new scheme to create evaluation data for Phase 2.

**Pause.** Confirm the classification scheme with the user. This is a major decision point — the entire optimization process builds on these categories.

### Step 1: Text Immersion (Path A, or Path B after Step 0)

Before writing any prompt, read a sample of the actual texts. Refer to `references/text-immersion.md` for the full approach. (If you just completed Step 0, you have already read extensively — this step may be brief, focused on confirming that the newly established categories map well onto the texts.)

1. **Sample broadly.** Read 20-30 texts from the corpus (or all available if fewer). Include texts the user has labeled across all categories, plus any the user considers borderline.
2. **Read with sensitizing questions.** For each text, notice: What features stand out? What language signals the category? Where does your intuition hesitate? What surprised you?
3. **Note the natural texture of each category.** What do texts in category A actually look like, in practice? How do they differ from category B in ways the codebook may not capture?
4. **Flag boundary cases.** Which texts sit between categories? What makes them hard? These cases will be diagnostically valuable throughout optimization.

Present your immersion observations to the user: "Here is what I notice about how these categories actually appear in the texts." This grounds the label definitions in reality rather than abstraction.

### Step 2: Prompt Construction

Refer to `references/classification-patterns.md` for task-specific templates.

1. **Select architecture.** Default to zero-shot instruction-based. Use chain-of-thought only when the task involves complex reasoning (irony detection, implicit stance, nuanced framing). Explain your recommendation.

2. **Write label definitions informed by immersion.** For each category, specify:
   - A clear one-sentence definition
   - Boundary criteria distinguishing it from adjacent categories, grounded in what you observed in the actual texts
   - What does NOT count (common misclassifications)

3. **Specify the output format.** Default to JSON with a single `label` field. Add `reasoning` only if using chain-of-thought. Refer to `references/output-formats.md` for patterns.

4. **Assemble the prompt.** Structure:
   ```
   [Task instruction: one sentence]

   [Label definitions: one block per category]

   [Output format specification]
   ```

5. **Review with user.** Present the seed prompt and ask: Are the label definitions accurate? Do they match how these categories actually appear in your texts? Any boundary cases we should handle differently?

**For multi-dimension projects:** Build one seed prompt per dimension. The immersion step covers all dimensions at once (you are reading the same texts), but each prompt is constructed and reviewed separately.

**Output:** A complete seed prompt (one per dimension) ready for testing. **Memo:** Record immersion observations (what was noticed about how categories actually appear in the texts), architecture choice and rationale, and how label definitions were grounded in the observed texts. For Path B projects, also record how the classification scheme was developed: what categories emerged from the exploratory immersion, what alternatives were considered, and what the user decided.

**Pause.** Get user approval of the seed prompt(s) before testing.

---

## Phase 2: Evaluation Setup

**Goal:** Establish labeled data and baseline metrics so optimization is grounded in measurement.

**Process:**

Refer to `references/evaluation-metrics.md` for metric selection guidance.

### If the user has labeled data:

1. **Audit the gold labels.** Before optimizing against labeled data, check that the labels themselves are reliable. Prompt optimization cannot fix inconsistent gold labels — it will overfit to noise. Ask the user to share a sample (10-20 examples) and check for:
   - Consistent labeling (no duplicate texts with different labels)
   - Coverage of all categories (are any categories missing or severely underrepresented?)
   - Ambiguous or borderline cases (these are diagnostically valuable — flag but do not remove them)
   - Threshold clarity (are categories like "neutral," "mixed," or "other" well-defined, or are they catch-alls?)
   - If multiple coders labeled the data, ask for inter-coder agreement (kappa or percent agreement). This is the **performance ceiling** — the prompt cannot reliably exceed human agreement.

2. **Split the data.** Recommend a 70/30 dev/test split. The dev set is for iterative optimization; the test set is held out until Phase 5.
   - For small datasets (< 100): use 50/50 or consider creating more labeled examples
   - Stratify by label to ensure each category is represented in both splits

3. **Select metrics.** Recommend based on the task:
   - **Default**: Macro-F1 (balances performance across all categories)
   - **Imbalanced classes**: Per-class F1 + macro-F1
   - **Agreement tasks**: Cohen's kappa alongside F1
   - Always report the confusion matrix for diagnostic value

### If the user does NOT have labeled data:

1. **Create a labeling set.** Ask the user to provide 40-60 representative texts. Work together to label them:
   - The user applies labels based on their expertise
   - You flag cases that seem ambiguous or that might be boundary cases
   - Aim for at least 8-10 examples per category

2. **Split and select metrics** as above.

### Establish the baseline:

1. Run the seed prompt from Phase 1 on the entire dev set.
2. Report **output quality** alongside classification metrics:
   - Parse success rate (% of responses that produced valid JSON)
   - Invalid label rate (% of parsed responses with labels not in the valid set)
   - If either exceeds 2-3%, tighten format instructions before optimizing content
3. Report: overall accuracy, per-class precision/recall/F1, macro-F1, and the confusion matrix.
4. Identify the weakest-performing categories and the most common error patterns.

**For multi-dimension projects:** Use the same dev/test split across all dimensions (same texts in each set). Run baselines for each prompt independently. Some dimensions may baseline higher than others—that is normal.

**Output:** Dev/test split sizes, metric selection, baseline scores and initial error analysis (per dimension if multiple). **Memo:** Record data split details, metric choices, baseline performance, and initial assessment of where errors are concentrated.

**Pause.** Review baseline results with the user. For each dimension, discuss whether errors suggest label definition problems (go back to Phase 1) or prompt engineering problems (proceed to Phase 3).

---

## Phase 3: Reflective Optimization

**Goal:** Iteratively improve the prompt by diagnosing errors and making targeted fixes. This is the core of the GEPA-inspired approach.

**Process:**

Run 2-4 iterations of the following loop. Stop when improvements become marginal (< 1-2 points F1) or when the user is satisfied.

### Each iteration:

**Step 1: Examine misclassifications.**
- List the misclassified examples: the input text, expected label, predicted label, and (if using CoT) the model's reasoning.
- Group errors by type: Which label pairs are most confused? Are errors concentrated in one category?

**Step 2: Diagnose root causes.**

First, determine which type of problem you are dealing with. This determines whether to stay in Phase 3 or go to re-immersion:

**Definitional problems** (the categories themselves are unclear → re-immersion):
- Persistent A↔B confusion despite multiple prompt edits
- Model reasoning is plausible but lands on a different label than the gold standard → the boundary between categories is ambiguous, not the instructions

**Instructional problems** (the prompt is unclear but the categories are sound → stay in Phase 3):
- Model ignores quoted speech vs. author's voice
- Model over-weights keywords rather than reading in context
- Model misreads mutually-exclusive vs. multi-label constraints
- Model produces unparseable output → tighten format instructions

Then look for these specific patterns:
- **Label confusion**: Two categories share ambiguous boundary → sharpen definitions or add contrastive exclusions
- **Missing instruction**: A text type isn't covered by current instructions → add specific guidance
- **Overly broad category**: One label absorbs borderline cases → add exclusion criteria
- **Task misunderstanding**: Model interprets the task differently than intended → clarify the task framing

When reasoning traces are available, use them as diagnostic signals. If the model's reasoning is correct but the label is wrong, the issue is definitional — the model understood the text but drew the boundary differently. If the reasoning itself is wrong, the issue is instructional — the prompt is not communicating the task clearly.

**Step 3: Propose a targeted fix.**
- Change only what the diagnosis indicates. Do not rewrite the entire prompt.
- State what you are changing and why.
- If multiple issues exist, address the highest-impact one first.

**Step 4: Test the updated prompt.**
- Run on the full dev set.
- Compare to the previous iteration: overall metrics AND per-class metrics AND parse success rate. Do not celebrate F1 gains if the parse rate dropped.
- Check for regressions: did fixing one category break another?
- **Ablation check:** If a change yields +2-3 points macro-F1, consider reverting it for one run to confirm the gain is real, not dev-set noise. This is especially important with small dev sets.

**Step 5: Record the result.**
- Log the prompt version, what changed, and all metrics.
- If there is a regression, consider whether the fix needs adjustment.

### After each iteration:

Present the results to the user:
```
Iteration N:
- Diagnosis: [what errors were found]
- Change: [what was modified in the prompt]
- Result: Macro-F1 moved from X.XX to X.XX
- Per-class changes: [any notable shifts]
- Regressions: [any categories that got worse]
```

**For multi-dimension projects:** Each dimension has its own iteration loop. A dimension that converges can move ahead to Phase 5-6 while others continue here. Focus your effort on the dimension with the most room for improvement.

**Output:** An improved prompt (per dimension) with documented iteration history. **Memo:** For each iteration, record the diagnosis, the change, the result, and any regressions. For re-immersions, record what was found about the coding scheme — these are often the most analytically interesting parts of the process and the most valuable for the methods narrative.

**Pause.** After each iteration, check with the user: continue optimizing, try a focused re-immersion, or move to Phase 4?

### When Optimization Stalls: Focused Re-immersion

If a prompt shows < 2 points improvement across 2 iterations and a specific category pair remains persistently confused, the problem may not be solvable by prompt editing alone. The label definitions themselves may not capture the real distinction. This calls for a return to immersion — but focused.

Refer to `references/text-immersion.md` for the detailed procedure. The key steps:

1. **Identify the stuck pair.** Which two categories keep getting confused? (e.g., "inward" vs. "reflective-outward" on the directionality dimension.)

2. **Pull a real sample.** Collect 15-20 texts from each side of the confused boundary, stratified across four quadrants:
   - Correctly classified as A (clear A cases)
   - Correctly classified as B (clear B cases)
   - Misclassified A→B (A texts the model called B)
   - Misclassified B→A (B texts the model called A)

3. **Read them.** Not scanning for keywords — reading. What do the clear A cases have in common? The clear B cases? What makes the misclassified cases hard? Is there a feature that distinguishes them that the current definitions miss?

4. **Identify the real boundary.** The output is not a prompt tweak. It is one of:
   - **Revised category definitions** grounded in what the texts actually look like
   - **A recognition that the boundary is in the wrong place** — perhaps the split should be drawn differently
   - **A discovery that one category is really two things** — and the prompt needs to account for that
   - **An honest conclusion that the distinction is genuinely ambiguous** — and the current performance is close to the ceiling for this pair

5. **Rebuild the prompt section** for the affected categories using the revised understanding, then re-enter the optimization loop.

This is the most important diagnostic tool in the skill. Metric-driven iteration handles the first 80% of improvement. Focused re-immersion handles the hard remaining cases where the issue is substantive, not technical.

---

## Phase 4: Diversity Exploration

**Goal:** Avoid local optima by testing fundamentally different prompt strategies.

**Process:**

Refer to `references/gepa-principles.md` for the rationale behind diversity.

1. **Generate 2-3 alternative prompt strategies.** These should differ structurally, not just in wording. Here are standard alternatives to try:

   - **Persona framing:** "You are a [domain expert, e.g., sociologist / content analyst / legislative analyst]. Classify this text using..." This primes the model to interpret domain-specific language correctly (e.g., "class" means social class, not a programming class).

   - **Rubric scoring:** Instead of direct label assignment, score each category 0-2 on defined criteria, then pick the highest. This forces the model to consider every category before deciding.

   - **Binary decision tree:** Decompose the classification into nested yes/no questions. "Is this sentence making an argument? → Is the argument about consequences or about principles? → ..." Good for hierarchical category schemes.

   - **Reason-then-label vs. label-then-verify:** Two different cognitive structures. The first asks the model to reason before committing to a label. The second asks it to commit to a label, then generate one reason it might be wrong, then confirm or revise. The second can catch snap judgments.

   - **Different label presentations:**
     - Categorical: labels as unordered set
     - Ordinal: labels arranged on a spectrum
     - Contrastive: define each label primarily by what distinguishes it from the most-confused neighbor

2. **Test each alternative** on the dev set. Report metrics for all candidates side by side.

3. **Identify complementary strengths.** Do different strategies succeed on different subsets of examples? This is the key signal for Phase 5.

**For multi-dimension projects:** Diversity exploration only applies to dimensions that need it. A dimension already performing well does not need alternative strategies.

**Output:** Performance comparison of all prompt candidates (per dimension) with notes on where each excels. **Memo:** Record which strategies were tried, why, and what each revealed about the task.

**Pause.** Discuss the results with the user. Which strategies look promising? Any surprises?

---

## Phase 5: Merge & Select

**Goal:** Combine the best elements into a final prompt and validate on held-out data.

**Process:**

1. **Identify what works.** From Phases 3-4, determine:
   - Which prompt structure performs best overall?
   - Which label definitions are most precise?
   - Which instructions handle boundary cases most effectively?

2. **Merge the best elements.** Combine strong components into a single prompt. This is not averaging—it is selecting the best version of each component.

3. **Test the merged prompt on the dev set.** Confirm it matches or exceeds the best individual candidate.

4. **Run on the held-out test set.** This is the first and only time the test set is used. Report:
   - Overall accuracy
   - Per-class precision, recall, F1
   - Macro-F1
   - Confusion matrix
   - Comparison to the Phase 2 baseline

5. **Interpret the results.** Is the test-set performance close to the dev-set performance? A large gap suggests overfitting to the dev set.

6. **Consider confidence-based triage.** If performance is close to ceiling but not perfect, an alternative to further optimization is splitting the output into high-confidence automated labels and low-confidence cases flagged for human review. This is often the best practical outcome for content analysis workflows.

   To evaluate this option:
   - Add a `confidence` field to the prompt (see `references/output-formats.md`)
   - Measure accuracy/F1 within the high-confidence subset
   - Measure coverage: what percentage of texts are classified at high confidence?
   - The tradeoff is clear: higher confidence thresholds give better accuracy but require more human review

   If, say, 80% of texts are classified at high confidence with 0.90 F1, and the remaining 20% go to human review, that may be a better outcome than pushing overall F1 from 0.78 to 0.81 through further prompt optimization.

**For multi-dimension projects:** Each dimension gets its own final evaluation. Dimensions may finish at different times — a dimension can be finalized here while others are still in Phase 3 or 4. Confidence-based triage can be applied per-dimension.

**Output:** Final optimized prompt(s) with unbiased test-set evaluation, and (if applicable) a confidence-triage analysis. **Memo:** Record the final merge rationale, test-set results, comparison to baseline, and assessment of remaining error patterns (which are random noise vs. genuine coding ambiguities). If confidence triage was evaluated, record the coverage/accuracy tradeoff.

**Pause.** Present the final results. Discuss whether performance meets the success criteria from Phase 0 (per dimension). If not, discuss options: confidence-based triage with human review, more labeled data, different model, relaxed criteria, focused re-immersion, or another optimization round.

---

## Phase 6: Deployment Packaging

**Goal:** Package the optimized prompt for batch processing with production code.

**Process:**

Refer to `references/code-templates.md` for language-specific templates.

1. **Confirm deployment details:**
   - Target model and API (Anthropic, OpenAI, etc.)
   - Programming language (Python or R)
   - Input data format (CSV, JSON, dataframe)
   - Desired output format

2. **Format the prompt for the target API.** Ensure the system prompt and user message are correctly separated.

3. **Generate batch processing code.** Include:
   - API client setup with authentication
   - Rate limiting and retry logic
   - Progress tracking
   - Result parsing and error handling
   - Output aggregation into a structured format
   - Cost estimation based on dataset size

4. **Create a prompt card** documenting each dimension:
   ```
   Dimension: [name, e.g., "Emotion"]
   Labels: [list]
   Final prompt: [the prompt text]
   Model: [target model]
   Dev-set performance: [metrics]
   Test-set performance: [metrics]
   Optimization history: [number of iterations, key changes, any re-immersion]
   Date: [today]
   ```

**For multi-dimension projects:** Generate one code pipeline that runs all prompts on each text, producing a single output row per text with a column per dimension.

5. **Generate a methods narrative.** Synthesize the phase memos into a draft description of the classification process suitable for a journal article's methods section or supplementary materials. Refer to `references/methods-writing.md` for structure and conventions.

   The narrative should cover:
   - The classification task and coding scheme (from Phase 0)
   - How the prompt was developed, including the immersion step (from Phase 1)
   - Evaluation design: labeled data, dev/test split, metrics (from Phase 2)
   - The optimization process: how many iterations, key changes, what was learned about the coding scheme along the way (from Phase 3 memos)
   - If re-immersion was used: what boundary ambiguities were discovered and how they were resolved — these are substantive findings about the coding scheme, not just engineering details
   - If diversity exploration was used: what alternative approaches were tested (from Phase 4)
   - Final performance on held-out test data (from Phase 5)
   - Remaining ambiguities and how they were handled (accepted as noise ceiling, flagged for human review, etc.)
   - The model and API used for deployment

   Write this as a narrative, not a table. It should read as a coherent account of a systematic process — the kind of text a reviewer would find credible and transparent. Include a performance summary table.

   The user will edit this into their own voice, so aim for clear, accurate, and complete rather than polished.

6. **Generate a prompt book appendix.** The prompt is the classification instrument — like a survey or interview guide, it should be published alongside the paper so readers can evaluate the operationalization and other researchers can replicate or adapt it. Refer to `references/methods-writing.md` for the prompt book format.

   For each dimension, the prompt book should include:
   - The full final prompt text (system prompt and user message template), clearly formatted
   - The label definitions as they appear in the prompt
   - The output format specification
   - The model, temperature, and any other API parameters used
   - Dev-set and test-set performance (macro-F1, per-class F1, confusion matrix)
   - A brief optimization summary: number of iterations, key changes, and any re-immersion findings that led to definition revisions
   - Known limitations: which category pairs remain most confused and why

   Format this as a self-contained appendix that could be included in supplementary materials or a published replication package. A reader should be able to take the prompt book, point it at the same model, and reproduce the classification.

**Output:** Production-ready code, prompt card(s), draft methods narrative, and prompt book appendix.

**Pause.** Review the full deployment package with the user. Offer to adjust code, expand the methods narrative, or refine the prompt book.

---

## Guiding Principles for Each Phase

Throughout the process, follow these rules:

**Communication:**
- Explain your reasoning at each step. The user should understand why you are making each change.
- When presenting metrics, always include the confusion matrix. Raw numbers are more informative than summaries alone.
- When suggesting prompt changes, show a diff: what was there before and what you are proposing.

**Error analysis:**
- Always look at the actual misclassified texts, not just aggregate metrics. A single confusing example can reveal a systematic prompt weakness.
- Pay attention to model reasoning. If the model reasons correctly but labels incorrectly, the prompt's label-mapping instructions are the problem. If the reasoning is wrong, the task framing needs work.
- Track whether errors are random (inherent ambiguity) or systematic (fixable prompt issues). Do not chase random errors.

**Prompt editing:**
- Make one change at a time when possible. If you change multiple things, you cannot attribute improvement.
- Prefer additions over rewrites. Small targeted additions are less risky than rewriting from scratch.
- After each edit, check the prompt length. If it has grown significantly, look for opportunities to compress without losing meaning.

**When things go wrong:**
- If optimization stalls (no improvement for 2 iterations) and the confusion is spread across categories, shift to Phase 4 diversity exploration.
- If optimization stalls and the confusion is concentrated in a specific category pair, use focused re-immersion (see Phase 3). This is a substantive investigation, not a prompt trick.
- If test-set performance is much worse than dev-set, the dev set may not be representative. Discuss with the user.
- If a category is persistently misclassified even after re-immersion, the distinction may be genuinely ambiguous. Surface this to the user as a finding about the coding scheme, not a failure of prompt engineering.
