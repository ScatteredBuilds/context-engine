# Failure Modes

This project is an early retrieval-only slice. These are known failure modes to inspect as the system grows.

## Weak Context

The CLI refuses when the top retrieval score is below the configured threshold. This threshold is simple and may reject useful context or allow weak matches.

## Misleading Similarity

Cosine similarity over embeddings can return text that is semantically nearby but not actually sufficient to answer the question.

## Small Note Corpus

With only one sample note, retrieval behavior is easy to inspect but not representative of a larger personal knowledge base.

## Recomputed Embeddings

Embeddings are recomputed on every run. This keeps the code simple, but it will become slow as the note corpus grows.

## Markdown Structure Loss

Markdown is loaded as plain text. Headings, links, code blocks, and lists are not parsed into richer structure yet.

## No Answer Generation

The current CLI prints retrieved chunks and source filenames. It does not synthesize a final answer from the retrieved context.
