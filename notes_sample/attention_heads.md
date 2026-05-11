# Attention Heads

Attention heads let a transformer compare each token with other tokens in the context window.

Different heads can learn different patterns. One head might connect pronouns to earlier nouns, while another might track punctuation or repeated terms.

For interpretability work, attention heads are useful because their attention patterns can sometimes be inspected directly. The pattern is not a full explanation of the model's behavior, but it can give clues about which tokens influenced a layer's computation.
