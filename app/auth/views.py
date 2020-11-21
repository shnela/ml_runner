from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, login_required
from werkzeug.security import generate_password_hash

from . import bp
from .forms import CreateUser, LoginForm
from .models import User
from .. import db
from ..utils import send_email


@bp.route('/admin/', methods=['GET', 'POST'])
@login_required
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
        return redirect(url_for('main.index'))
    return render_template('admin.html', form=form)


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.data['name']).first()
        login_user(user)

        flash('Logged in successfully.')

        next = request.args.get('next')
        # # is_safe_url should check if the url is safe for redirects.
        # # See http://flask.pocoo.org/snippets/62/ for an example.
        # if not is_safe_url(next):
        #     return flask.abort(400)

        return redirect(next or url_for('main.index'))
    return render_template('auth/login.html', form=form)

