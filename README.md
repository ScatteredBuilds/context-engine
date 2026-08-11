# context-engine

A small local semantic-retrieval pipeline for Markdown notes. It isolates the retrieval stage of a retrieval-augmented generation system so loading, chunking, ranking, source attribution, and refusal behavior can be inspected without an answer-generating model.

## Status

Learning project / working prototype. The CLI retrieves relevant note chunks; it does not generate a natural-language answer.

## Problem

Before generated answers can be evaluated for grounding, the retrieval layer must reliably find relevant source material and decline unrelated queries. This project tests that narrower problem against a deliberately small sample corpus.

## Implemented

- Recursive Markdown loading with hidden-file exclusion
- Configurable word-based chunks and overlap
- `sentence-transformers/all-MiniLM-L6-v2` embeddings
- Cosine-similarity ranking and configurable top-k retrieval
- Source filenames in CLI output
- Refusal when the top score is below a fixed threshold
- JSON-defined retrieval checks with pass/fail output

## Architecture

```text
Markdown files -> loader -> word chunks -> embeddings
                                         |
query ----------> embedding -------------+-> cosine ranking -> top-k results
                                                               |
                                      threshold ----------------+-> sources or refusal
```

`ask.py` is a thin entry point to `src.ask`. The implementation is split across `src/load.py`, `src/chunk.py`, `src/retrieve.py`, and `src/ask.py`.

## Setup and usage

Python 3.10 or newer is required.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python ask.py "What do my notes say about attention heads?"
```

The first retrieval run downloads the configured embedding model. Use your own notes directory or adjust retrieval settings:

```bash
python ask.py "your question" --notes-dir path/to/notes --top-k 2 --threshold 0.35
```

## Evaluation and testing

```bash
python evals/run_basic_queries.py
python evals/run_basic_queries.py --eval-file evals/expanded_queries.json
```

A case passes when an expected source appears among results at or above the threshold. For negative cases, it passes when no result clears the threshold. These checks evaluate retrieval behavior only—not answer quality, relevance judgments at scale, or production readiness.

Committed run records show 3/3 basic checks and 19/20 expanded checks. The expanded set preserves one failure for the ambiguous query `What does the note say about terms?`; see [evals/README.md](evals/README.md) and [outputs/expanded_eval_run.md](outputs/expanded_eval_run.md).

For dependency-free verification of the loader and chunker:

```bash
python -m py_compile ask.py src/load.py src/chunk.py src/retrieve.py src/ask.py evals/run_basic_queries.py
```

## Limitations

- The committed corpus contains one sample note, so the reported counts are smoke-test evidence, not benchmark results.
- The fixed `0.35` threshold is not calibrated for a larger or different corpus.
- Embeddings are recomputed on every command and model loading dominates small runs.
- Chunking is whitespace-based and does not preserve Markdown structure.
- The system returns excerpts rather than generating an answer.
- Model download and retrieval require network access on the first run.

Known failure modes are documented in [docs/failure_modes.md](docs/failure_modes.md).
