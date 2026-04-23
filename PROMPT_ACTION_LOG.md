Prompt Action Log

2026-04-23

Prompt

User asked: "Replace blocking Playwright-style tests with a non-blocking site health report that is visible directly on the published homepage."

Files and folders inspected

* .github/workflows/
* docs/
* mkdocs.yml
* README.md
* AGENTS.md
* scripts/
* tests/

Actions taken

* Removed the blocking Playwright workflow path.
* Added a non-blocking site health report generator.
* Integrated the generated report into the homepage.
* Updated agent rules and repository guidance to use the health report.

Verification

* Ran python3 scripts/site_health.py.
* Ran .venv/bin/mkdocs build --strict --clean.
* Confirmed the built homepage includes the Site Health section and warnings.

Open questions and follow-up

* Decide later whether to keep scripts/check_template.py as a local-only helper or retire it.
