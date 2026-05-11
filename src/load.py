from pathlib import Path


def is_hidden(path: Path) -> bool:
    return any(part.startswith(".") for part in path.parts)


def load_markdown_notes(notes_dir: str | Path) -> list[dict[str, str]]:
    root = Path(notes_dir)
    notes = []

    for path in sorted(root.rglob("*.md")):
        relative_path = path.relative_to(root)
        if is_hidden(relative_path):
            continue

        notes.append(
            {
                "filename": str(relative_path),
                "text": path.read_text(encoding="utf-8"),
            }
        )

    return notes
