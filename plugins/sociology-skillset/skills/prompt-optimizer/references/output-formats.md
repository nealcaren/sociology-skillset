# Output Format Patterns

Structured output formats for classification prompts. Consistent, parseable output is essential for batch processing.

## Default: Single Label JSON

Use this for most classification tasks.

**Prompt instruction:**
```
Respond with a JSON object containing your classification:
{"label": "[one of: label_a, label_b, label_c]"}
```

**Parsing:** Extract the `label` field from parsed JSON.

**Why JSON over plain text:** JSON parsing is unambiguous. Plain text responses ("I would classify this as positive") require fragile string matching and are prone to variation.

## Label with Reasoning (Chain-of-Thought)

Use when you need diagnostic reasoning traces or the task requires explicit multi-step inference.

**Prompt instruction:**
```
First, briefly explain your reasoning (1-2 sentences). Then provide your classification.

Respond with a JSON object:
{"reasoning": "[your brief reasoning]", "label": "[one of: label_a, label_b, label_c]"}
```

**Parsing:** Extract `label` for the classification. Use `reasoning` for error diagnosis in Phase 3.

**Token cost note:** The reasoning field adds 20-60 tokens per classification. At scale, this adds up. Consider using reasoning during optimization and removing it for production if the label-only prompt performs equivalently.

## Label with Confidence

Use when you want to identify uncertain classifications for human review.

**Prompt instruction:**
```
Respond with a JSON object:
{"label": "[one of: label_a, label_b, label_c]", "confidence": "[high, medium, or low]"}
```

**Parsing:** Extract `label` for classification. Filter `low` confidence cases for manual review.

**Note:** LLM confidence self-reports are not calibrated probabilities. They are useful as a rough filter (high vs. low confidence) but should not be treated as precise uncertainty estimates.

## Multi-Label Output

Use when texts can belong to multiple categories simultaneously.

**Prompt instruction:**
```
Assign all applicable labels. Most texts will have 1-3 labels.

Respond with a JSON object:
{"labels": ["label_a", "label_b"]}
```

**Parsing:** Extract the `labels` array. Handle the case where only one label applies (array with one element).

## Multi-Field Coding

Use when the classification task involves multiple dimensions (e.g., sentiment AND topic, or stance AND certainty).

**Prompt instruction:**
```
Classify the text on two dimensions:

Respond with a JSON object:
{"topic": "[one of: economy, health, education]", "sentiment": "[one of: positive, negative, neutral]"}
```

**Parsing:** Extract each field separately. This is more reliable than asking for a combined label like "economy_positive."

## Output Format Specification Tips

### Be explicit about valid values
List the exact valid label strings in the output format instruction. This reduces the chance of the model inventing variations.

```
Good:  {"label": "[one of: support, oppose, neutral]"}
Bad:   {"label": "[your classification]"}
```

### Match label strings to your data pipeline
Use simple, lowercase, underscore-separated strings. Avoid spaces, special characters, or mixed case in label values.

```
Good:  "strongly_agree", "somewhat_agree", "neutral"
Bad:   "Strongly Agree", "Somewhat agree", "NEUTRAL"
```

### Specify JSON explicitly
Do not rely on the model inferring the format. State "Respond with a JSON object" and show the exact structure.

### Handle the "no applicable label" case
If some texts may not fit any category, include an explicit option:

```
{"label": "[one of: label_a, label_b, label_c, none]"}
```

This is better than letting the model improvise ("I cannot classify this text" as free text).

## Parsing Strategies

### Primary: JSON parsing

```python
import json
result = json.loads(response_text)
label = result["label"]
```

### Fallback: Extract JSON from surrounding text

Models sometimes wrap JSON in explanation text or markdown code fences. Handle this:

```python
import json
import re

def extract_label(response_text, valid_labels):
    """Extract classification label from model response."""
    # Try direct JSON parse
    try:
        result = json.loads(response_text.strip())
        if result.get("label") in valid_labels:
            return result["label"]
    except json.JSONDecodeError:
        pass

    # Try extracting JSON from markdown code fence
    json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response_text, re.DOTALL)
    if json_match:
        try:
            result = json.loads(json_match.group(1))
            if result.get("label") in valid_labels:
                return result["label"]
        except json.JSONDecodeError:
            pass

    # Try finding JSON object anywhere in text
    json_match = re.search(r'\{[^{}]*\}', response_text)
    if json_match:
        try:
            result = json.loads(json_match.group(0))
            if result.get("label") in valid_labels:
                return result["label"]
        except json.JSONDecodeError:
            pass

    # Last resort: look for valid label as standalone word
    for label in valid_labels:
        if re.search(r'\b' + re.escape(label) + r'\b', response_text.lower()):
            return label

    return None  # Unparseable
```

### Tracking parse failures

Always track the parse failure rate. If more than 2-3% of responses fail to parse, tighten the output format instructions in the prompt. Common fixes:
- Add "Respond ONLY with the JSON object, no other text"
- Add "Do not include markdown formatting or code fences"
- Simplify the JSON structure
