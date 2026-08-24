"""Validate GitHub-rendered mathematical documentation before merge."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
FORBIDDEN = (
    r"\\operatorname",
    r"\\DeclareMathOperator",
    r"\\newcommand",
    r"\\def",
)
AMBIGUOUS = (
    r"\^\*",
    r"\^_",
    r"_\^",
)


def extract_math(text: str) -> list[str]:
    blocks: list[str] = []
    blocks.extend(re.findall(r"\$\$(.*?)\$\$", text, flags=re.DOTALL))
    blocks.extend(re.findall(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", text, flags=re.DOTALL))
    blocks.extend(re.findall(r"```math\s*(.*?)```", text, flags=re.DOTALL))
    return blocks


def balanced_braces(expr: str) -> bool:
    depth = 0
    escaped = False
    for char in expr:
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def main() -> int:
    failures: list[str] = []
    for path in DOCS:
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN:
            if re.search(pattern, text):
                failures.append(f"{path.relative_to(ROOT)}: forbidden LaTeX macro {pattern}")
        for pattern in AMBIGUOUS:
            if re.search(pattern, text):
                failures.append(f"{path.relative_to(ROOT)}: ambiguous LaTeX syntax {pattern}")
        math_blocks = extract_math(text)
        if not math_blocks:
            failures.append(f"{path.relative_to(ROOT)}: no math blocks detected")
        for index, expr in enumerate(math_blocks, 1):
            if not balanced_braces(expr):
                failures.append(f"{path.relative_to(ROOT)}: unbalanced braces in math block {index}")

    if failures:
        print("Documentation validation failed:")
        print("\n".join(f"- {item}" for item in failures))
        return 1

    print(f"Validated {len(DOCS)} documentation files with GitHub-safe math syntax.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
