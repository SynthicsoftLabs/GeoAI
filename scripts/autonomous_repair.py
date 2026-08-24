"""Autonomous deterministic repair engine for GeoAI repository invariants."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

UNSUPPORTED_REPLACEMENTS = {
    r"\\operatorname\{Fix\}": r"\\mathrm{Fix}",
    r"\\operatorname\{arsinh\}": r"\\mathrm{arsinh}",
}


def repair_latex(text: str) -> str:
    for pattern, replacement in UNSUPPORTED_REPLACEMENTS.items():
        text = re.sub(pattern, replacement, text)

    # GitHub's Markdown parser can reinterpret literal asterisks and underscores
    # inside math. Normalize the forms that are known to render ambiguously.
    text = re.sub(r"\^(?<!\{)\*", r"^{\\ast}", text)
    text = re.sub(r"\^\{\*\}", r"^{\\ast}", text)
    text = re.sub(r"\^_", r"^{_}", text)
    text = re.sub(r"_\*", r"_{\\ast}", text)
    return text


def repair_docs() -> bool:
    changed = False
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", ".venv", "venv"} for part in path.parts):
            continue
        original = path.read_text(encoding="utf-8")
        repaired = repair_latex(original)
        if repaired != original:
            path.write_text(repaired, encoding="utf-8")
            changed = True
    return changed


def repair_project_metadata() -> bool:
    path = ROOT / "pyproject.toml"
    if not path.exists():
        return False
    original = path.read_text(encoding="utf-8")
    repaired = re.sub(r'license\s*=\s*\{text\s*=\s*"[^"]+"\}', 'license = {text = "Apache-2.0"}', original)
    if repaired != original:
        path.write_text(repaired, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = repair_docs() or repair_project_metadata()
    print("AUTONOMOUS_REPAIR_CHANGED=" + str(changed).lower())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
