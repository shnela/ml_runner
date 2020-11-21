from flask import render_template

from app.auth.models import User
from . import bp


@bp.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)
