# ComicCraft - main.py

import json

comic = {
    "title": "",
    "characters": [],
    "panels": []
}


def create_comic():
    title = input("Enter comic title: ").strip()

    if title:
        comic["title"] = title
        print(f"\nComic '{title}' created successfully!")
    else:
        print("Title cannot be empty.")


def add_character():
    name = input("Character name: ").strip()
    description = input("Character description: ").strip()

    if not name:
        print("Character name cannot be empty.")
        return

    character = {
        "name": name,
        "description": description
    }

    comic["characters"].append(character)
    print(f"\nCharacter '{name}' added!")


def add_panel():
    scene = input("Enter scene description: ").strip()
    dialogue = input("Enter dialogue: ").strip()

    if not scene:
        print("Scene description cannot be empty.")
        return

    panel = {
        "panel_number": len(comic["panels"]) + 1,
        "scene": scene,
        "dialogue": dialogue
    }

    comic["panels"].append(panel)
    print(f"\nPanel {panel['panel_number']} added!")


def view_comic():
    print("\n" + "=" * 50)
    print(f"COMIC: {comic['title'] or 'Untitled'}")
    print("=" * 50)

    print("\nCHARACTERS")
    print("-" * 50)

    if comic["characters"]:
        for character in comic["characters"]:
            print(f"Name: {character['name']}")
            print(f"Description: {character['description']}")
            print()
    else:
        print("No characters added yet.")

    print("\nPANELS")
    print("-" * 50)

    if comic["panels"]:
        for panel in comic["panels"]:
            print(f"\nPanel {panel['panel_number']}")
            print(f"Scene: {panel['scene']}")
            print(f"Dialogue: {panel['dialogue']}")
    else:
        print("No panels added yet.")

    print("=" * 50)


def save_comic():
    filename = input("Enter filename (example: my_comic.json): ").strip()

    if not filename:
        print("Filename cannot be empty.")
        return

    if not filename.endswith(".json"):
        filename += ".json"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(comic, file, indent=4)

        print(f"\nComic saved successfully as '{filename}'!")

    except OSError as error:
        print(f"Could not save comic: {error}")


def load_comic():
    filename = input("Enter comic filename: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            loaded_comic = json.load(file)

        comic.clear()
        comic.update(loaded_comic)

        print("\nComic loaded successfully!")

    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid comic file.")
    except OSError as error:
        print(f"Could not load comic: {error}")


def main():
    while True:
        print("\n")
        print("=" * 40)
        print("          🎨 COMICCRAFT")
        print("=" * 40)
        print("1. Create Comic")
        print("2. Add Character")
        print("3. Add Comic Panel")
        print("4. View Comic")
        print("5. Save Comic")
        print("6. Load Comic")
        print("7. Exit")
        print("=" * 40)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_comic()

        elif choice == "2":
            add_character()

        elif choice == "3":
            add_panel()

        elif choice == "4":
            view_comic()

        elif choice == "5":
            save_comic()

        elif choice == "6":
            load_comic()

        elif choice == "7":
            print("\nThanks for using ComicCraft! 👋")
            break

        else:
            print("\nInvalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
