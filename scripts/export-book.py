#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
EXPORT_METADATA = ROOT / "docs" / "export-metadata.yaml"
BUILD_DIR = ROOT / "build"
EXPORTS_DIR = ROOT / "exports"


def load_metadata() -> dict:
    if not EXPORT_METADATA.exists():
        raise SystemExit("Saknar docs/export-metadata.yaml.")

    if yaml is None:
        raise SystemExit("Python-paketet PyYAML saknas. Installera med: pip install pyyaml")

    data = yaml.safe_load(EXPORT_METADATA.read_text(encoding="utf-8")) or {}
    for field in ["title", "author", "language", "identifier", "date", "version"]:
        if not data.get(field):
            raise SystemExit(f"Metadatafält saknas eller är tomt: {field}")
    return data


def count_table_cells(line: str) -> int:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return -1
    return len([part for part in stripped.split("|")[1:-1]])


def validate_markdown(path: Path, text: str) -> list[str]:
    errors: list[str] = []

    for idx, line in enumerate(text.splitlines(), start=1):
        if re.match(r"^#{4,}\s", line):
            errors.append(f"{path}: rad {idx}: H4 eller djupare rubrik är inte tillåten.")

    if text.count("```") % 2 != 0:
        errors.append(f"{path}: ojämnt antal kodblocksmarkörer.")

    lines = text.splitlines()
    table_separator_re = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")

    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if line.strip().startswith("|") and line.strip().endswith("|"):
            table_start = idx
            table_lines = []
            while idx < len(lines) and lines[idx].strip().startswith("|") and lines[idx].strip().endswith("|"):
                table_lines.append((idx + 1, lines[idx]))
                idx += 1

            if len(table_lines) < 2 or not table_separator_re.match(table_lines[1][1]):
                errors.append(f"{path}: rad {table_lines[0][0]}: möjlig tabell utan korrekt separatorrad.")
                continue

            expected_cells = count_table_cells(table_lines[0][1])
            for line_no, table_line in table_lines:
                cells = count_table_cells(table_line)
                if cells != expected_cells:
                    errors.append(f"{path}: rad {line_no}: tabellrad har annat antal celler.")
        else:
            idx += 1

    for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
        target = match.group(1)
        if target.startswith(("http://", "https://")):
            continue
        image_path = (path.parent / target).resolve()
        if not image_path.exists():
            errors.append(f"{path}: bildreferens saknar fil: {target}")

    return errors


def collect_chapters(metadata: dict) -> list[Path]:
    chapters = metadata.get("chapters") or []
    if not chapters:
        raise SystemExit("Inga kapitel angivna i docs/export-metadata.yaml.")

    paths = [(ROOT / chapter).resolve() for chapter in chapters]
    if paths[0].name != "00-inledning.md":
        raise SystemExit("Första kapitlet i metadata måste vara chapters/00-inledning.md.")

    for path in paths:
        if not path.exists():
            raise SystemExit(f"Saknar kapitel: {path.relative_to(ROOT)}")

    return paths


def build_markdown(metadata: dict, chapters: list[Path]) -> Path:
    BUILD_DIR.mkdir(exist_ok=True)
    output = BUILD_DIR / "book.md"

    parts = []
    title = metadata["title"]
    subtitle = metadata.get("subtitle", "")
    author = metadata["author"]

    parts.append(f"% {title}\n% {author}\n")
    if subtitle:
        parts.append(f"\n> {subtitle}\n")

    for chapter in chapters:
        text = chapter.read_text(encoding="utf-8")
        errors = validate_markdown(chapter.relative_to(ROOT), text)
        if errors:
            raise SystemExit("Valideringsfel:\n" + "\n".join(errors))
        parts.append("\n\n" + text.strip() + "\n")

    output.write_text("\n".join(parts), encoding="utf-8")
    return output


def run_pandoc(args: list[str]) -> None:
    if shutil.which("pandoc") is None:
        raise SystemExit("Pandoc saknas. Installera Pandoc och kör exporten igen.")

    subprocess.run(["pandoc", *args], check=True)


def export_epub(metadata: dict, source: Path) -> None:
    EXPORTS_DIR.mkdir(exist_ok=True)
    output = EXPORTS_DIR / "greenfield-eller-brownfield.epub"
    args = [
        str(source),
        "--from=gfm",
        "--to=epub3",
        "--metadata", f"title={metadata['title']}",
        "--metadata", f"author={metadata['author']}",
        "--metadata", "lang=sv-SE",
        "--metadata", f"identifier={metadata['identifier']}",
        "--css=styles/epub.css",
        f"--output={output}",
    ]
    cover = metadata.get("cover_image")
    if cover and (ROOT / cover).exists():
        args.insert(-1, f"--epub-cover-image={cover}")
    run_pandoc(args)
    print(f"Skapade {output.relative_to(ROOT)}")


def export_pdf(metadata: dict, source: Path) -> None:
    EXPORTS_DIR.mkdir(exist_ok=True)
    output = EXPORTS_DIR / "greenfield-eller-brownfield.pdf"
    args = [
        str(source),
        "--from=gfm",
        "--pdf-engine=xelatex",
        "--toc",
        "--toc-depth=3",
        "--metadata", f"title={metadata['title']}",
        "--metadata", f"author={metadata['author']}",
        "--metadata", "lang=sv-SE",
        f"--output={output}",
    ]
    try:
        run_pandoc(args)
    except subprocess.CalledProcessError as exc:
        raise SystemExit(
            "PDF-export misslyckades. Kontrollera att xelatex finns installerat, "
            "exempelvis via MacTeX eller TinyTeX."
        ) from exc
    print(f"Skapade {output.relative_to(ROOT)}")


def main() -> None:
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    if target not in {"all", "epub", "pdf", "validate"}:
        raise SystemExit("Använd: export-book.py [all|epub|pdf|validate]")

    metadata = load_metadata()
    chapters = collect_chapters(metadata)
    source = build_markdown(metadata, chapters)

    if target == "validate":
        print("Validering klar.")
        return

    if target in {"all", "epub"}:
        export_epub(metadata, source)
    if target in {"all", "pdf"}:
        export_pdf(metadata, source)


if __name__ == "__main__":
    main()
