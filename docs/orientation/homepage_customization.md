# Customizing the Homepage

This guide shows how to personalize the homepage by swapping images and editing animated buttons.

## Replace the Placeholder Image

1. Add your image to `docs/assets/` (SVG recommended for text-based images).
2. Open `docs/index.md` and update the `src` attribute of the `<img>` tag.
3. Commit the new image to your repository.

## Edit the Buttons

- Buttons are defined in `docs/index.md` inside `<a>` tags with the class `animated-button`.
- Change the button text between the opening and closing tags.
- Update the `href` attribute to point to your target page or external link.

## Tweak Animations

Animation styles live in `docs/stylesheets/extra.css`.
Modify these CSS rules to change colors, hover effects, or animation speeds.
