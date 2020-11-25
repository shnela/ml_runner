from flask import (
    flash,
    render_template,
    session
)

from . import bp
from ..models import User


@bp.route('/')
def index():
    flash('index page')
    user_info = {
        'name': session.get('name', 'Unknown'),
        'age': session.get('age', 0),
    }
    return render_template('index.html', user_info=user_info)


@bp.route('/users/')
def users_list():
    users = User.query.all()
    return render_template('users_list.html', users=users)


@bp.route('/users/<int:user_id>/')
def user_details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_details.html', user=user)


@bp.route('/user/<name>/<amount>/')
def hello_from_kwargs(name, amount):
    amount = int(amount)
    return render_template('hello_from_kwargs.html', name=name, amount=amount)
