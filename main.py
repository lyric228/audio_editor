from flask import Flask, render_template, send_from_directory, request
from werkzeug.utils import secure_filename
from forms import FileForm
from os import path


server = Flask(__name__)


@server.route("/", methods=("GET", "POST"))
def home():
    form = FileForm()
    if request.method == "POST" and form.validate():
        # print(secure_filename(filename=form.file.data))
        print(form.file.data)

    return render_template("index.html", form=form)


@server.route("/about")
def about():
    return render_template("about.html")


@server.route("/favicon.ico")
def favicon():
    return send_from_directory(path.join(server.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon")
