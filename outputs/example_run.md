# Example Run

Status: verified locally with `.venv/bin/python`.

The bare `python` command was not available in this shell, so the verified runs used the project virtual environment directly.

## Basic retrieval checks

Command:

```bash
.venv/bin/python evals/run_basic_queries.py
```

Output:

```text
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|██████████| 103/103 [00:00<00:00, 18839.71it/s]
Query: What do my notes say about attention heads?
Top source: attention_heads.md
Score: 0.617
Result: PASS

Loading weights: 100%|██████████| 103/103 [00:00<00:00, 16810.51it/s]
Query: What do my notes say about transformer interpretability?
Top source: attention_heads.md
Score: 0.387
Result: PASS

Loading weights: 100%|██████████| 103/103 [00:00<00:00, 12653.43it/s]
Query: What do my notes say about database indexing?
Top source: <none above threshold>
Score: n/a
Result: PASS

Passed 3/3 retrieval checks
```

## CLI retrieval

Command:

```bash
.venv/bin/python ask.py "What do my notes say about attention heads?"
```

Output:

```text
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|██████████| 103/103 [00:00<00:00, 25357.36it/s]
Retrieved chunks
================
Source: attention_heads.md | score: 0.617
# Attention Heads Attention heads let a transformer compare each token with other tokens in the context window. Different heads can learn different patterns. One head might connect pronouns to earlier nouns, while another might track punctuation or repeated terms. For interpretability work, attention heads are useful because their attention patterns can sometimes be inspected directly. The pattern is not a full explanation of the model's behavior, but it can give clues about which tokens influenced a layer's computation.

Sources
=======
- attention_heads.md
```

This project currently retrieves note chunks. It does not generate a final natural-language answer.
