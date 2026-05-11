import argparse

from src.chunk import chunk_notes
from src.load import load_markdown_notes
from src.retrieve import retrieve


DEFAULT_THRESHOLD = 0.35


def print_result(result: dict[str, str | int | float]) -> None:
    print(f"Source: {result['filename']} | score: {result['score']:.3f}")
    print(result["text"])
    print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Retrieve grounded context from local markdown notes."
    )
    parser.add_argument("question")
    parser.add_argument("--notes-dir", default="notes_sample")
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--chunk-size", type=int, default=120)
    parser.add_argument("--overlap", type=int, default=25)
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    parser.add_argument(
        "--model",
        default="sentence-transformers/all-MiniLM-L6-v2",
    )
    args = parser.parse_args()

    notes = load_markdown_notes(args.notes_dir)
    chunks = chunk_notes(notes, chunk_size=args.chunk_size, overlap=args.overlap)
    results = retrieve(args.question, chunks, model_name=args.model, top_k=args.top_k)

    if not results or results[0]["score"] < args.threshold:
        print("I do not have enough grounded context in the notes to answer that.")
        return

    print("Retrieved chunks")
    print("================")
    for result in results:
        print_result(result)

    sources = sorted({str(result["filename"]) for result in results})
    print("Sources")
    print("=======")
    for source in sources:
        print(f"- {source}")


if __name__ == "__main__":
    main()
