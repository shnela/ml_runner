from flask import (
    flash,
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from . import bp
from .forms import LoginForm


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    # show diff between GET and POST
    form = LoginForm()
    if form.validate_on_submit():
        flash('You were successfully logged in')
        session['name'] = form.name.data
        session['age'] = form.age.data
        return redirect(url_for('index'))
    return render_template('auth/login.html', form=form)


@bp.route('/logout/', methods=['GET', 'POST'])
def logout():
    flash('You were successfully logged out')
    if 'name' in session:
        del session['name']
    if 'name' in session:
        del session['age']
    return redirect(url_for('main.index'))
