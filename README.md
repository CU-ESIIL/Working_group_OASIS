# Working Group Template

This repository is a template for ESIIL Working Groups.

This template is designed as one connected system:

- The repository is where the science happens.
- The website is where the science is shared.
- GitHub connects them through commits, version history, and publishing.

## How this repository is organized

The repository has two connected layers. Top-level files configure the project and its automation. The `docs/` folder contains the website content. `mkdocs.yml` tells MkDocs how to turn that content into the public site. Analysis folders hold the working scientific materials that generate the results shown on the website.

```text
.
├── README.md              # Repository overview and setup notes
├── mkdocs.yml             # Website navigation, theme, plugins, and edit links
├── docs/                  # Markdown source for the public website
├── scripts/               # Build helpers and site health checks
├── templates/             # Reusable meeting-note templates
├── containers/            # Optional runtime and environment setup
└── other working folders  # Add data, notebooks, scripts, workflows, outputs, or figures here as the group's science grows
```

Use these rules of thumb when deciding where to put something:

- Top-level files and folders are for project configuration, automation, contribution guidance, licensing, environment setup, and repo-wide metadata.
- `docs/` is for public website pages and assets. Markdown files here become website pages through MkDocs.
- `mkdocs.yml` controls how the website is rendered, including navigation, theme settings, plugins, and GitHub edit links.
- Scientific working materials belong in working folders such as data, notebooks, scripts, workflows, outputs, and figure directories.

## Common places to edit

- `docs/index.md` is the homepage for the public site.
- `docs/work-plan.md` is where the group can track milestones, meetings, and active work.
- `docs/resources.md` is where datasets, references, and code links can be collected.
- `docs/community-care.md` is where collaboration expectations and group care guidance live.
- `docs/assets/images/slots/` contains named image slots for the homepage and other shared visuals.
- `docs/assets/images/process/` contains folder-driven process galleries that render automatically on the site.

## Preview locally

```bash
pip install -r requirements.txt
python scripts/generate_image_slots.py
python scripts/site_health.py
mkdocs serve
```

## Build site

```bash
python scripts/generate_image_slots.py
python scripts/site_health.py
mkdocs build --strict --clean
```

## Swapping homepage images

The site uses semantic image slots so Working Group members do not need to edit Markdown links every time an image changes.

1. Open the relevant folder in `docs/assets/images/slots/`.
2. Delete the old image file.
3. Add one new `.png`, `.jpg`, `.jpeg`, `.webp`, or `.svg` file.
4. Run `python scripts/generate_image_slots.py`.
5. Commit the image change and the regenerated slot references.

If a slot folder contains multiple images, the generator uses the first image alphabetically and the site health report will warn you to clean it up. The cleanest workflow is still one image per slot folder.

## Using process galleries

Process galleries are folder-driven. Add files to a gallery folder, commit them, and the site updates automatically.

1. Open the relevant folder in `docs/assets/images/process/`.
2. Add images or supported deliverable files.
3. Optionally add a `captions.txt` file with lines like `filename.png | Caption text`.
4. Run `python scripts/generate_image_slots.py`.
5. Commit the new files and the regenerated gallery includes.

Supported image files:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`
- `.svg`

Supported linked deliverable files:

- `.pdf`
- `.html`
- `.csv`
- `.xlsx`
- `.docx`
- `.pptx`

## Site Health

The site generates a non-blocking health report during the build.

The report appears at the bottom of the homepage and flags common issues such as missing files, placeholder links, outdated navigation, or incomplete template fields.

Warnings do not prevent the site from publishing. They are intended to help Working Group admins improve the site.

## GitHub Pages

This site is automatically built and deployed using GitHub Actions.
