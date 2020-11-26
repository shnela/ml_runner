from flask import render_template

from . import bp
from .. import db
from ..models import User, Post
from ..reflected_models import ReflectedUser, ReflectedPost


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/users/')
def users_list():
    users = User.query.all()
    # users = db.session.query(ReflectedUser).all()
    return render_template('users_list.html', users=users)


@bp.route('/users/<int:user_id>/')
def user_details(user_id):
    user = User.query.get_or_404(user_id)
    # user = db.session.query(ReflectedUser).get_or_404(user_id)
    return render_template('user_details.html', user=user)


@bp.route('/posts/')
def posts_list():
    posts = Post.query.all()
    # posts = db.session.query(ReflectedPost).all()
    return render_template('posts_list.html', posts=posts)


@bp.route('/posts/<int:post_id>/')
def post_details(post_id):
    post = Post.query.get_or_404(post_id)
    # post = db.session.query(ReflectedPost).get_or_404(post_id)
    return render_template('post_details.html', post=post)
