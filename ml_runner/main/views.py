from flask import render_template

from . import bp
from ..models import User


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/users/')
def users_list():
    users = User.query.all()
    return render_template('users_list.html', users=users)


@bp.route('/users/<int:user_id>/')
def user_details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_details.html', user=user)


@bp.route('/posts/')
def posts_list():
    """Return posts here, remember about generating href to post_details"""
    pass


@bp.route('/posts/<int:post_id>/')
def post_details(post_id):
    """Return post here, remember about displaying both
    content and creation_date"""
    pass
