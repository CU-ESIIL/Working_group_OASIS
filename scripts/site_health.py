from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPORT = DOCS / "_site_health.md"
MKDOCS = ROOT / "mkdocs.yml"

REQUIRED_FILES = [
    ROOT / "docs/index.md",
    ROOT / "docs/work-plan.md",
    ROOT / "docs/resources.md",
    ROOT / "docs/community-care.md",
    ROOT / "mkdocs.yml",
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "PROMPT_ACTION_LOG.md",
]

PLACEHOLDERS = {
    "[link]": "generic placeholder link",
    "TODO": "TODO placeholder",
    "TBD": "TBD placeholder",
    "Short one-sentence description": "homepage description placeholder",
    "Name | Role": "people table placeholder",
    "GitHub Community Care Page Link": "community care link placeholder",
}

REQUIRED_NAV = ["Home", "Work Plan", "Resources", "Community Care"]
DEPRECATED_NAV = ["Art Gallery", "Code of Conduct", "Participant Agreement"]
TEXT_FILES = [ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "PROMPT_ACTION_LOG.md", MKDOCS]


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


def all_text_files() -> list[Path]:
    files = list(TEXT_FILES)
    files.extend(sorted(DOCS.rglob("*.md")))
    return files


def placeholder_issues() -> list[str]:
    issues: list[str] = []

    for path in all_text_files():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for needle, description in PLACEHOLDERS.items():
            if needle == "Name | Role":
                if needle in text.replace("|------|------|", ""):
                    issues.append(
                        f"⚠ Placeholder detected: {description} in {path.relative_to(ROOT)}"
                    )
                continue
            if needle in text:
                issues.append(
                    f"⚠ Placeholder detected: {description} in {path.relative_to(ROOT)}"
                )

    return issues


def missing_file_issues() -> list[str]:
    issues: list[str] = []
    for path in REQUIRED_FILES:
        if not path.exists():
            issues.append(f"⚠ Missing required file: {path.relative_to(ROOT)}")
    return issues


def navigation_issues() -> list[str]:
    if not MKDOCS.exists():
        return ["⚠ Navigation issue: mkdocs.yml is missing."]

    labels = nav_labels(MKDOCS.read_text(encoding="utf-8"))
    issues: list[str] = []

    for label in REQUIRED_NAV:
        if label not in labels:
            issues.append(f"⚠ Navigation issue: missing nav item '{label}'.")

    for label in DEPRECATED_NAV:
        if label in labels:
            issues.append(f"⚠ Navigation issue: deprecated nav item '{label}' is still present.")

    return issues


def internal_link_issues() -> list[str]:
    issues: list[str] = []
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            clean = target.strip()
            if not clean or clean.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if clean.startswith("<") and clean.endswith(">"):
                clean = clean[1:-1]
            if clean.endswith((".png", ".jpg", ".jpeg", ".svg", ".gif", ".ico", ".webp")):
                resolved = (path.parent / clean).resolve()
            else:
                resolved = (path.parent / clean.split("#", 1)[0]).resolve()
            if not resolved.exists():
                issues.append(
                    f"⚠ Internal link issue: {path.relative_to(ROOT)} links to missing target '{target}'."
                )

    return issues


def write_report(issues: list[str]) -> None:
    lines = ["Site Health", ""]

    if not issues:
        lines.append("✓ No issues detected.")
    else:
        for issue in issues:
            lines.append(issue)
            lines.append("")

    lines.extend(
        [
            "",
            "This report is generated automatically during the site build. Fix these items in the repository to improve the site.",
            "",
        ]
    )

    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    issues = []
    issues.extend(missing_file_issues())
    issues.extend(placeholder_issues())
    issues.extend(navigation_issues())
    issues.extend(internal_link_issues())
    write_report(issues)
    print(f"Generated {REPORT.relative_to(ROOT)} with {len(issues)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
