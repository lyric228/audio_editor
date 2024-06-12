from flask import Flask, render_template, send_from_directory, request, url_for, redirect
from werkzeug.utils import secure_filename
from forms import FileForm
from os import path


server = Flask(__name__)


@server.route("/", methods=("GET", "POST"))
def home():
    form = FileForm(meta={"csrf": False})
    if request.method == "POST" and form.validate_on_submit():
        filename = secure_filename(filename=form.file.data.filename)
        form.file.data.save(dst=filename)
        return redirect(url_for("home"))

    return render_template("index.html", form=form)


@server.route("/about")
def about():
    return render_template("about.html")


@server.route("/favicon.ico")
def favicon():
    return send_from_directory(path.join(server.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon")
