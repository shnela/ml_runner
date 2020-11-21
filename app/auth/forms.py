from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

from .models import User


class CreateUser(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password1 = PasswordField('password', validators=[DataRequired(), EqualTo('password2', 'Passwords must match')])
    password2 = PasswordField('repeat password', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Field name should be unique')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Field email should be unique')
