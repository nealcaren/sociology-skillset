# Classification Prompt Patterns

Seed prompt templates and guidance for common text classification tasks. Each pattern includes a template, common pitfalls, and label definition tips.

## General Template Structure

Every classification prompt follows this structure. Adapt the specifics to your task.

```
You are classifying [text type] into [number] categories.

## Categories

[For each category:]
**[Label]**: [One-sentence definition]. [Boundary criteria: what distinguishes this from adjacent categories]. [Exclusions: what does NOT count].

## Instructions

Read the text carefully. Assign exactly one label based on the definitions above.
[Task-specific instructions as needed.]

## Output format

Respond with a JSON object:
{"label": "[one of the valid labels]"}
```

---

## Sentiment Analysis

**Task:** Classify text by expressed sentiment or opinion valence.

**Template:**
```
You are classifying [text type] by sentiment.

## Categories

**positive**: The text expresses approval, satisfaction, enthusiasm, or favorable opinion toward the subject. Includes mild positive language ("pretty good", "not bad") unless clearly sarcastic.

**negative**: The text expresses disapproval, dissatisfaction, frustration, or unfavorable opinion toward the subject. Includes complaints, criticism, and expressions of disappointment.

**neutral**: The text is factual, descriptive, or informational without expressing a clear positive or negative opinion. Questions, requests, and purely descriptive statements are neutral unless they carry clear evaluative language.

## Instructions

Classify based on the overall sentiment of the text toward [the subject]. If the text contains mixed sentiment, classify based on the dominant tone.

Respond with JSON: {"label": "positive"} or {"label": "negative"} or {"label": "neutral"}
```

**Common pitfalls:**
- Sarcasm and irony: explicitly instruct how to handle ("classify based on the *intended* meaning, not literal words")
- Negation: "not bad" reads as mildly positive; "not great" reads as mildly negative
- Mixed sentiment: decide upfront whether to classify by dominant tone or add a "mixed" category
- Neutral overuse: neutral tends to become a catch-all; tighten its definition

**Label definition tips:**
- Define the threshold between mild sentiment and neutral explicitly
- If using a 5-point scale (very negative through very positive), provide examples of where the boundaries fall
- For domain-specific sentiment (product reviews, political text), anchor definitions to the domain

---

## Topic Classification

**Task:** Classify text by its primary subject matter.

**Template:**
```
You are classifying [text type] by topic.

## Categories

**[topic_1]**: Text primarily about [description]. Includes [subtopics]. Does NOT include [common confusion].

**[topic_2]**: Text primarily about [description]. Includes [subtopics]. Does NOT include [common confusion].

[Continue for each topic...]

## Instructions

Classify based on the primary topic of the text. If a text touches on multiple topics, classify by the one that receives the most substantive discussion.

[If applicable:] Ignore mentions of [topic] that appear only as background context or passing reference.

Respond with JSON: {"label": "[topic]"}
```

**Common pitfalls:**
- Overlapping topics: a text about "economic impact of climate policy" could be economics or environment. Define which takes priority or add specific boundary rules.
- Granularity mismatch: categories that are too broad (e.g., "politics") or too narrow (e.g., "Senate filibuster reform") cause problems. Match granularity to your analytical needs.
- Rare topics: categories with very few examples are hard to optimize. Consider merging rare topics into an "other" category.

**Label definition tips:**
- List 2-3 subtopics under each category to clarify scope
- Explicitly state what adjacent topics are NOT included
- For hierarchical topics, specify whether to classify at the top level or a specific sublevel

---

## Stance Detection

**Task:** Classify text by the author's position toward a specific target (policy, person, idea).

**Template:**
```
You are classifying [text type] by the author's stance toward [target].

## Categories

**favor**: The author explicitly or implicitly supports [target]. Includes direct endorsement, arguments in favor, positive framing, and calls to action supporting [target].

**against**: The author explicitly or implicitly opposes [target]. Includes direct criticism, arguments against, negative framing, and calls to action opposing [target].

**neutral**: The author does not express a clear position toward [target]. Includes balanced reporting, purely factual descriptions, and texts where the author's own stance is indeterminate.

## Instructions

Focus on the AUTHOR'S stance, not the topic of the text. A text that mentions [target] is not necessarily in favor of it. A text that criticizes opponents of [target] is implicitly in favor.

Look for evaluative language, framing choices, and argumentative structure—not just keywords.

Respond with JSON: {"label": "favor"} or {"label": "against"} or {"label": "neutral"}
```

**Common pitfalls:**
- Reporting vs. advocating: a journalist describing a policy debate may be neutral even while quoting strong opinions. Instruct the model to distinguish the author's voice from quoted/reported speech.
- Implicit stance: framing choices (calling a policy "reform" vs. "overhaul") signal stance without explicit opinion. Mention this in instructions.
- Irrelevant texts: texts that do not mention the target at all need handling—either filter them out in preprocessing or add an "irrelevant" category.

**Label definition tips:**
- Name the specific target in the definitions, not just "the topic"
- Distinguish between stance toward the target itself vs. stance toward related concepts
- Consider whether "neutral" means "balanced" or "not discussing stance"

---

## Frame Analysis

**Task:** Classify text by the interpretive frame or lens used to present an issue.

**Template:**
```
You are classifying [text type] by the framing used to discuss [issue].

## Frames

**[frame_1]**: The text presents [issue] primarily through the lens of [description]. Key indicators: [specific language patterns, argument types, emphasized aspects].

**[frame_2]**: The text presents [issue] primarily through the lens of [description]. Key indicators: [specific language patterns, argument types, emphasized aspects].

[Continue for each frame...]

## Instructions

Classify based on the DOMINANT frame in the text. A text may touch on multiple frames; assign the one that structures the main argument or narrative.

Framing is about HOW the issue is discussed, not WHAT position is taken. Two texts can take opposite positions while using the same frame (e.g., both sides arguing about economic costs).

Respond with JSON: {"label": "[frame]"}
```

**Common pitfalls:**
- Frame vs. topic: framing is about interpretive lens, not subject matter. A text about healthcare can use an economic frame, a moral frame, or a legal frame. Ensure label definitions focus on the lens, not the topic.
- Multiple frames: most texts contain multiple frames. The "dominant frame" instruction helps, but consider whether your analysis needs multi-label annotation instead.
- Abstract definitions: frames are inherently abstract. Ground each definition in concrete indicators (word choices, argument structures, emphasized consequences).

**Label definition tips:**
- Provide 3-5 specific linguistic or rhetorical indicators for each frame
- Include a sentence about what each frame emphasizes and what it de-emphasizes
- If frames come from a published typology, reference it but translate academic language into clear instructions

---

## Content Coding (General)

**Task:** Apply a custom coding scheme to text data. This covers tasks like identifying rhetorical strategies, communication styles, information types, etc.

**Template:**
```
You are coding [text type] according to the following scheme.

## Code definitions

**[code_1]**: [Clear definition]. Assign this code when the text [specific observable criteria]. Do NOT assign when [common false positive].

**[code_2]**: [Clear definition]. Assign this code when the text [specific observable criteria]. Do NOT assign when [common false positive].

[Continue for each code...]

## Instructions

[Specify whether codes are mutually exclusive or whether multiple can apply.]

[Any ordering or priority rules for ambiguous cases.]

[Specify what to do with texts that do not fit any code: assign "other" / "none" / flag for review.]

Respond with JSON: {"label": "[code]"}
```

**Common pitfalls:**
- Coder-dependent definitions: if the coding scheme relies on subjective judgment that varies across human coders, the LLM will also struggle. Tighten definitions before optimizing.
- Implicit knowledge: coding schemes developed for trained human coders may assume domain knowledge. Make all criteria explicit in the prompt.
- "Other" category: if many texts do not fit defined codes, "other" becomes dominant and uninformative. Either refine codes or filter input data.

---

## Multi-Label Classification

**Task:** Assign one or more labels from a set (not mutually exclusive).

**Template:**
```
You are classifying [text type]. A text may have multiple applicable labels.

## Labels

**[label_1]**: [Definition]. Apply when [criteria].
**[label_2]**: [Definition]. Apply when [criteria].
[Continue...]

## Instructions

Apply ALL labels that are relevant to the text. Most texts will have 1-3 labels. It is acceptable to apply only one label if only one fits.

[Specify threshold: apply a label if the text "clearly" discusses it? Or if it "mentions" it?]

Respond with JSON: {"labels": ["label_1", "label_2"]}
```

**Common pitfalls:**
- Threshold ambiguity: "relevant" is vague. Specify how much discussion of a topic warrants a label (primary focus? any mention? substantive discussion?).
- Label correlation: some labels frequently co-occur. This is not a problem unless the correlation is an artifact of ambiguous definitions.
- Evaluation complexity: multi-label F1 differs from multi-class F1. Use example-based or label-based F1 as appropriate.

---

## Multi-Dimensional Classification

**Task:** Apply multiple independent classification dimensions to the same texts (e.g., emotion + directionality + rhetorical style).

This is different from multi-label classification (multiple labels from one set). Here, each dimension has its own label set, and every text gets one label per dimension.

### Separate Prompts vs. Single Prompt

**Default: use separate prompts.** One prompt per dimension, each optimized independently.

**Why separate is better:**
- Each prompt can be optimized, tested, and diagnosed independently
- A stall on one dimension does not block the others
- Focused re-immersion targets one dimension's confused pair without touching the rest
- Simpler prompts perform more reliably

**When a single combined prompt might work:**
- All dimensions are straightforward (high baseline accuracy)
- Dimensions are conceptually linked and benefit from joint reasoning
- Cost constraints require minimizing API calls

**Combined prompt template (use sparingly):**
```
You are classifying [text type] on multiple dimensions.

## Dimension 1: [Name]
[Label definitions...]

## Dimension 2: [Name]
[Label definitions...]

## Instructions
Classify the text on each dimension independently.

Respond with JSON:
{"dimension_1": "[label]", "dimension_2": "[label]"}
```

**Pitfalls of combined prompts:**
- Dimensions can interfere: the model may let its judgment on one dimension influence another
- Harder to diagnose errors — did the model confuse the labels, or did one dimension's reasoning bleed into another?
- Optimization requires changing one dimension's definitions while holding the others constant, which is fiddly in a single prompt

### Optimization Workflow for Multiple Dimensions

1. **Phase 0:** Define all dimensions together. Note potential interactions.
2. **Phase 1:** Immersion covers all dimensions at once (same texts). Build one seed prompt per dimension.
3. **Phase 2:** Same dev/test split for all dimensions. Run baselines independently.
4. **Phase 3:** Optimize each dimension on its own track. Some will converge faster.
5. **Focused re-immersion:** Triggered per-dimension, per-confused-pair. Does not affect other dimensions.
6. **Phase 5-6:** Dimensions can finish at different times. Package code runs all prompts per text.

### Handling Dimension Interactions

Sometimes dimensions correlate in the data (e.g., "anger" emotion frequently co-occurs with "outward" directionality). This is fine — it reflects the data, not a prompt problem.

Watch for cases where the correlation leads the model astray: if it always predicts "outward" when it detects "anger," even for inward-directed anger texts, the directionality prompt may need an explicit instruction: "Classify directionality based on the target of the expression, regardless of the emotion present."

---

## Chain-of-Thought Variant

For any of the above tasks, you can add explicit reasoning. Use this when:
- The classification requires multi-step inference
- Errors in direct classification stem from the model skipping reasoning steps
- You need the reasoning trace for diagnostic purposes

**Addition to any template:**
```
## Instructions

Before classifying, briefly reason about the text:
1. What is the text about?
2. What [relevant features] does it exhibit?
3. Based on these observations, which category best fits?

Respond with JSON:
{"reasoning": "[your brief reasoning]", "label": "[label]"}
```

**Note:** Chain-of-thought increases token usage per classification. For batch processing at scale, confirm this cost is acceptable. Consider using CoT during optimization for diagnosis, then switching to direct classification for deployment if performance holds.

---

## Diagnostic Strategy Guide

When classification performance stalls, use this table to match the symptom to the right prompt strategy:

| Symptom | Strategy | How |
|---|---|---|
| Model jumps to conclusions, misses nuance | Chain-of-thought | Add reasoning field before label; decompose into sub-questions |
| Two specific categories keep bleeding into each other | Contrastive definitions | Add "DO NOT include" exclusions and explicit boundary criteria to the confused pair |
| Model misses subtext, irony, or implicit signals | Annotated few-shot | Provide 2-3 examples with reasoning explaining *why* the label fits |
| Concept is too abstract or multi-faceted | Decomposition | Break into 2-3 concrete sub-questions, then assign label based on answers |
| Model misinterprets domain-specific language | Persona framing | Add "You are a [domain expert]..." to prime domain-appropriate interpretation |
| Many borderline cases with no clear correct label | Confidence triage | Add confidence field; route low-confidence cases to human review |
| Model commits to a label too quickly, misses counter-evidence | Label-then-verify | Ask for preliminary label, one reason it might be wrong, then final label |

---

## Tips for All Classification Types

1. **Use the exact label strings** in the output format specification. If labels contain spaces or special characters, use simple snake_case alternatives.
2. **Order categories consistently.** List them in the same order in definitions and output format. For ordinal categories, list them in order.
3. **Name the task explicitly.** "You are classifying tweets by sentiment" is better than "Read the following text and respond."
4. **Be specific about edge cases upfront.** Every classification task has ambiguous cases. Address them in the definitions rather than discovering them during evaluation.
5. **Keep the prompt scannable.** Use headers, bold labels, and short paragraphs. The model processes structured prompts more reliably than dense prose.
6. **Use reasoning traces for diagnosis, not production.** Brief justifications (1-2 sentences) are valuable during optimization for understanding *why* the model chose a label. But consider removing the reasoning field for deployment if the label-only prompt performs equivalently — it saves tokens at scale.
