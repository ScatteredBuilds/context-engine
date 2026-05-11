# Example Run

Status: expected output only, not verified runtime output.

The local environment used to write this file did not have `sentence-transformers` installed, so the CLI was not run end to end. The example below is based only on the contents of `notes_sample/attention_heads.md`.

Command:

```bash
python ask.py "What do my notes say about attention heads?"
```

Expected output shape:

```text
Retrieved chunks
================
Source: attention_heads.md | score: <score from local embedding model>
# Attention Heads Attention heads let a transformer compare each token with other tokens in the context window. Different heads can learn different patterns...

Sources
=======
- attention_heads.md
```

Weak-context query example:

```bash
python ask.py "What do my notes say about database indexing?"
```

Expected output:

```text
I do not have enough grounded context in the notes to answer that.
```

This project currently retrieves note chunks. It does not generate a final natural-language answer.
