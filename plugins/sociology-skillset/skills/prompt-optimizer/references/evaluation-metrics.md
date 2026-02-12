# Evaluation Metrics Reference

Metrics for evaluating text classification prompts. Use this reference when setting up evaluation in Phase 2 and interpreting results in Phases 3-5.

## Core Metrics

### Accuracy

**What it measures:** The proportion of correctly classified examples out of all examples.

**Formula:** `correct / total`

**When to use:** Only when classes are roughly balanced. With imbalanced data, accuracy is misleading—a classifier that always predicts the majority class can achieve high accuracy while failing completely on minority classes.

**When NOT to use:** Imbalanced datasets (e.g., 90% neutral, 5% positive, 5% negative).

### Precision

**What it measures:** Of all examples the model labeled as class X, how many actually are class X.

**Formula:** `true positives / (true positives + false positives)`

**Interpretation:** High precision means few false alarms. When the model says "positive," it is usually right.

**When it matters most:** When false positives are costly (e.g., flagging content for removal—you do not want to incorrectly flag acceptable content).

### Recall

**What it measures:** Of all examples that actually are class X, how many did the model correctly identify.

**Formula:** `true positives / (true positives + false negatives)`

**Interpretation:** High recall means few missed cases. The model catches most of the actual positives.

**When it matters most:** When false negatives are costly (e.g., detecting harmful content—you do not want to miss any).

### F1 Score

**What it measures:** The harmonic mean of precision and recall for a single class.

**Formula:** `2 * (precision * recall) / (precision + recall)`

**Interpretation:** Balances precision and recall. An F1 of 0.80 means both precision and recall are reasonably high (though not necessarily equal).

**Per-class F1:** Compute F1 separately for each category. This is the most diagnostic single metric—it tells you exactly which categories the prompt handles well and which it struggles with.

### Macro-F1

**What it measures:** The unweighted average of per-class F1 scores.

**Formula:** `mean(F1_class1, F1_class2, ..., F1_classN)`

**Interpretation:** Treats all classes equally regardless of their frequency. A macro-F1 of 0.75 means the prompt performs reasonably across all categories, even rare ones.

**Recommended as the primary optimization metric** for most classification tasks. It prevents the optimizer from sacrificing minority class performance for majority class gains.

### Weighted-F1

**What it measures:** The weighted average of per-class F1 scores, weighted by class frequency.

**When to prefer over macro-F1:** When class imbalance reflects real-world importance (i.e., you care more about getting the common classes right).

### Cohen's Kappa

**What it measures:** Agreement between the model's predictions and the gold labels, adjusted for chance agreement.

**Formula:** `(observed agreement - expected agreement) / (1 - expected agreement)`

**Interpretation:**
- < 0.20: Poor
- 0.21-0.40: Fair
- 0.41-0.60: Moderate
- 0.61-0.80: Substantial
- 0.81-1.00: Near-perfect

**When to use:** When you want to account for class distribution. Useful for comparing across datasets with different class balances. Also standard in content analysis research, so useful when reporting results in academic contexts.

## The Confusion Matrix

The single most diagnostic artifact for prompt optimization. Always compute it.

**What it shows:** For each true label (rows), how many examples were predicted as each label (columns).

**Example (3-class):**
```
                Predicted
              pos   neg   neu
Actual pos  [ 42     3     5 ]
       neg  [  2    38    10 ]
       neu  [  7     4    39 ]
```

**How to read it:**
- Diagonal = correct predictions
- Off-diagonal = errors
- Row sums = total actual examples per class
- Column sums = total predicted per class

**What to look for:**
- **Asymmetric confusion:** If the model confuses A→B much more than B→A, the definitions are biased in one direction.
- **One category absorbing others:** A column with many off-diagonal entries means that category's definition is too broad.
- **One category being missed:** A row with many off-diagonal entries means that category's definition is too narrow or overlaps with others.
- **Specific pair confusion:** Two categories with high mutual confusion need sharper boundary criteria.

## Choosing the Right Metric

| Situation | Primary metric | Also report |
|---|---|---|
| Balanced classes, standard task | Macro-F1 | Accuracy, per-class F1, confusion matrix |
| Imbalanced classes | Macro-F1 | Per-class F1, confusion matrix |
| Cost-sensitive (false positives costly) | Per-class precision | F1, confusion matrix |
| Cost-sensitive (false negatives costly) | Per-class recall | F1, confusion matrix |
| Academic content analysis | Cohen's kappa | Macro-F1, per-class F1, confusion matrix |
| Multi-label | Example-based F1 or label-based macro-F1 | Per-label precision/recall |

**Default recommendation:** Use **macro-F1** as the primary metric for optimization decisions. Always report the **confusion matrix** for diagnostics. Add **Cohen's kappa** if the work is academic.

## Creating Labeled Data

If the user does not have labeled data, guide them through creating a usable evaluation set.

### Sample size guidelines

| Number of categories | Minimum dev set | Recommended dev set | Minimum per class |
|---|---|---|---|
| 2-3 | 30 | 60-90 | 10 |
| 4-6 | 50 | 100-150 | 10 |
| 7+ | 80 | 150-200 | 8-10 |

These are minimums for prompt optimization, not for publication-quality evaluation. Larger sets give more stable metrics.

### Sampling strategy

- **Random sample** from the target corpus is the baseline approach
- **Stratified sample** if you know the approximate class distribution and want to ensure coverage
- **Purposive inclusion** of known edge cases and boundary examples alongside random samples—these are diagnostically valuable even if they overrepresent ambiguity

### Labeling process

1. The user labels all examples (they are the domain expert)
2. For ambiguous cases, the user notes the ambiguity—these cases are valuable for understanding the task's difficulty ceiling
3. If inter-coder reliability data is available from prior work, use it to set realistic performance expectations

### Splitting the data

- **Dev set (70%):** Used for iterative optimization in Phases 3-4. You will evaluate against this set multiple times.
- **Test set (30%):** Held out until Phase 5. Used exactly once for unbiased final evaluation.
- **Stratify by label:** Ensure each class appears in both splits proportionally.
- **For small datasets (< 100 total):** Use a 50/50 split to keep the test set meaningful.

## Interpreting Results During Optimization

### What counts as meaningful improvement?

- **> 3 points macro-F1:** Clear improvement, likely reflects a real prompt change.
- **1-3 points macro-F1:** Possible improvement, but could be noise with small dev sets. Check per-class metrics.
- **< 1 point macro-F1:** Not meaningful. Either the prompt change had no effect or the dev set is too small to detect the difference.

### When to stop optimizing

- Macro-F1 improvements are consistently < 2 points across iterations
- Per-class F1 scores are all within an acceptable range
- Remaining errors appear to be genuinely ambiguous cases rather than systematic prompt failures
- The prompt meets the success criteria established in Phase 0

### Dev-set vs. test-set gap

- **< 3 points difference:** Normal. The dev set was used for multiple iterations, so slight overfitting is expected.
- **3-8 points difference:** Moderate concern. The prompt may have overfit to quirks of the dev set. Consider whether the dev set is representative.
- **> 8 points difference:** Significant concern. The dev set likely does not represent the target distribution. Discuss with the user—more labeled data or a different sampling strategy may be needed.

## Performance Benchmarks

Typical performance ranges for LLM-based text classification (these are rough guides, not guarantees):

| Task type | Typical macro-F1 range | Notes |
|---|---|---|
| Binary sentiment | 0.80-0.92 | Well-studied, usually achievable |
| 3-class sentiment | 0.70-0.85 | Neutral class is the challenge |
| Topic (5-10 classes) | 0.70-0.88 | Depends on topic distinctness |
| Stance detection | 0.60-0.80 | Implicit stance is hard |
| Frame analysis | 0.55-0.75 | Frames are inherently fuzzy |
| Complex content coding | 0.50-0.75 | Depends heavily on codebook clarity |

These ranges assume a well-optimized prompt on a capable model. Starting (baseline) performance is typically 5-15 points lower.
