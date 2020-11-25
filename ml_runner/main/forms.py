from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    SubmitField,
    PasswordField
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    NumberRange,
    ValidationError,
)


class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired(), NumberRange(min=0)])
    # email = StringField('email', validators=[DataRequired(), Email()])
    # password = PasswordField('password', validators=[DataRequired()])
    # password2 = PasswordField('password2', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        if field.data and field.data.lower() == 'admin':
            raise ValidationError("You can't log in as admin")
