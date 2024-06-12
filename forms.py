from flask_wtf.file import FileField, FileRequired
from wtforms.fields.simple import SubmitField
from flask_wtf import FlaskForm


class FileForm(FlaskForm):
    file = FileField(validators=[FileRequired()])
    submit = SubmitField()
