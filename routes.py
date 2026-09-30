from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to ComicCraft AI Comic Story Creator!"


@app.route("/create-comic", methods=["POST"])
def create_comic():

    data = request.get_json()

    story = data.get("story", "")
    character = data.get("character", "")
    genre = data.get("genre", "")

    if story == "":
        return jsonify({
            "error": "Please enter a story"
        })

    comic = {
        "title": "My AI Comic",
        "story": story,
        "character": character,
        "genre": genre,
        "status": "Comic created successfully"
    }

    return jsonify(comic)


@app.route("/health")
def health():

    return jsonify({
        "status": "running",
        "project": "ComicCraft"
    })


if __name__ == "__main__":
    app.run(debug=True)
