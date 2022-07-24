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
    data = []
    with open("data/dwarves.json", "r", encoding="utf-8") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", dwarves=data)


@app.route("/about/<dwarve_name>")
def about_dwarf(dwarve_name):
    with open("data/dwarves.json", "r", encoding="utf-8") as json_data:
        data = json.load(json_data)
        for member in data:
            if member["url"] == dwarve_name:
                # if url of member matches with a dwarve on the list, then 
                # let declare dwarve and let it = to member
                dwarve = member
                return "<h1>" + dwarve["name"] + "</h1>"
                # return render_template("about_dwarve.html", dwarve)


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
