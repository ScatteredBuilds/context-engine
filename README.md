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

```text
Retrieved chunks
================
Source: attention_heads.md | score: 0.642
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

## Current limitations

- It retrieves context, but does not generate a final natural-language answer yet.
- The confidence threshold is simple and will need calibration.
- Embeddings are recomputed on every run.
- There is no eval set yet.
- Markdown parsing is basic text loading.

Early buildout.
