from flask import render_template
from flask_login import login_required

from . import bp
from .models import MLModel


@bp.route('/models/')
@login_required
def models_list():
    models = MLModel.query.all()
    return render_template('ml_models/models_list.html', models=models)
