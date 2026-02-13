import re
import sys

TAGS: list[str] = [
    "gnome",
    "elementary",
    "gtk3",
    "gtk4",
    "libadwaita",
    "libhandy",
    "libgranite",
    "libxapp",
    "relm",
    "relm4",
    "c",
    "c++",
    "csharp",
    "d",
    "zig",
    "go",
    "rust",
    "vala",
    "granite",  # TODO: granite -> libgranite
    "python",
    "julia",
    "lua",
    "haskell",
    "perl",
    "swift",
    "crystal",
    "gjs",
    "javascript",
    "clojurescript",
    "typescript",
    "scheme",
    "kotlin",
    "lisp",
]


def lint_awesome_list(text: str, allowed_tags: list[str]) -> list[tuple[int, str]]:
    lines: list[str] = text.split("\n")
    errors: list[tuple[int, str]] = []
    linting: bool = False
    found_lint_start: bool = False
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        if line == "<!-- custom-lint start-->":
            linting = True
            found_lint_start = True
            continue
        if not linting:
            continue
        if not line.startswith("-") or line.startswith("---"):
            continue
        if not line.startswith("- ["):
            errors.append(
                (
                    line_number,
                    "Must start with '- [Name](url) - description `#tag1` `#tag2`.",
                )
            )
            continue
        link_match = re.match(r"^- \[([^\]]+)\]\(([^)]+)\) - (.+)$", line)
        if not link_match:
            errors.append((line_number, "Invalid link format."))
            continue
        tags = re.findall(r"`#(\S+)`", line)
        if not tags:
            errors.append(
                (
                    line_number,
                    "No valid tags found (must be wrapped in single backticks, e.g., `#tag`).",
                )
            )
            continue
        for tag in tags:
            if tag not in allowed_tags:
                errors.append(
                    (
                        line_number,
                        f"Tag `{tag}` is not allowed. Allowed tags: {sorted(allowed_tags)}",
                    )
                )
    if not found_lint_start:
        errors.append(
            (0, "Lint start marker `<!-- custom-lint start-->` not found in the file.")
        )
    return errors


def main():
    file_path: str = "README.md"
    text: str = open(file_path, "r", encoding="utf-8").read()
    errors: list[tuple[int, str]] = lint_awesome_list(text, TAGS)
    if errors:
        for line_number, message in errors:
            print(f"::error file={file_path},line={line_number}::{message}")
        sys.exit(1)


if __name__ == "__main__":
    main()
