from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class CreateMLModelForm(FlaskForm):
    pickled_model = FileField(validators=[DataRequired()])
    submit = SubmitField('Submit')
