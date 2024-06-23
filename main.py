from flask import Flask, render_template, send_from_directory, request
from werkzeug.utils import secure_filename
from forms import FileForm, InputForm
from os import path, mkdir
from db import *


server = Flask(__name__)


@server.route("/", methods=("GET", "POST"))
def home():
    form = FileForm(meta={"csrf": False})
    if request.method == "POST" and form.validate_on_submit():
        filename = secure_filename(filename=form.file.data.filename)
        dates = date.today().strftime("%d %m")
        try:
            form.file.data.save(dst=f"static/sounds/{dates}/{filename}")

        except FileNotFoundError:
            mkdir(f"static/sounds/{dates}")
            mkdir(f"static/sounds/{dates}/edited")
            form.file.data.save(dst=f"static/sounds/{dates}/{filename}")

        temp = filename.split('.')
        return editor(add_sound('.'.join(temp[:-1]), temp[-1]))
    return render_template("index.html", form=form)


@server.route("/about")
def about():
    return render_template("about.html")


@server.route("/favicon.ico")
def favicon():
    return send_from_directory(path.join(server.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon")


@server.route("/editor/<int:sound_id>")
def editor(sound_id):
    info = get_info(sound_id)
    editor_input = InputForm(meta={"csrf": False})
    return render_template("editor.html", info=info, editor_input=editor_input)
