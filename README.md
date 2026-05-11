# context-engine

A local context and retrieval engine for grounding model answers in personal notes.

This project starts as a local RAG system over Obsidian notes using Python and local models.

## Goal

Given a question:
- retrieve relevant notes
- provide grounded context
- generate an answer
- cite source filenames
- refuse weak-context queries

Target command:

python ask.py "What do my notes say about attention heads?"

## Planned structure

context-engine/
  src/
  notes_sample/
  evals/
  outputs/
  docs/

## Milestones

1. Load markdown notes
2. Add chunking
3. Add embeddings
4. Add retrieval
5. Add local model answering
6. Add refusal behavior
7. Add evals
8. Document failure cases

## Current status

Early buildout.
