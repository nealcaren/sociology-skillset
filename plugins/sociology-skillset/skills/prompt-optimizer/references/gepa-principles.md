# GEPA Principles for Prompt Optimization

This reference distills the key insights from the GEPA (Generalized Evolutionary Prompt Architect) approach to prompt optimization (Agrawal et al. 2025, "Reflective Prompt Evolution Can Outperform Reinforcement Learning"). These principles guide the optimization phases in this skill.

## The Core Idea

GEPA treats prompt optimization as an evolutionary process: generate candidate prompts, evaluate them on real examples, reflect on what went wrong, and produce improved variants. The critical innovation is *reflective mutation*—using error analysis and reasoning to guide prompt changes, rather than random or gradient-based modifications.

Key finding: A single round of reflective optimization typically produces the largest performance gain. Subsequent rounds help, but with diminishing returns. This means the diagnostic quality of each iteration matters more than the number of iterations.

## Principle 1: Reflective Mutation

**What it means:** When a prompt fails on examples, examine *why* it failed before changing anything. The error pattern determines the fix.

**How it works in practice:**
1. Run the prompt on labeled examples
2. Collect misclassifications along with the model's reasoning
3. Group errors by pattern (label confusion, missing coverage, boundary ambiguity)
4. Diagnose the root cause for each pattern
5. Propose a targeted prompt edit that addresses the diagnosed cause

**Why it matters:** Random prompt modifications (swapping synonyms, reordering instructions) are inefficient. Targeted fixes based on error diagnosis converge faster and are less likely to introduce regressions.

**Anti-pattern to avoid:** Rewriting the entire prompt after seeing errors. This discards what was already working. Change only what the diagnosis indicates.

## Principle 2: Execution Traces as Signal

**What it means:** The model's intermediate reasoning (chain-of-thought, scratchpad, reasoning traces) contains diagnostic information beyond just the final answer.

**How to use it:**
- If the reasoning is correct but the final label is wrong → the label-mapping instructions are unclear
- If the reasoning is wrong from the start → the task framing or definitions need work
- If the reasoning is partially correct but goes off track → a specific instruction is misleading or missing

**Practical implication:** When using chain-of-thought prompts, always examine the reasoning for misclassified examples. Even with direct-classification prompts, you can temporarily add a reasoning field to diagnose stubborn errors, then remove it for production.

## Principle 3: Evaluation Traces as Signal

**What it means:** Per-class metrics (not just overall accuracy) reveal which categories the prompt handles well and which it struggles with.

**How to use it:**
- A category with low recall is being missed → its definition may be too narrow
- A category with low precision is capturing too much → its definition is too broad or overlaps with others
- Two categories with high mutual confusion → their boundary criteria need sharpening
- One category with near-perfect scores → its definition is working; do not change it when editing others

**Practical implication:** Always compute per-class precision, recall, and F1. The confusion matrix is the single most informative diagnostic artifact.

## Principle 4: Diversity and Pareto Selection

**What it means:** Maintaining a diverse set of prompt candidates avoids getting stuck in local optima. Different prompt strategies may excel on different subsets of examples.

**The hill-climbing trap:** If you only ever modify a single prompt, each change tries to improve on the last version. This is hill-climbing—effective locally but easily trapped. A prompt optimized for one error pattern may create blind spots for others.

**Pareto selection:** Rather than picking the single "best" prompt, identify candidates that are non-dominated—each one excels on some metric or subset. These represent different trade-offs worth exploring.

**How to apply it:**
1. After initial optimization (Phase 3), generate 2-3 structurally different prompt strategies
2. Evaluate all candidates on the same dev set
3. Look for complementary strengths: does Strategy A handle Category X well while Strategy B handles Category Y?
4. Use these insights to inform the merge in Phase 5

**Practical simplification:** In interactive optimization (vs. automated runs), 2-3 diverse candidates are sufficient. The goal is not exhaustive search but avoiding tunnel vision.

## Principle 5: System-Aware Merge

**What it means:** Combining the best elements of multiple prompt candidates into a single prompt, informed by where each one excels.

**How to merge:**
- Identify the best-performing version of each prompt component (task framing, label definitions, output format, etc.)
- Combine them, checking for consistency
- Test the merged prompt to confirm it captures the strengths of its sources
- If the merge underperforms individual candidates, the components may be interacting; try different combinations

**What NOT to do:** Do not simply concatenate prompts or average their language. A merge is surgical: selecting the most effective version of each component.

## Principle 6: Instructions Beat Few-Shot Examples

**Empirical finding:** GEPA consistently found that well-crafted instructions outperform few-shot demonstrations across classification tasks.

**Why:**
- Few-shot examples consume tokens that could be used for better instructions
- Examples can mislead: the model may overfit to surface features of the examples rather than learning the intended rule
- Instructions generalize better to edge cases not covered by examples
- At scale, shorter prompts (instructions without examples) reduce cost significantly

**When examples still help:**
- The task involves a format that is hard to describe but easy to show
- The classification depends on stylistic or tonal qualities that benefit from demonstration
- You have exhausted instruction-based approaches and need additional signal

**Default recommendation:** Start with zero-shot instructions. Add examples only if instruction-based optimization plateaus and error analysis suggests the model needs demonstrations.

## Principle 7: Brevity and Focus

**Empirical finding:** Shorter prompts frequently outperform longer ones, all else being equal.

**Why:**
- Long prompts dilute the model's attention across many instructions
- Redundant instructions can create conflicting signals
- Concise language forces clearer thinking about what actually matters

**How to apply it:**
- After each optimization iteration, review the prompt for unnecessary words
- If a sentence does not change classification behavior, remove it
- Test compressed versions—you may find performance holds or improves
- Aim for the minimum prompt that captures all necessary distinctions

## Principle 8: First Iteration Matters Most

**Empirical finding:** The largest performance gain typically comes from the first reflective optimization iteration. Going from a naive prompt to a diagnosed-and-fixed prompt yields the biggest jump.

**Implications:**
- Invest heavily in the quality of the first error analysis (Phase 3, Iteration 1)
- Do not rush through diagnosis to get to iteration 2
- If the first iteration does not produce meaningful improvement, the problem may be in the evaluation setup (wrong metric, unrepresentative dev set, ambiguous labels) rather than the prompt

## Key Empirical Findings from GEPA

- Reflective prompt optimization outperformed RL-based methods (RLHF, PPO-based prompt tuning) on standard classification benchmarks
- The approach works across model sizes and families
- Gains are largest on tasks with well-defined categories and sufficient labeled data
- Tasks with inherently ambiguous categories (where human annotators disagree) show smaller gains—this is a floor set by the task, not by the method
- Automated reflective evolution (GEPA's full algorithm) and interactive human-guided optimization (this skill's approach) follow the same logic; the interactive version benefits from domain expertise at the diagnosis step
