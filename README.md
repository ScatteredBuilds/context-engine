# context-engine

A local context and retrieval engine for grounding model answers in personal notes.

This project starts as a local RAG system over Obsidian notes using Python and local models.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The first run will download the sentence-transformers embedding model.

## Usage

```bash
python ask.py "What do my notes say about attention heads?"
```

Optional settings:

```bash
python ask.py "What do my notes say about attention heads?" --top-k 2 --chunk-size 80 --overlap 15
```

## Example output

The example output below shows the expected output shape. It is not a benchmark.

```text
Retrieved chunks
================
Source: attention_heads.md | score: <score from local embedding model>
Attention heads let a transformer compare each token with other tokens in the context window...

Sources
=======
- attention_heads.md
```

If the retrieved context is weak, the command refuses to answer:

```text
I do not have enough grounded context in the notes to answer that.
```

## Current structure

context-engine/
  src/
  notes_sample/
  evals/
  outputs/
  docs/

## What it does now

- recursively loads markdown notes
- skips hidden files
- chunks notes with configurable overlap
- embeds chunks with sentence-transformers
- retrieves chunks with cosine similarity
- prints source filenames
- refuses when the top score is below a threshold

## Verification status

- `python3 -m py_compile ask.py src/load.py src/chunk.py src/retrieve.py src/ask.py` passes locally.
- Loader and chunker smoke tests pass against `notes_sample/attention_heads.md`.
- Retrieval verification was run locally with `.venv/bin/python evals/run_basic_queries.py` and passed 3/3 checks.
- CLI retrieval was run locally with `.venv/bin/python ask.py "What do my notes say about attention heads?"`.
- `evals/basic_queries.json` contains a small set of manual retrieval checks. These are not benchmark results.
- `outputs/example_run.md` records verified local runtime output.

## Retrieval verification

Run the basic retrieval checks with:

```bash
python evals/run_basic_queries.py
```

The script loads `evals/basic_queries.json`, runs each query through the existing retrieval pipeline, and prints the query, top source, score, and pass/fail result. A case passes when one of its expected sources appears in the retrieved top-k results above the confidence threshold.

The script does not call an LLM and does not measure answer quality.

## Known dependency requirement

The retrieval path requires `sentence-transformers`.

Install dependencies before running the CLI:

```bash
pip install -r requirements.txt
```

The first successful run will also download the configured embedding model.

## Current limitations

- It retrieves context, but does not generate a final natural-language answer yet.
- The confidence threshold is simple and will need calibration.
- Embeddings are recomputed on every run.
- The eval file is a small manual check set, not an automated benchmark.
- Markdown parsing is basic text loading.

## Next milestone

Calibrate the retrieval threshold with more sample notes and document failure cases from real runs.

Early buildout.
