import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.chunk import chunk_notes
from src.load import load_markdown_notes

try:
    from src.retrieve import retrieve
except ModuleNotFoundError as error:
    if error.name != "sentence_transformers":
        raise

    print("Missing dependency: sentence-transformers")
    print("Install dependencies with: pip install -r requirements.txt")
    raise SystemExit(1)


DEFAULT_THRESHOLD = 0.35


def load_cases(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def top_result_above_threshold(results: list[dict], threshold: float) -> dict | None:
    if not results:
        return None

    top_result = results[0]
    if top_result["score"] < threshold:
        return None

    return top_result


def case_passed(
    expected_sources: list[str],
    results: list[dict],
    threshold: float,
) -> bool:
    passing_results = [result for result in results if result["score"] >= threshold]

    if not expected_sources:
        return not passing_results

    retrieved_sources = {result["filename"] for result in passing_results}
    return any(source in retrieved_sources for source in expected_sources)


def print_case(query: str, expected_sources: list[str], results: list[dict], threshold: float) -> bool:
    top_result = top_result_above_threshold(results, threshold)
    passed = case_passed(expected_sources, results, threshold)

    print(f"Query: {query}")
    if top_result is None:
        print("Top source: <none above threshold>")
        print("Score: n/a")
    else:
        print(f"Top source: {top_result['filename']}")
        print(f"Score: {top_result['score']:.3f}")

    print(f"Result: {'PASS' if passed else 'FAIL'}")
    print()
    return passed


def main() -> None:
    parser = argparse.ArgumentParser(description="Run basic retrieval checks.")
    parser.add_argument("--eval-file", default="evals/basic_queries.json")
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

    cases = load_cases(Path(args.eval_file))
    notes = load_markdown_notes(args.notes_dir)
    chunks = chunk_notes(notes, chunk_size=args.chunk_size, overlap=args.overlap)

    passed_count = 0
    for case in cases:
        results = retrieve(
            case["query"],
            chunks,
            model_name=args.model,
            top_k=args.top_k,
        )
        if print_case(
            case["query"],
            case.get("expected_sources", []),
            results,
            args.threshold,
        ):
            passed_count += 1

    total = len(cases)
    print(f"Passed {passed_count}/{total} retrieval checks")

    if passed_count != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
