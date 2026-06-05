# Context Engine Evaluation Report

## Purpose

The purpose of this evaluation is to determine whether expected source material appears in top-k retrieval results.

The evaluation checks retrieval behavior directly. It does not evaluate answer generation, because the current CLI retrieves note chunks and source filenames but does not synthesize a final natural-language answer.

## Evaluation Method

Source corpus:

- The default evaluation corpus is `notes_sample/`.
- The repository contains one sample note used by the current evaluation: `notes_sample/attention_heads.md`.
- Markdown notes are loaded recursively.
- Hidden files are skipped.

Retrieval process:

- `evals/run_basic_queries.py` loads cases from `evals/basic_queries.json`.
- It loads markdown notes with `load_markdown_notes`.
- It chunks notes with `chunk_notes`.
- It retrieves top-k results with `retrieve`.
- It marks a case as passing when one expected source appears in retrieved results above the threshold.
- If a case has no expected sources, it passes when no retrieved result is above the threshold.

Chunking approach:

- Text is split on whitespace.
- Default chunk size is 120 words.
- Default overlap is 25 words.
- Chunk size must be greater than 0.
- Overlap must be 0 or greater and smaller than chunk size.

Embedding model:

- The default model is `sentence-transformers/all-MiniLM-L6-v2`.
- The README states that the first run downloads the sentence-transformers embedding model.

Similarity method:

- Retrieval embeds each chunk and the query.
- The repository computes cosine similarity in `src/retrieve.py`.
- Results are sorted by score in descending order.
- The default top-k value is 3.
- The default threshold is 0.35.

## Current Test Set

The current test set contains 3 queries.

Expected documents:

- 2 queries expect `attention_heads.md`.
- 1 query expects no source above threshold.

Evaluation approach:

- The test set is a small manual retrieval check set.
- It is not a benchmark dataset.
- The script does not call an LLM and does not measure answer quality.

## Results

| Query | Expected Doc | Retrieved? | Evidence |
| --- | --- | --- | --- |
| What do my notes say about attention heads? | `attention_heads.md` | Yes | `outputs/example_run.md` records top source `attention_heads.md`, score `0.617`, result `PASS`. |
| What do my notes say about transformer interpretability? | `attention_heads.md` | Yes | `outputs/example_run.md` records top source `attention_heads.md`, score `0.387`, result `PASS`. |
| What do my notes say about database indexing? | None expected | No source above threshold | `outputs/example_run.md` records top source `<none above threshold>`, score `n/a`, result `PASS`. |

The saved run reports: `Passed 3/3 retrieval checks`.

## Failure Analysis

### Observed Failures

No failures are currently documented in repository evidence.

### Potential Failures

The following potential failures are documented in `docs/failure_modes.md`.

Weak context:

- Expected behavior: the threshold should prevent weak retrieved context from being treated as grounded.
- Potential observed behavior: the threshold may reject useful context or allow weak matches.
- Likely root cause: the confidence threshold is simple and has not been calibrated against a larger set of notes.

Misleading similarity:

- Expected behavior: retrieved chunks should be sufficient to answer the query.
- Potential observed behavior: cosine similarity may return text that is semantically nearby but not actually sufficient.
- Likely root cause: embedding similarity is not the same as answer sufficiency.

Small note corpus:

- Expected behavior: retrieval behavior should generalize beyond the sample note.
- Potential observed behavior: behavior against one note may not represent a larger personal knowledge base.
- Likely root cause: the current corpus contains only one sample note.

Recomputed embeddings:

- Expected behavior: retrieval should stay usable as the note corpus grows.
- Potential observed behavior: retrieval may become slow.
- Likely root cause: embeddings are recomputed on every run.

Markdown structure loss:

- Expected behavior: retrieval should preserve useful document structure where needed.
- Potential observed behavior: headings, links, code blocks, and lists are not represented with richer structure.
- Likely root cause: markdown is loaded as plain text.

No answer generation:

- Expected behavior: this project currently retrieves context and source filenames.
- Potential observed behavior: it does not synthesize a final answer.
- Likely root cause: answer generation is outside the current implementation.

## Limitations

- The evaluation uses one sample markdown note.
- The test set contains only 3 manual queries.
- There is no benchmark dataset.
- The evaluation checks retrieval only, not answer quality.
- The confidence threshold is simple and not calibrated with a larger corpus.
- Embeddings are recomputed on every run.
- Markdown parsing is plain text loading.

## Next Evaluation Cases

1. Synonym query: ask about "self-attention routing" and expect `attention_heads.md` if the wording retrieves the sample note.
2. Ambiguous query: ask about "heads" without saying attention and check whether retrieval returns useful source material or refuses.
3. Partial-match query: ask about "attention patterns" and expect `attention_heads.md`.
4. Multi-concept retrieval: add another sample note, then ask a query that should retrieve both attention-related and second-note context.
5. Missing-document scenario: ask about a topic not present in `notes_sample/` and expect no source above threshold.
