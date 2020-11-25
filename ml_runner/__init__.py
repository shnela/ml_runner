import os
from flask import (
    flash,
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
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

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
Bootstrap(app)


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


@app.route('/')
def index():
    flash('index page')
    user_info = {
        'name': session.get('name', 'Unknown'),
        'age': session.get('age', 0),
    }
    return render_template('index.html', user_info=user_info)


@app.route('/bootstrap_play/')
def bootstrap_play():
    return render_template('bootstrap_play.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # show diff between GET and POST
    form = LoginForm()
    if form.validate_on_submit():
        flash('You were successfully logged in')
        session['name'] = form.name.data
        session['age'] = form.age.data
        return redirect(url_for('index'))
    return render_template('auth/login.html', form=form)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    flash('You were successfully logged out')
    if 'name' in session:
        del session['name']
    if 'name' in session:
        del session['age']
    return redirect(url_for('index'))


@app.route('/user/<name>/<amount>/')
def hello_from_kwargs(name, amount):
    amount = int(amount)
    return render_template('hello_from_kwargs.html', name=name, amount=amount)


if __name__ == '__main__':
    app.run()
