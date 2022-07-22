import json
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", page_title="Home")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/about")
def about():
    with open("data/dwarves.json", "r", encoding="utf-8") as json_data:
        dwarves_json_data = json.load(json_data)
    return render_template("about.html", page_title="About", dwarves=dwarves_json_data)


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
