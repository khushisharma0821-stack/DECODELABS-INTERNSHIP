from flask import Flask, render_template, request, send_from_directory, Response
import os
from utils import extract_text

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():

    confidence = 0
    extracted_text = ""
    image_name = None

    if request.method == "POST":

        image = request.files["image"]

        if image.filename != "":

            image_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)

            image.save(image_path)

            extracted_text, confidence = extract_text(image_path)

            image_name = image.filename

    return render_template(
        "index.html",
        text=extracted_text,
        image_name=image_name,
        confidence=confidence
    )


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/download")
def download():

    text = request.args.get("text", "")

    return Response(
        text,
        mimetype="text/plain",
        headers={
            "Content-Disposition": "attachment; filename=Extracted_Text.txt"
        }
    )


if __name__ == "__main__":
    app.run(debug=True)