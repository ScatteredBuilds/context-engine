# Expanded Evaluation Run

Command:

```bash
.venv/bin/python evals/run_basic_queries.py --eval-file evals/expanded_queries.json
```

Output:

```text
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 17455.08it/s]
Query: What do my notes say about attention heads?
Top source: attention_heads.md
Score: 0.617
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 16375.93it/s]
Query: How do transformer attention heads compare tokens?
Top source: attention_heads.md
Score: 0.733
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 13451.65it/s]
Query: What patterns can different heads learn?
Top source: attention_heads.md
Score: 0.523
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 15264.41it/s]
Query: What do the notes say about pronouns and earlier nouns?
Top source: attention_heads.md
Score: 0.353
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 14015.49it/s]
Query: How are punctuation or repeated terms tracked in transformer notes?
Top source: attention_heads.md
Score: 0.465
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 14882.64it/s]
Query: What does the note say about attention patterns?
Top source: attention_heads.md
Score: 0.571
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 14533.18it/s]
Query: Why are attention heads useful for interpretability work?
Top source: attention_heads.md
Score: 0.753
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 15516.60it/s]
Query: Can attention patterns fully explain model behavior?
Top source: attention_heads.md
Score: 0.626
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 16079.10it/s]
Query: What clues can attention give about which tokens influenced computation?
Top source: attention_heads.md
Score: 0.472
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 13682.13it/s]
Query: How does a transformer connect words across the context window?
Top source: attention_heads.md
Score: 0.495
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 16398.30it/s]
Query: What component helps tokens look at other tokens?
Top source: attention_heads.md
Score: 0.448
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 14345.45it/s]
Query: Do the notes discuss interpretability and token influence together?
Top source: attention_heads.md
Score: 0.447
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 13863.02it/s]
Query: What do the notes say about patterns, punctuation, and repeated terms?
Top source: attention_heads.md
Score: 0.383
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 13513.51it/s]
Query: What are heads?
Top source: attention_heads.md
Score: 0.427
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 13790.01it/s]
Query: What does the note say about terms?
Top source: <none above threshold>
Score: n/a
Result: FAIL

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 14353.56it/s]
Query: What do my notes say about database indexing?
Top source: <none above threshold>
Score: n/a
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 23853.64it/s]
Query: What do my notes say about AWS networking?
Top source: <none above threshold>
Score: n/a
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 13566.55it/s]
Query: What do my notes say about payment outages?
Top source: <none above threshold>
Score: n/a
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 18243.81it/s]
Query: What do my notes say about Python package management?
Top source: <none above threshold>
Score: n/a
Result: PASS

Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]Loading weights: 100%|██████████| 103/103 [00:00<00:00, 12602.12it/s]
Query: What do my notes say about customer support workflows?
Top source: <none above threshold>
Score: n/a
Result: PASS

Passed 19/20 retrieval checks

```

Exit status: 1
