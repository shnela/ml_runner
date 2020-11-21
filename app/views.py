from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from app import db, app
from app.forms import CreateUser
from app.models import User
from app.utils import send_email


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
