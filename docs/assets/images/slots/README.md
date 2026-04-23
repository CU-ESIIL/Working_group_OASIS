# Image Slots

This folder contains semantic image slots for the website.

Each subfolder controls one purpose-driven image location, such as the homepage hero image, the group photo, or one of the square workflow buttons.

To swap an image:

1. Open the relevant slot folder.
2. Delete the old image.
3. Add one new `.png`, `.jpg`, `.jpeg`, `.webp`, or `.svg` file.
4. Run `python scripts/generate_image_slots.py`.
5. Commit the image and regenerated slot references.

Use one image per slot folder. If multiple images are present, the site generator uses the first image alphabetically and the site health report will warn you to clean the folder up.
