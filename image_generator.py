# image_generator.py

import os
import uuid
from pathlib import Path

from dotenv import load_dotenv
from google import genai


# ============================================================
# COMICCRAFT - IMAGE GENERATOR
# ============================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please add GEMINI_API_KEY to your .env file."
    )


# Create Gemini client
client = genai.Client(api_key=API_KEY)


# Folder where generated images will be saved
OUTPUT_FOLDER = Path("generated_images")
OUTPUT_FOLDER.mkdir(exist_ok=True)


# ============================================================
# CREATE COMIC IMAGE PROMPT
# ============================================================

def create_image_prompt(
    scene,
    characters,
    style="modern comic book"
):
    """
    Create a detailed prompt for a comic image.
    """

    prompt = f"""
Create a high-quality comic-book illustration.

SCENE:
{scene}

CHARACTERS:
{characters}

ART STYLE:
{style}

Include:

- Clear character appearance
- Character expressions
- Character poses
- Background
- Environment
- Important objects
- Camera angle
- Lighting
- Mood
- Comic-book composition

Keep the characters visually consistent.
Make the scene suitable for a comic story.
"""

    return prompt.strip()


# ============================================================
# GENERATE IMAGE
# ============================================================

def generate_image(
    prompt,
    filename=None
):
    """
    Generate an image using the configured Gemini image model.
    """

    try:

        if filename is None:
            filename = f"comic_{uuid.uuid4().hex[:8]}.png"

        output_path = OUTPUT_FOLDER / filename

        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=prompt
        )

        # Find generated image data
        for part in response.parts:

            if part.inline_data is not None:

                image = part.as_image()

                image.save(output_path)

                return {
                    "success": True,
                    "message": "Comic image generated successfully!",
                    "file": str(output_path)
                }

        return {
            "success": False,
            "message": "No image was returned by the model."
        }

    except Exception as error:

        return {
            "success": False,
            "message": f"Image generation failed: {error}"
        }


# ============================================================
# GENERATE COMIC PANEL
# ============================================================

def generate_comic_panel(
    scene,
    characters,
    panel_number=1
):
    """
    Generate one comic panel.
    """

    prompt = create_image_prompt(
        scene=scene,
        characters=characters,
        style="colorful modern comic book"
    )

    filename = f"panel_{panel_number}.png"

    return generate_image(
        prompt,
        filename
    )


# ============================================================
# GENERATE MULTIPLE PANELS
# ============================================================

def generate_comic_pages(
    scenes,
    characters
):
    """
    Generate multiple comic panels.
    """

    results = []

    for index, scene in enumerate(scenes, start=1):

        result = generate_comic_panel(
            scene=scene,
            characters=characters,
            panel_number=index
        )

        results.append(result)

    return results


# ============================================================
# TEST IMAGE GENERATOR
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("              COMICCRAFT")
    print("             IMAGE GENERATOR")
    print("=" * 60)

    scene = """
    A college student discovers a mysterious robot
    inside an old abandoned laboratory.
    The robot suddenly wakes up and looks at the student.
    """

    characters = """
    Arun - a curious college student wearing a blue shirt.
    Robo-X - a small friendly futuristic robot with glowing eyes.
    """

    print("\nGenerating comic panel...\n")

    result = generate_comic_panel(
        scene=scene,
        characters=characters,
        panel_number=1
    )

    if result["success"]:

        print("SUCCESS!")
        print("Image saved at:")
        print(result["file"])

    else:

        print("ERROR!")
        print(result["message"])

    print("\n" + "=" * 60)
    print("ComicCraft image generation finished!")
    print("=" * 60)
