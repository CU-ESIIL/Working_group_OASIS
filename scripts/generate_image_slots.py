from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
GENERATED = DOCS / "_generated"
SLOTS_ROOT = DOCS / "assets" / "images" / "slots"
PROCESS_ROOT = DOCS / "assets" / "images" / "process"
IMAGE_OUTPUT = GENERATED / "image_slots.md"
SLOT_NOTES_ROOT = GENERATED / "slot_notes"
GALLERIES_ROOT = GENERATED / "galleries"

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
DELIVERABLE_EXTENSIONS = {".pdf", ".html", ".csv", ".xlsx", ".docx", ".pptx"}
SUPPORTED_EXTENSIONS = IMAGE_EXTENSIONS | DELIVERABLE_EXTENSIONS
CAPTION_FILE = "captions.txt"
REPO_URL = "https://github.com/CU-ESIIL/Working_group_OASIS"

SLOT_METADATA = {
    "hero": {
        "title": "Homepage hero image",
        "caption": "This image gives the Working Group homepage a shared visual identity for environmental data science.",
        "instructions": "To update: delete the current image in this folder and upload one new image. Keep it clean, uncluttered, and concept-driven rather than photo-real.",
        "fallback": "placeholder.svg",
    },
    "group-photo": {
        "title": "Group photo image",
        "caption": "This image represents collaboration, team identity, or a real working group photo.",
        "instructions": "To update: delete the current image in this folder and upload one new image. A real group photo is welcome here, but an abstract collaboration image also works.",
        "fallback": "placeholder.svg",
    },
    "repository-side": {
        "title": "Repository-side image",
        "caption": "This image represents the repository side of the working group: data, code, workflows, and reproducibility.",
        "instructions": "To update: delete the current image in this folder and upload one new square image. Use a flat, minimal, screen-print style graphic with no text.",
        "fallback": "placeholder.svg",
    },
    "website-side": {
        "title": "Website-side image",
        "caption": "This image represents the website side of the working group: summaries, maps, figures, and public communication.",
        "instructions": "To update: delete the current image in this folder and upload one new square image. Use a flat, minimal, screen-print style graphic with no text.",
        "fallback": "placeholder.svg",
    },
    "data": {
        "title": "Data image",
        "caption": "This image represents datasets, metadata, and the data sources behind the working group.",
        "instructions": "To update: delete the current image in this folder and upload one new square image. Use a flat, minimal, screen-print style graphic with no text.",
        "fallback": "placeholder.svg",
    },
    "analysis": {
        "title": "Analysis image",
        "caption": "This image represents analysis, notebooks, methods, and exploratory workflows.",
        "instructions": "To update: delete the current image in this folder and upload one new square image. Use a flat, minimal, screen-print style graphic with no text.",
        "fallback": "placeholder.svg",
    },
    "outputs": {
        "title": "Outputs image",
        "caption": "This image represents figures, synthesis products, and the final outputs shared by the working group.",
        "instructions": "To update: delete the current image in this folder and upload one new square image. Use a flat, minimal, screen-print style graphic with no text.",
        "fallback": "placeholder.svg",
    },
}

PROCESS_METADATA = {
    "start-here": {
        "description": "This gallery displays early setup artifacts for the working group.",
        "instructions": "Use this folder for kickoff notes, orientation screenshots, starter diagrams, and early planning visuals.",
    },
    "data": {
        "description": "This gallery displays data source artifacts and metadata documentation for the working group.",
        "instructions": "Use this folder for dataset screenshots, metadata views, download notes, and data reference visuals.",
    },
    "methods": {
        "description": "This gallery displays methods, protocols, and analysis setup artifacts.",
        "instructions": "Use this folder for method diagrams, notebook screenshots, protocol sketches, and workflow setup visuals.",
    },
    "exploration": {
        "description": "This gallery displays rough exploration artifacts for the working group.",
        "instructions": "Use this folder for draft plots, exploratory figures, and quick visual checks.",
    },
    "whiteboards": {
        "description": "This gallery displays whiteboards, meeting sketches, and planning visuals.",
        "instructions": "Use this folder for photographed whiteboards, conceptual sketches, and facilitation notes.",
    },
    "workflows": {
        "description": "This gallery displays workflow artifacts and reproducibility notes.",
        "instructions": "Use this folder for pipeline diagrams, task trackers, and reproducibility snapshots.",
    },
    "outputs": {
        "description": "This gallery displays emerging and final outputs from the working group.",
        "instructions": "Use this folder for draft figures, polished graphics, synthesis visuals, and final output previews.",
    },
    "deliverables": {
        "description": "This gallery displays deliverable files and linked products for the working group.",
        "instructions": "Use this folder for reports, spreadsheets, slides, manuscripts, and other shareable deliverables.",
    },
    "reports": {
        "description": "This gallery displays report-ready documents and summary materials.",
        "instructions": "Use this folder for report drafts, PDFs, executive summaries, and update memos.",
    },
    "community": {
        "description": "This gallery displays community-facing updates, outreach visuals, and collaboration artifacts.",
        "instructions": "Use this folder for event photos, outreach materials, collaboration snapshots, and community update graphics.",
    },
}


def relpath(path: Path) -> str:
    return path.relative_to(DOCS).as_posix()


def github_folder_url(path: Path) -> str:
    return f"{REPO_URL}/tree/main/{path.relative_to(ROOT).as_posix()}"


def visible_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return sorted(
        [
            path
            for path in folder.iterdir()
            if path.is_file()
            and not path.name.startswith(".")
            and path.name != "README.md"
            and path.name != CAPTION_FILE
            and path.suffix.lower() in SUPPORTED_EXTENSIONS
        ],
        key=lambda path: path.name.lower(),
    )


def load_captions(folder: Path) -> dict[str, str]:
    captions_path = folder / CAPTION_FILE
    if not captions_path.exists():
        return {}

    captions: dict[str, str] = {}
    for line in captions_path.read_text(encoding="utf-8").splitlines():
        clean = line.strip()
        if not clean or clean.startswith("#") or "|" not in clean:
            continue
        name, caption = clean.split("|", 1)
        captions[name.strip()] = caption.strip()
    return captions


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def render_slot_refs() -> None:
    ensure_parent(IMAGE_OUTPUT)
    lines = ["<!-- This file is generated by scripts/generate_image_slots.py. -->", ""]

    for slot_name, meta in SLOT_METADATA.items():
        slot_dir = SLOTS_ROOT / slot_name
        images = [path for path in visible_files(slot_dir) if path.suffix.lower() in IMAGE_EXTENSIONS]
        selected = images[0] if images else slot_dir / meta["fallback"]
        lines.append(f"[slot-{slot_name}]: {relpath(selected)}")

        note_path = SLOT_NOTES_ROOT / f"{slot_name}.md"
        ensure_parent(note_path)
        note_path.write_text(
            "\n".join(
                [
                    f"> {meta['caption']}",
                    ">",
                    f"> [Replace this image in GitHub]({github_folder_url(slot_dir)})",
                    ">",
                    f"> {meta['instructions']}",
                    ">",
                    "> Delete this note after the site is customized.",
                    "",
                ]
            ),
            encoding="utf-8",
        )

    IMAGE_OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def image_caption(file: Path, captions: dict[str, str]) -> str:
    return captions.get(file.name, file.stem.replace("-", " ").replace("_", " ").title())


def file_label(file: Path) -> str:
    return f"{file.suffix.lower().lstrip('.').upper()} file"


def asset_href(path: Path, prefix: str) -> str:
    return f"{prefix}{relpath(path)}"


def render_gallery(folder: Path, prefix_name: str, prefix: str) -> None:
    rel = folder.relative_to(PROCESS_ROOT)
    output = GALLERIES_ROOT / prefix_name / rel / "index.md"
    ensure_parent(output)

    files = visible_files(folder)
    captions = load_captions(folder)
    images = [path for path in files if path.suffix.lower() in IMAGE_EXTENSIONS]
    deliverables = [path for path in files if path.suffix.lower() in DELIVERABLE_EXTENSIONS]
    meta = PROCESS_METADATA.get(rel.as_posix(), {})
    description = meta.get("description", f"This gallery displays artifacts from the {rel.as_posix()} folder.")
    instructions = meta.get(
        "instructions",
        "Use this folder for images, PDFs, and other files you want the website to display automatically.",
    )

    lines = ["<!-- This file is generated by scripts/generate_image_slots.py. -->", ""]

    if images:
        lines.append('<div class="media-gallery">')
        for image in images:
            alt = image_caption(image, captions)
            lines.extend(
                [
                    '  <figure class="media-gallery__card media-gallery__card--image">',
                    f'    <a href="{asset_href(image, prefix)}">',
                    f'      <img src="{asset_href(image, prefix)}" alt="{alt}">',
                    "    </a>",
                    f'    <figcaption>{alt}</figcaption>',
                    "  </figure>",
                ]
            )
        lines.append("</div>")
        lines.append("")

    if deliverables:
        lines.append('<div class="media-gallery media-gallery--files">')
        for file in deliverables:
            caption = image_caption(file, captions)
            lines.extend(
                [
                    f'  <a class="media-gallery__card media-gallery__card--file" href="{asset_href(file, prefix)}">',
                    f'    <strong>{caption}</strong>',
                    f'    <span>{file_label(file)} · {file.name}</span>',
                    "  </a>",
                ]
            )
        lines.append("</div>")
        lines.append("")

    if not images and not deliverables:
        lines.extend(
            [
                "No gallery files yet.",
                "",
                "Add images, PDFs, or other supported files to this folder and commit. The website will display them automatically.",
                "",
            ]
        )

    lines.extend(
        [
            f"> {description}",
            ">",
            f"> [Add or replace files in this gallery]({github_folder_url(folder)})",
            ">",
            f"> To update: upload supported files to this folder and commit. The website sorts files alphabetically. {instructions}",
            ">",
            "> Delete this note after the site is finalized.",
            "",
        ]
    )

    output.write_text("\n".join(lines), encoding="utf-8")


def render_process_galleries() -> None:
    if not PROCESS_ROOT.exists():
        return
    for folder in sorted(path for path in PROCESS_ROOT.rglob("*") if path.is_dir()):
        render_gallery(folder, "root", "")
        render_gallery(folder, "child", "../")


def main() -> int:
    render_slot_refs()
    render_process_galleries()
    print(f"Generated slot references in {IMAGE_OUTPUT.relative_to(ROOT)}.")
    print(f"Generated slot notes in {SLOT_NOTES_ROOT.relative_to(ROOT)}.")
    print(f"Generated galleries in {GALLERIES_ROOT.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
