# Code Templates for Batch Classification

Production-ready templates for batch processing with optimized prompts. Includes Python (Anthropic SDK) and R (httr2) implementations.

**Note on model names and pricing:** The model names and prices below are examples current as of the skill's creation date. Model availability, naming conventions, and pricing change frequently. Always confirm the current model name and pricing at runtime. Treat model names in these templates as parameters to be updated, not constants.

## Python: Anthropic API

### Basic batch classification

```python
import anthropic
import json
import time
import pandas as pd

client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY env var

SYSTEM_PROMPT = """[Your optimized system prompt here]"""

MODEL = "claude-sonnet-4-5-20250929"
VALID_LABELS = ["label_a", "label_b", "label_c"]  # update with your labels


def classify_text(text, max_retries=3):
    """Classify a single text using the optimized prompt."""
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=150,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": text}],
            )
            response_text = response.content[0].text
            result = json.loads(response_text)
            label = result.get("label")
            if label in VALID_LABELS:
                return {
                    "label": label,
                    "raw_response": response_text,
                    "input_tokens": response.usage.input_tokens,
                    "output_tokens": response.usage.output_tokens,
                }
            else:
                return {
                    "label": None,
                    "raw_response": response_text,
                    "error": f"Invalid label: {label}",
                }
        except json.JSONDecodeError:
            if attempt < max_retries - 1:
                continue
            return {
                "label": None,
                "raw_response": response_text,
                "error": "JSON parse failure",
            }
        except anthropic.RateLimitError:
            wait_time = 2 ** (attempt + 1)
            print(f"Rate limited. Waiting {wait_time}s...")
            time.sleep(wait_time)
        except anthropic.APIError as e:
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return {"label": None, "raw_response": None, "error": str(e)}
    return {"label": None, "raw_response": None, "error": "Max retries exceeded"}


def classify_batch(df, text_column, delay=0.5):
    """Classify all texts in a dataframe.

    Args:
        df: pandas DataFrame with text data
        text_column: name of the column containing text to classify
        delay: seconds between API calls (for rate limiting)

    Returns:
        DataFrame with added 'predicted_label' and 'raw_response' columns
    """
    results = []
    total = len(df)

    for i, text in enumerate(df[text_column]):
        if pd.isna(text) or str(text).strip() == "":
            results.append({"label": None, "error": "Empty text"})
            continue

        result = classify_text(str(text))
        results.append(result)

        if (i + 1) % 10 == 0 or (i + 1) == total:
            done = sum(1 for r in results if r.get("label") is not None)
            failed = sum(1 for r in results if r.get("error"))
            print(f"Progress: {i + 1}/{total} | Success: {done} | Failed: {failed}")

        time.sleep(delay)

    df["predicted_label"] = [r.get("label") for r in results]
    df["raw_response"] = [r.get("raw_response") for r in results]
    df["error"] = [r.get("error") for r in results]

    return df


# Usage
df = pd.read_csv("your_data.csv")
df = classify_batch(df, text_column="text", delay=0.5)
df.to_csv("classified_output.csv", index=False)

# Summary
print(f"\nResults:")
print(f"  Classified: {df['predicted_label'].notna().sum()}/{len(df)}")
print(f"  Parse failures: {df['error'].notna().sum()}")
print(f"\nLabel distribution:")
print(df["predicted_label"].value_counts())
```

### Cost estimation

```python
def estimate_cost(df, text_column, model="claude-sonnet-4-5-20250929"):
    """Estimate API cost for batch classification."""
    # Rough token estimates (1 token ≈ 4 characters for English)
    avg_text_len = df[text_column].str.len().mean()
    avg_input_tokens = avg_text_len / 4 + 200  # text + system prompt overhead
    avg_output_tokens = 30  # JSON response

    n = len(df)

    # Pricing per million tokens (check current pricing)
    pricing = {
        "claude-sonnet-4-5-20250929": {"input": 3.00, "output": 15.00},
        "claude-haiku-4-5-20251001": {"input": 0.80, "output": 4.00},
    }

    if model not in pricing:
        print(f"Unknown model: {model}. Using Sonnet pricing as estimate.")
        model = "claude-sonnet-4-5-20250929"

    input_cost = (n * avg_input_tokens / 1_000_000) * pricing[model]["input"]
    output_cost = (n * avg_output_tokens / 1_000_000) * pricing[model]["output"]
    total = input_cost + output_cost

    print(f"Estimated cost for {n} classifications with {model}:")
    print(f"  Avg input tokens: ~{int(avg_input_tokens)}")
    print(f"  Avg output tokens: ~{int(avg_output_tokens)}")
    print(f"  Input cost:  ${input_cost:.2f}")
    print(f"  Output cost: ${output_cost:.2f}")
    print(f"  Total:       ${total:.2f}")

    return total
```

### Evaluation helper

```python
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    cohen_kappa_score,
)


def evaluate(df, true_col, pred_col, labels=None):
    """Evaluate classification performance."""
    mask = df[pred_col].notna()
    y_true = df.loc[mask, true_col]
    y_pred = df.loc[mask, pred_col]

    if labels is None:
        labels = sorted(y_true.unique())

    print("Classification Report:")
    print(classification_report(y_true, y_pred, labels=labels, digits=3))

    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    cm_df = pd.DataFrame(cm, index=labels, columns=labels)
    print(cm_df)

    kappa = cohen_kappa_score(y_true, y_pred)
    print(f"\nCohen's Kappa: {kappa:.3f}")

    if (~mask).sum() > 0:
        print(f"\nNote: {(~mask).sum()} examples excluded (parse failures)")
```

---

## R: httr2

### Basic batch classification

```r
library(httr2)
library(jsonlite)
library(dplyr)
library(purrr)

SYSTEM_PROMPT <- "[Your optimized system prompt here]"
MODEL <- "claude-sonnet-4-5-20250929"
VALID_LABELS <- c("label_a", "label_b", "label_c")  # update with your labels

classify_text <- function(text, max_retries = 3) {
  for (attempt in seq_len(max_retries)) {
    tryCatch({
      resp <- request("https://api.anthropic.com/v1/messages") |>
        req_headers(
          `x-api-key` = Sys.getenv("ANTHROPIC_API_KEY"),
          `anthropic-version` = "2023-06-01",
          `content-type` = "application/json"
        ) |>
        req_body_json(list(
          model = MODEL,
          max_tokens = 150,
          system = SYSTEM_PROMPT,
          messages = list(list(role = "user", content = text))
        )) |>
        req_retry(max_tries = 3, backoff = ~ 2) |>
        req_perform()

      body <- resp_body_json(resp)
      response_text <- body$content[[1]]$text
      result <- fromJSON(response_text)

      if (!is.null(result$label) && result$label %in% VALID_LABELS) {
        return(tibble(
          label = result$label,
          raw_response = response_text,
          error = NA_character_
        ))
      } else {
        return(tibble(
          label = NA_character_,
          raw_response = response_text,
          error = paste0("Invalid label: ", result$label)
        ))
      }
    }, error = function(e) {
      if (attempt == max_retries) {
        return(tibble(
          label = NA_character_,
          raw_response = NA_character_,
          error = conditionMessage(e)
        ))
      }
      Sys.sleep(2^attempt)
    })
  }
}

classify_batch <- function(df, text_column, delay = 0.5) {
  n <- nrow(df)
  results <- vector("list", n)

  for (i in seq_len(n)) {
    text <- df[[text_column]][i]

    if (is.na(text) || trimws(text) == "") {
      results[[i]] <- tibble(
        label = NA_character_,
        raw_response = NA_character_,
        error = "Empty text"
      )
      next
    }

    results[[i]] <- classify_text(text)

    if (i %% 10 == 0 || i == n) {
      done <- sum(map_lgl(results[seq_len(i)], ~ !is.na(.x$label)))
      message(sprintf("Progress: %d/%d | Success: %d", i, n, done))
    }

    Sys.sleep(delay)
  }

  results_df <- bind_rows(results)
  bind_cols(df, results_df)
}

# Usage
df <- read.csv("your_data.csv")
df <- classify_batch(df, text_column = "text", delay = 0.5)
write.csv(df, "classified_output.csv", row.names = FALSE)

# Summary
message(sprintf(
  "\nResults:\n  Classified: %d/%d\n  Parse failures: %d",
  sum(!is.na(df$label)), nrow(df), sum(!is.na(df$error))
))
table(df$label)
```

### Cost estimation (R)

```r
estimate_cost <- function(df, text_column, model = "claude-sonnet-4-5-20250929") {
  avg_text_len <- mean(nchar(df[[text_column]]), na.rm = TRUE)
  avg_input_tokens <- avg_text_len / 4 + 200
  avg_output_tokens <- 30
  n <- nrow(df)

  pricing <- list(
    "claude-sonnet-4-5-20250929" = list(input = 3.00, output = 15.00),
    "claude-haiku-4-5-20251001" = list(input = 0.80, output = 4.00)
  )

  p <- pricing[[model]]
  if (is.null(p)) {
    message("Unknown model. Using Sonnet pricing.")
    p <- pricing[["claude-sonnet-4-5-20250929"]]
  }

  input_cost <- (n * avg_input_tokens / 1e6) * p$input
  output_cost <- (n * avg_output_tokens / 1e6) * p$output
  total <- input_cost + output_cost

  message(sprintf("Estimated cost for %d classifications with %s:", n, model))
  message(sprintf("  Input cost:  $%.2f", input_cost))
  message(sprintf("  Output cost: $%.2f", output_cost))
  message(sprintf("  Total:       $%.2f", total))

  invisible(total)
}
```

### Evaluation helper (R)

```r
library(caret)

evaluate <- function(df, true_col, pred_col) {
  mask <- !is.na(df[[pred_col]])
  y_true <- factor(df[[true_col]][mask])
  y_pred <- factor(df[[pred_col]][mask], levels = levels(y_true))

  cm <- confusionMatrix(y_pred, y_true)
  print(cm)

  if (sum(!mask) > 0) {
    message(sprintf("\nNote: %d examples excluded (parse failures)", sum(!mask)))
  }
}
```

---

## Tips for Batch Processing

1. **Start small.** Run 10-20 examples first to verify the prompt and parsing work correctly before processing thousands.

2. **Save raw responses.** Always store the full API response alongside the parsed label. This enables reprocessing without re-calling the API.

3. **Handle rate limits gracefully.** The `delay` parameter spaces out requests. Increase it if you hit rate limits. For large batches, consider Anthropic's Message Batches API.

4. **Monitor parse failures.** If more than 2-3% of responses fail to parse, revisit the output format instructions in your prompt.

5. **Resume interrupted runs.** For large batches, save results incrementally. Check which rows already have results before restarting.

6. **Cost awareness.** Run `estimate_cost()` before large batches. Haiku is 4-5x cheaper than Sonnet—consider it for simpler classification tasks where the performance difference is small.
