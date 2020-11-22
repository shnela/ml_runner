from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired


class CreateMLModelForm(FlaskForm):
    model_name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description')
    pickled_model = FileField(validators=[DataRequired()])
    submit = SubmitField('Submit')


class UploadCSVForm(FlaskForm):
    csv_file = FileField(validators=[DataRequired()])
    submit = SubmitField('Submit')
