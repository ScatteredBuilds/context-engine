def chunk_text(
    text: str,
    filename: str,
    chunk_size: int = 120,
    overlap: int = 25,
) -> list[dict[str, str | int]]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if overlap < 0:
        raise ValueError("overlap must be 0 or greater")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    words = text.split()
    chunks = []
    start = 0
    chunk_id = 0

    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk_words = words[start:end]

        if chunk_words:
            chunks.append(
                {
                    "filename": filename,
                    "chunk_id": chunk_id,
                    "text": " ".join(chunk_words),
                }
            )

        if end == len(words):
            break

        start = end - overlap
        chunk_id += 1

    return chunks


def chunk_notes(
    notes: list[dict[str, str]],
    chunk_size: int = 120,
    overlap: int = 25,
) -> list[dict[str, str | int]]:
    chunks = []

    for note in notes:
        chunks.extend(
            chunk_text(
                text=note["text"],
                filename=note["filename"],
                chunk_size=chunk_size,
                overlap=overlap,
            )
        )

    return chunks
