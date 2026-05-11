from math import sqrt
from typing import Iterable

from sentence_transformers import SentenceTransformer


def cosine_similarity(a: Iterable[float], b: Iterable[float]) -> float:
    a_values = list(a)
    b_values = list(b)

    dot = sum(x * y for x, y in zip(a_values, b_values))
    a_norm = sqrt(sum(x * x for x in a_values))
    b_norm = sqrt(sum(y * y for y in b_values))

    if a_norm == 0 or b_norm == 0:
        return 0.0

    return dot / (a_norm * b_norm)


def retrieve(
    query: str,
    chunks: list[dict[str, str | int]],
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    top_k: int = 3,
) -> list[dict[str, str | int | float]]:
    if not chunks:
        return []

    model = SentenceTransformer(model_name)
    texts = [str(chunk["text"]) for chunk in chunks]
    chunk_embeddings = model.encode(texts)
    query_embedding = model.encode(query)

    scored_chunks = []
    for chunk, embedding in zip(chunks, chunk_embeddings):
        scored_chunks.append(
            {
                **chunk,
                "score": cosine_similarity(query_embedding, embedding),
            }
        )

    return sorted(scored_chunks, key=lambda item: item["score"], reverse=True)[:top_k]
