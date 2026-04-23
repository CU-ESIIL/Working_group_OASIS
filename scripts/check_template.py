from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MKDOCS_FILE = ROOT / "mkdocs.yml"

REQUIRED_FILES = [
    ROOT / "docs/index.md",
    ROOT / "docs/work-plan.md",
    ROOT / "docs/resources.md",
    ROOT / "docs/community-care.md",
    MKDOCS_FILE,
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / "PROMPT_ACTION_LOG.md",
]

ALLOWED_NAV = ["Home", "Work Plan", "Resources", "Community Care", "Outputs"]
REQUIRED_NAV = ["Home", "Work Plan", "Resources", "Community Care"]
DISALLOWED_NAV = ["Art Gallery", "Code of Conduct", "Participant Agreement"]


def nav_labels(text: str) -> list[str]:
    lines = text.splitlines()
    in_nav = False
    labels: list[str] = []

    for line in lines:
        if not in_nav:
            if line.strip() == "nav:":
                in_nav = True
            continue

        if line and not line.startswith((" ", "\t", "-")):
            break

        match = re.match(r"^\s{2}-\s+([^:]+):\s*", line)
        if match:
            labels.append(match.group(1).strip())

    return labels


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")

    if not MKDOCS_FILE.exists():
        errors.append("Missing required file: mkdocs.yml")
    else:
        labels = nav_labels(MKDOCS_FILE.read_text(encoding="utf-8"))
        unknown = [label for label in labels if label not in ALLOWED_NAV]
        missing = [label for label in REQUIRED_NAV if label not in labels]
        banned = [label for label in labels if label in DISALLOWED_NAV]

        if unknown:
            errors.append(
                "mkdocs.yml nav contains unsupported items: "
                + ", ".join(unknown)
            )
        if missing:
            errors.append(
                "mkdocs.yml nav is missing required items: "
                + ", ".join(missing)
            )
        if banned:
            errors.append(
                "mkdocs.yml nav contains disallowed items: "
                + ", ".join(banned)
            )

    if errors:
        print("Template integrity check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Template integrity check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
