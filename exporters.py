# exporters.py

import json
import os
import shutil
from pathlib import Path
from datetime import datetime

from PIL import Image


# ============================================================
# COMICCRAFT - EXPORTERS
# ============================================================

EXPORT_FOLDER = Path("exports")
EXPORT_FOLDER.mkdir(exist_ok=True)


# ============================================================
# CREATE EXPORT FOLDER
# ============================================================

def create_export_folder(folder_name="comic_export"):

    folder = EXPORT_FOLDER / folder_name

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    return folder


# ============================================================
# EXPORT COMIC AS PNG
# ============================================================

def export_png(
    image_path,
    output_name="comic.png"
):

    try:

        image_path = Path(image_path)

        if not image_path.exists():

            return {
                "success": False,
                "message": "Image file not found."
            }

        output_folder = create_export_folder()

        output_path = (
            output_folder / output_name
        )

        image = Image.open(
            image_path
        ).convert("RGB")

        image.save(
            output_path,
            format="PNG"
        )

        return {
            "success": True,
            "format": "PNG",
            "file": str(output_path),
            "message": "Comic exported as PNG successfully."
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }


# ============================================================
# EXPORT COMIC AS JPEG
# ============================================================

def export_jpeg(
    image_path,
    output_name="comic.jpg"
):

    try:

        image_path = Path(image_path)

        if not image_path.exists():

            return {
                "success": False,
                "message": "Image file not found."
            }

        output_folder = create_export_folder()

        output_path = (
            output_folder / output_name
        )

        image = Image.open(
            image_path
        ).convert("RGB")

        image.save(
            output_path,
            format="JPEG",
            quality=95
        )

        return {
            "success": True,
            "format": "JPEG",
            "file": str(output_path),
            "message": "Comic exported as JPEG successfully."
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }


# ============================================================
# EXPORT COMIC AS PDF
# ============================================================

def export_pdf(
    image_paths,
    output_name="comic_book.pdf"
):

    try:

        if not image_paths:

            return {
                "success": False,
                "message": "No comic pages found."
            }

        images = []

        for path in image_paths:

            path = Path(path)

            if not path.exists():

                continue

            image = Image.open(
                path
            ).convert("RGB")

            images.append(image)

        if not images:

            return {
                "success": False,
                "message": "No valid images found."
            }

        output_folder = create_export_folder()

        output_path = (
            output_folder / output_name
        )

        first_image = images[0]

        remaining_images = images[1:]

        first_image.save(
            output_path,
            format="PDF",
            save_all=True,
            append_images=remaining_images,
            resolution=100.0
        )

        return {
            "success": True,
            "format": "PDF",
            "file": str(output_path),
            "pages": len(images),
            "message": "Comic exported as PDF successfully."
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }


# ============================================================
# EXPORT STORY AS JSON
# ============================================================

def export_json(
    comic_data,
    output_name="comic_data.json"
):

    try:

        output_folder = create_export_folder()

        output_path = (
            output_folder / output_name
        )

        data = {
            "project": "ComicCraft",
            "exported_at": datetime.now().isoformat(),
            "comic": comic_data
        }

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        return {
            "success": True,
            "format": "JSON",
            "file": str(output_path),
            "message": "Comic data exported successfully."
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }


# ============================================================
# EXPORT STORY AS TEXT
# ============================================================

def export_text(
    story,
    output_name="comic_story.txt"
):

    try:

        output_folder = create_export_folder()

        output_path = (
            output_folder / output_name
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(story)

        return {
            "success": True,
            "format": "TXT",
            "file": str(output_path),
            "message": "Comic story exported successfully."
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }


# ============================================================
# COPY COMPLETE COMIC PROJECT
# ============================================================

def export_project(
    source_folder,
    project_name="comic_project"
):

    try:

        source = Path(source_folder)

        if not source.exists():

            return {
                "success": False,
                "message": "Source folder not found."
            }

        destination = (
            EXPORT_FOLDER / project_name
        )

        if destination.exists():

            shutil.rmtree(destination)

        shutil.copytree(
            source,
            destination
        )

        return {
            "success": True,
            "folder": str(destination),
            "message": "Comic project exported successfully."
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }


# ============================================================
# GET EXPORT INFORMATION
# ============================================================

def get_export_info(
    file_path
):

    try:

        path = Path(file_path)

        if not path.exists():

            return {
                "success": False,
                "message": "File not found."
            }

        size = path.stat().st_size

        return {
            "success": True,
            "file_name": path.name,
            "file_type": path.suffix,
            "file_size_bytes": size,
            "file_size_kb": round(
                size / 1024,
                2
            ),
            "location": str(path)
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }


# ============================================================
# LIST EXPORTED FILES
# ============================================================

def list_exports():

    try:

        files = []

        if not EXPORT_FOLDER.exists():

            return files

        for file in EXPORT_FOLDER.rglob("*"):

            if file.is_file():

                files.append({
                    "name": file.name,
                    "path": str(file),
                    "type": file.suffix,
                    "size_kb": round(
                        file.stat().st_size / 1024,
                        2
                    )
                })

        return files

    except Exception as error:

        print(
            f"Error listing exports: {error}"
        )

        return []


# ============================================================
# DELETE EXPORTED FILE
# ============================================================

def delete_export(
    file_path
):

    try:

        path = Path(file_path)

        if not path.exists():

            return {
                "success": False,
                "message": "File not found."
            }

        if path.is_file():

            path.unlink()

        elif path.is_dir():

            shutil.rmtree(path)

        return {
            "success": True,
            "message": "Export deleted successfully."
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }


# ============================================================
# COMPLETE EXPORT
# ============================================================

def export_complete_comic(
    comic_data,
    story,
    page_images,
    final_image=None
):

    results = {}

    # Export JSON
    results["json"] = export_json(
        comic_data,
        "comic_data.json"
    )

    # Export story
    results["text"] = export_text(
        story,
        "comic_story.txt"
    )

    # Export PDF
    if page_images:

        results["pdf"] = export_pdf(
            page_images,
            "comic_book.pdf"
        )

    # Export final PNG
    if final_image:

        results["png"] = export_png(
            final_image,
            "comic.png"
        )

    return results


# ============================================================
# TEST EXPORTER
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("              COMICCRAFT")
    print("               EXPORTER")
    print("=" * 60)

    sample_comic = {
        "title": "The Mystery Robot",
        "genre": "Science Fiction",
        "character": "Arun",
        "pages": 4
    }

    sample_story = """
    Arun discovers a mysterious robot
    inside an abandoned laboratory.
    The robot becomes his new friend
    and helps him solve a mystery.
    """

    print("\nExporting comic data...")

    json_result = export_json(
        sample_comic
    )

    print(json_result["message"])

    print("\nExporting story...")

    text_result = export_text(
        sample_story
    )

    print(text_result["message"])

    print("\nAvailable exports:")

    files = list_exports()

    for file in files:

        print(
            f"- {file['name']} "
            f"({file['size_kb']} KB)"
        )

    print("\n" + "=" * 60)
    print("Export process completed!")
    print("=" * 60)
