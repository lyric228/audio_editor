from flask_wtf.file import FileField, FileRequired
from wtforms.fields.simple import SubmitField
from wtforms.fields import IntegerField
from flask_wtf import FlaskForm


class FileForm(FlaskForm):
    file = FileField(validators=[FileRequired()])
    submit = SubmitField()


class InputForm(FlaskForm):
    input_start = IntegerField()
    input_end = IntegerField()
    submit = SubmitField()
