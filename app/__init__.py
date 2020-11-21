import os
from threading import Thread

from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate

from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# modules initialization
Bootstrap(app)
Moment(app)
db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


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


def send_email_async(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template_name, **kwargs):
    msg = Message(subject, sender=app.config.get('MAIL_DEFAULT_SENDER'), recipients=[to])
    msg.body = render_template(f'{template_name}.txt', **kwargs)
    msg.html = render_template(f'{template_name}.html', **kwargs)
    thread = Thread(target=send_email_async, args=(app, msg))
    thread.start()


@app.shell_context_processor
def shell_context():
    return dict(User=User, db=db, mail=mail, send_email=send_email)


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/admin/', methods=['GET', 'POST'])
def admin():
    form = CreateUser()
    if form.validate_on_submit():
        flash(f"You've just created {form.data['name']}")
        new_user = User(
            username=form.data['name'],
            email=form.data['email'],
            password_hash=generate_password_hash(form.data['password1']),
        )
        db.session.add(new_user)
        db.session.commit()
        send_email(to=new_user.email, subject='Account created', template_name='email/new_user',
                   username=new_user.username)
        return redirect(url_for('index'))
    return render_template('admin.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500