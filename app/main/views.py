from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from . import bp
from .forms import CreateUser
from .models import User
from .. import db
from ..utils import send_email


@bp.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@bp.route('/admin/', methods=['GET', 'POST'])
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
