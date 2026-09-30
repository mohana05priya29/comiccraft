# layout_builder.py

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os
import math


# ============================================================
# COMICCRAFT - LAYOUT BUILDER
# ============================================================

# Folder containing generated panel images
INPUT_FOLDER = Path("generated_images")

# Folder for final comic pages
OUTPUT_FOLDER = Path("comic_pages")

OUTPUT_FOLDER.mkdir(exist_ok=True)


# ============================================================
# DEFAULT SETTINGS
# ============================================================

PAGE_WIDTH = 1600
PAGE_HEIGHT = 2200

MARGIN = 60
GAP = 30

BACKGROUND_COLOR = "white"
BORDER_WIDTH = 8


# ============================================================
# LOAD FONT
# ============================================================

def load_font(size=50):

    possible_fonts = [
        "arial.ttf",
        "Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    ]

    for font in possible_fonts:

        if os.path.exists(font):
            return ImageFont.truetype(font, size)

    return ImageFont.load_default()


# ============================================================
# LOAD PANEL IMAGE
# ============================================================

def load_panel(path):

    try:

        image = Image.open(path).convert("RGB")

        return image

    except Exception as error:

        print(f"Could not load {path}: {error}")

        return None


# ============================================================
# RESIZE IMAGE
# ============================================================

def resize_panel(image, width, height):

    return image.resize(
        (width, height),
        Image.Resampling.LANCZOS
    )


# ============================================================
# ADD BORDER
# ============================================================

def add_border(
    draw,
    x,
    y,
    width,
    height
):

    draw.rectangle(
        [
            x,
            y,
            x + width,
            y + height
        ],
        outline="black",
        width=BORDER_WIDTH
    )


# ============================================================
# CREATE TWO COLUMN LAYOUT
# ============================================================

def create_two_column_layout(
    panel_paths,
    output_file="comic_page.png"
):

    page = Image.new(
        "RGB",
        (PAGE_WIDTH, PAGE_HEIGHT),
        BACKGROUND_COLOR
    )

    draw = ImageDraw.Draw(page)

    available_width = (
        PAGE_WIDTH
        - (2 * MARGIN)
        - GAP
    )

    panel_width = available_width // 2

    panel_height = (
        PAGE_HEIGHT
        - (2 * MARGIN)
        - GAP
    ) // 2

    positions = [
        (MARGIN, MARGIN),
        (MARGIN + panel_width + GAP, MARGIN),
        (MARGIN, MARGIN + panel_height + GAP),
        (
            MARGIN + panel_width + GAP,
            MARGIN + panel_height + GAP
        )
    ]

    for index, path in enumerate(panel_paths[:4]):

        image = load_panel(path)

        if image is None:
            continue

        image = resize_panel(
            image,
            panel_width,
            panel_height
        )

        x, y = positions[index]

        page.paste(
            image,
            (x, y)
        )

        add_border(
            draw,
            x,
            y,
            panel_width,
            panel_height
        )

    output_path = OUTPUT_FOLDER / output_file

    page.save(
        output_path,
        quality=95
    )

    return str(output_path)


# ============================================================
# CREATE THREE ROW LAYOUT
# ============================================================

def create_three_row_layout(
    panel_paths,
    output_file="comic_page_3.png"
):

    page = Image.new(
        "RGB",
        (PAGE_WIDTH, PAGE_HEIGHT),
        BACKGROUND_COLOR
    )

    draw = ImageDraw.Draw(page)

    panel_width = (
        PAGE_WIDTH - (2 * MARGIN)
    )

    panel_height = (
        PAGE_HEIGHT
        - (2 * MARGIN)
        - (2 * GAP)
    ) // 3

    y_position = MARGIN

    for index, path in enumerate(panel_paths[:3]):

        image = load_panel(path)

        if image is None:
            continue

        image = resize_panel(
            image,
            panel_width,
            panel_height
        )

        page.paste(
            image,
            (MARGIN, y_position)
        )

        add_border(
            draw,
            MARGIN,
            y_position,
            panel_width,
            panel_height
        )

        y_position += (
            panel_height + GAP
        )

    output_path = OUTPUT_FOLDER / output_file

    page.save(
        output_path,
        quality=95
    )

    return str(output_path)


# ============================================================
# CREATE COMIC TITLE
# ============================================================

def add_title(
    image,
    title
):

    draw = ImageDraw.Draw(image)

    font = load_font(70)

    text_box = draw.textbbox(
        (0, 0),
        title,
        font=font
    )

    text_width = (
        text_box[2] - text_box[0]
    )

    x = (
        image.width - text_width
    ) // 2

    draw.text(
        (x, 20),
        title,
        fill="black",
        font=font
    )

    return image


# ============================================================
# ADD SPEECH BUBBLE
# ============================================================

def add_speech_bubble(
    image,
    text,
    position,
    size=(400, 150)
):

    draw = ImageDraw.Draw(image)

    x, y = position

    width, height = size

    draw.rounded_rectangle(
        [
            x,
            y,
            x + width,
            y + height
        ],
        radius=30,
        fill="white",
        outline="black",
        width=5
    )

    font = load_font(30)

    draw.text(
        (
            x + 20,
            y + 20
        ),
        text,
        fill="black",
        font=font
    )

    return image


# ============================================================
# CREATE CUSTOM COMIC PAGE
# ============================================================

def build_comic_page(
    panel_paths,
    title="ComicCraft"
):

    if len(panel_paths) == 0:

        raise ValueError(
            "No comic panels were provided."
        )

    if len(panel_paths) <= 3:

        output = create_three_row_layout(
            panel_paths,
            "final_comic.png"
        )

    else:

        output = create_two_column_layout(
            panel_paths,
            "final_comic.png"
        )

    image = Image.open(output)

    image = add_title(
        image,
        title
    )

    image.save(output)

    return output


# ============================================================
# CREATE MULTIPLE COMIC PAGES
# ============================================================

def build_multiple_pages(
    panel_paths,
    panels_per_page=4
):

    pages = []

    total_panels = len(panel_paths)

    page_number = 1

    for start in range(
        0,
        total_panels,
        panels_per_page
    ):

        current_panels = panel_paths[
            start:start + panels_per_page
        ]

        output_name = (
            f"comic_page_{page_number}.png"
        )

        if len(current_panels) <= 3:

            output = create_three_row_layout(
                current_panels,
                output_name
            )

        else:

            output = create_two_column_layout(
                current_panels,
                output_name
            )

        pages.append(output)

        page_number += 1

    return pages


# ============================================================
# FIND GENERATED PANELS
# ============================================================

def find_panels():

    if not INPUT_FOLDER.exists():

        print(
            "generated_images folder not found."
        )

        return []

    panels = []

    for file in INPUT_FOLDER.iterdir():

        if file.suffix.lower() in [
            ".png",
            ".jpg",
            ".jpeg"
        ]:

            panels.append(file)

    panels.sort()

    return panels


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("              COMICCRAFT")
    print("             LAYOUT BUILDER")
    print("=" * 60)

    panels = find_panels()

    if not panels:

        print(
            "\nNo panel images found!"
        )

        print(
            "Generate images first using image_generator.py"
        )

    else:

        print(
            f"\nFound {len(panels)} panel(s)."
        )

        print(
            "\nBuilding comic pages..."
        )

        pages = build_multiple_pages(
            panels,
            panels_per_page=4
        )

        print(
            "\nComic pages created successfully!"
        )

        for page in pages:

            print(
                f"Created: {page}"
            )

    print("\n" + "=" * 60)
    print("Layout building completed!")
    print("=" * 60)
