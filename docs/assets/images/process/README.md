# Process Galleries

This folder contains folder-driven galleries for the Working Group OASIS site.

Each subfolder feeds a gallery on one or more pages. Add files to a folder, run `python scripts/generate_image_slots.py`, commit, and the site updates automatically.

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

Optional captions:

- Add a `captions.txt` file in any gallery folder.
- Use one line per file in the format `filename.ext | Caption text`.

Files are sorted alphabetically. `README.md`, hidden files, and unsupported files are ignored.
