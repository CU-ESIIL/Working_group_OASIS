Prompt Action Log

2026-04-29

Prompt

User asked: "Add selected Project Group OASIS infrastructure, instruction, and participant-support features to Working Group OASIS, adapted for the longer working-group lifecycle, without replacing the existing Working Group template or adding excluded sprint-oriented features."

Files and folders inspected

* Project_group_OASIS public site and repository listing
* docs/
* mkdocs.yml
* README.md
* AGENTS.md
* scripts/

Actions taken

* Added Cloud Triangle guidance for GitHub, compute, and persistent storage.
* Added JupyterLab/GitHub workflow instructions for linking, pulling, committing, pushing, and resolving simple conflicts.
* Added persistent storage guidance using GoCommands examples and working-group placeholder paths.
* Added working-group lifecycle and landmark instruction pages.
* Added public-facing site and cite/reuse guidance.
* Exposed new pages under the existing Resources navigation section.
* Added subtle working-group landmark guidance to the homepage.
* Updated README and AGENTS.md with additive contributor guidance.

Verification

* Ran `python3 scripts/generate_image_slots.py`.
* Ran `python3 scripts/site_health.py`.
* Ran `python3 scripts/check_template.py`.
* Ran `.venv/bin/mkdocs build --strict --clean`.
* Checked for excluded Project Group features and event-sprint language in the edited documentation; the only match was a pre-existing `docs/work-plan.md` heading.

Open questions and follow-up

* Confirm the exact shared persistent storage path with ESIIL staff or the working group facilitator.
* Future visual design could add small landmark stickers, but current labels intentionally remain plain Markdown.

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

2026-04-23

Prompt

User asked: "Reorganize the Working Group OASIS homepage around the repository plus website workflow, clarify how the repo is organized, and add a simple image-slot system for homepage visuals."

Files and folders inspected

* docs/
* docs/stylesheets/
* mkdocs.yml
* README.md
* scripts/
* .github/workflows/

Actions taken

* Rewrote the homepage to explain the repository side, website side, and GitHub bridge with a clearer start path.
* Added homepage edit affordances and enabled MkDocs Material edit actions.
* Clarified the repository structure in the root README and MkDocs comments.
* Added semantic image slot folders, slot documentation, and a pre-build generator for stable image references.
* Extended the site health report and GitHub Pages workflow to cover the new image-slot system.

Verification

* Ran `python3 scripts/generate_image_slots.py`.
* Ran `python3 scripts/site_health.py`.
* Ran `python3 scripts/check_template.py`.
* Ran `.venv/bin/mkdocs build --strict --clean`.
* Verified the built homepage in a local browser against `site/index.html`, including the visible edit affordance and GitHub edit-mode URL for `docs/index.md`.

Open questions and follow-up

* Consider whether future template iterations should add dedicated README files for scientific working folders once those folders become part of the base template.

2026-04-23

Prompt

User asked: "Generate and integrate an image system for Working Group OASIS with semantic image slots, folder-driven process galleries, replacement guidance, and reusable site-wide integration."

Files and folders inspected

* docs/
* docs/assets/images/
* docs/stylesheets/
* scripts/
* mkdocs.yml
* README.md
* .github/workflows/

Actions taken

* Expanded the image build step to generate both stable slot references and reusable gallery includes from semantic folders.
* Added the missing `group-photo` slot and replaced the slot placeholder artwork with cleaner SVG placeholders matched to hero, button, and collaboration use cases.
* Added process-gallery folders, README instructions, starter placeholder assets, and sample linked deliverables.
* Wired slot images, figure-style replacement notes, and folder-driven galleries into the homepage, work plan, resources, and community care pages.
* Extended styling, site health checks, and GitHub Actions build steps to support the new image and gallery system.

Verification

* Ran `python3 scripts/generate_image_slots.py`.
* Ran `python3 scripts/site_health.py`.
* Ran `python3 scripts/check_template.py`.
* Ran `.venv/bin/mkdocs build --strict --clean`.
* Verified the rendered homepage and resources page in the in-app browser against the built `site/` output.

Open questions and follow-up

* If future template pages are added below another nested directory level, the gallery generator may need one more relative-path variant for those deeper pages.
