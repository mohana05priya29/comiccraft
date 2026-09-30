import os
from dotenv import load_dotenv
from google import genai

# ============================================================
# COMICCRAFT - GEMINI PRO
# ============================================================

# Load .env file
load_dotenv()

# Get API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please add it to your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=API_KEY)


# ============================================================
# GENERATE DETAILED COMIC STORY
# ============================================================

def generate_detailed_story(
    idea,
    genre="Adventure",
    main_character="Hero",
    number_of_pages=6
):
    """
    Generate a detailed comic story.
    """

    prompt = f"""
You are an expert comic book writer for ComicCraft.

Create an original and engaging comic story.

COMIC IDEA:
{idea}

GENRE:
{genre}

MAIN CHARACTER:
{main_character}

NUMBER OF PAGES:
{number_of_pages}

Create the story using this structure:

TITLE:
Give a creative comic title.

CHARACTERS:
List all important characters.

CHARACTER DETAILS:
Describe their personality and role.

STORY:
Write the complete story.

PAGE BREAKDOWN:

PAGE 1:
Scene description
Characters
Actions
Dialogue

PAGE 2:
Scene description
Characters
Actions
Dialogue

PAGE 3:
Scene description
Characters
Actions
Dialogue

PAGE 4:
Scene description
Characters
Actions
Dialogue

PAGE 5:
Scene description
Characters
Actions
Dialogue

PAGE 6:
Scene description
Characters
Actions
Dialogue

ENDING:
Give the story a meaningful ending.

Make the story creative, easy to understand,
and suitable for a comic book.
Keep dialogues short and natural.
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )

        return response.text

    except Exception as error:

        return f"Story generation failed: {error}"


# ============================================================
# GENERATE CHARACTER
# ============================================================

def generate_character(
    name,
    personality,
    role="Main Character",
    special_power="None"
):
    """
    Generate a detailed comic character.
    """

    prompt = f"""
Create a detailed comic book character.

NAME:
{name}

PERSONALITY:
{personality}

ROLE:
{role}

SPECIAL POWER:
{special_power}

Give the following:

1. Character description
2. Physical appearance
3. Personality
4. Special abilities
5. Strengths
6. Weaknesses
7. Character goal
8. Character role in the story
9. Dialogue style
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )

        return response.text

    except Exception as error:

        return f"Character generation failed: {error}"


# ============================================================
# GENERATE SCENE
# ============================================================

def generate_scene(
    scene_description,
    characters
):
    """
    Generate a detailed comic scene.
    """

    prompt = f"""
Create a detailed comic scene.

SCENE:
{scene_description}

CHARACTERS:
{characters}

Describe:

1. Location
2. Background
3. Characters
4. Facial expressions
5. Body movements
6. Actions
7. Emotions
8. Dialogue
9. Camera angle
10. Lighting
11. Mood

Write the scene in a format useful for
comic creation.
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )

        return response.text

    except Exception as error:

        return f"Scene generation failed: {error}"


# ============================================================
# GENERATE DIALOGUE
# ============================================================

def generate_dialogue(
    situation,
    characters
):
    """
    Generate character dialogue.
    """

    prompt = f"""
Write natural comic-book dialogue.

SITUATION:
{situation}

CHARACTERS:
{characters}

Rules:

- Keep dialogue short.
- Make each character sound different.
- Show emotions through dialogue.
- Make the conversation interesting.
- Do not make dialogue unnecessarily long.
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )

        return response.text

    except Exception as error:

        return f"Dialogue generation failed: {error}"


# ============================================================
# GENERATE COMIC PANEL
# ============================================================

def generate_panel_prompt(
    scene,
    characters
):
    """
    Create a prompt for a comic image panel.
    """

    prompt = f"""
Create a detailed AI image prompt for a comic panel.

SCENE:
{scene}

CHARACTERS:
{characters}

Include:

- Character appearance
- Character position
- Facial expressions
- Body pose
- Background
- Environment
- Camera angle
- Lighting
- Mood
- Comic style
- Important objects

The output should be suitable for
an AI image generation system.
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )

        return response.text

    except Exception as error:

        return f"Panel generation failed: {error}"


# ============================================================
# IMPROVE EXISTING STORY
# ============================================================

def improve_story(story):
    """
    Improve an existing comic story.
    """

    prompt = f"""
Improve the following comic story.

STORY:
{story}

Improve:

- Story flow
- Character development
- Dialogue
- Suspense
- Emotions
- Ending

Keep the original idea.
Do not completely change the story.
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )

        return response.text

    except Exception as error:

        return f"Story improvement failed: {error}"


# ============================================================
# TEST COMICCRAFT
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("              COMICCRAFT")
    print("          GEMINI PRO ENGINE")
    print("=" * 60)

    print("\nGenerating comic story...\n")

    story = generate_detailed_story(
        idea="A college student discovers a mysterious robot.",
        genre="Science Fiction",
        main_character="Arun",
        number_of_pages=6
    )

    print(story)

    print("\n" + "=" * 60)
    print("ComicCraft story generation completed!")
    print("=" * 60)
