from flask import render_template
from flask_login import login_required

from app.auth.models import User
from . import bp


@bp.route('/')
@login_required
def index():
    users = User.query.all()
    return render_template('index.html', users=users)
