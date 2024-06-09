from wtforms import Form, FileField, SubmitField, validators


class FileForm(Form):
    file = FileField(validators=[validators.data_required()])
    submit = SubmitField()
