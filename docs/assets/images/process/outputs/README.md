# Outputs Gallery

This folder feeds an automatic gallery on the Working Group OASIS website.

Use this folder for draft figures, polished outputs, maps, synthesis graphics, and final visuals.

Supported files:

- Images: `.png`, `.jpg`, `.jpeg`, `.webp`, `.svg`
- Deliverables: `.pdf`, `.html`, `.csv`, `.xlsx`, `.docx`, `.pptx`

How to add files:

1. Upload files to this folder.
2. Optionally add `captions.txt` entries like `filename.png | Caption text`.
3. Run `python scripts/generate_image_slots.py`.
4. Commit the files and regenerated gallery includes.
