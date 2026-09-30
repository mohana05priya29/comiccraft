import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def generate_comic_story(
    idea,
    genre="Adventure",
    character="Main Hero"
):
    """
    Generate a comic story using Gemini Flash.
    """

    prompt = f"""
You are an AI comic story creator for ComicCraft.

Create an original comic story using the details below.

Comic idea:
{idea}

Genre:
{genre}

Main character:
{character}

Create the story in this format:

TITLE:
Give the comic title.

CHARACTERS:
List the main characters.

PAGE 1:
Describe the scene and dialogue.

PAGE 2:
Describe the scene and dialogue.

PAGE 3:
Describe the scene and dialogue.

PAGE 4:
Describe the scene and dialogue.

ENDING:
Give a satisfying ending.

Keep the story creative, simple and suitable for a comic book.
Include short dialogues between characters.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as error:

        return f"Error generating comic story: {error}"


def generate_character(
    name,
    personality,
    power="None"
):
    """
    Generate a character description.
    """

    prompt = f"""
Create a comic book character for ComicCraft.

Character name:
{name}

Personality:
{personality}

Special power:
{power}

Give:

1. Character description
2. Appearance
3. Personality
4. Special ability
5. Strength
6. Weakness
7. Character role in the story
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as error:

        return f"Error generating character: {error}"


def generate_comic_panel(
    scene_description
):
    """
    Generate a detailed comic panel prompt.
    """

    prompt = f"""
Convert the following scene into a detailed
comic panel description.

Scene:
{scene_description}

Include:

- Characters
- Facial expressions
- Body actions
- Background
- Environment
- Camera angle
- Lighting
- Mood
- Dialogue

Make it suitable for an AI comic image generator.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as error:

        return f"Error generating panel: {error}"


# --------------------------------------------------
# TEST THE GEMINI CONNECTION
# --------------------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("        COMICCRAFT AI")
    print("=" * 50)

    print("\nGenerating comic story...\n")

    story = generate_comic_story(
        idea="A student discovers a mysterious robot in college.",
        genre="Science Fiction",
        character="Arun"
    )

    print(story)

    print("\n" + "=" * 50)
    print("ComicCraft generation completed!")
    print("=" * 50)
