from flask import (
    current_app,
    flash,
    request,
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
    page = int(request.values.get('page', 1))
    users_paginator = User.query.paginate(
        page=page, per_page=current_app.config['PER_PAGE']
    )
    return render_template('users_list.html', users_paginator=users_paginator)


@bp.route('/users/<int:user_id>/')
def user_details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_details.html', user=user)


@bp.route('/user/<name>/<amount>/')
def hello_from_kwargs(name, amount):
    amount = int(amount)
    return render_template('hello_from_kwargs.html', name=name, amount=amount)
