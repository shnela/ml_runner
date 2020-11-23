import os

from flask import (
    Flask,
    abort,
    flash,
    render_template,
    request,
    redirect,
    url_for,
    session
)
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError


current_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(current_dir, 'test.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit')



@app.route('/')
def index():
    user_info = {
        'name': session.get('name', 'Unknown'),
        'age': session.get('age', 0),
    }
    return render_template('index.html', user_info=user_info)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # show diff between GET and POST
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['age'] = form.age.data
        flash(f"You've logged in as {session['name']}({session['age']})")
        return redirect(url_for('index'))
    return render_template('auth/login.html', form=form)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if 'name' in session:
        del session['name']
    if 'age' in session:
        del session['age']
    flash("You've logged out", category='warning')
    return redirect(url_for('index'))


@app.route('/user/<name>/<amount>/')
def hello_from_kwargs(name, amount):
    amount = int(amount)
    return render_template('hello_from_kwargs.html', name=name, amount=amount)


@app.route('/return_error/<int:response_code>/')
def return_response_with_code(response_code):
    return f'Return {response_code}', response_code


@app.route('/abort_error/<int:response_code>/')
def abort_response_with_code(response_code):
    abort(response_code)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    app.run()
