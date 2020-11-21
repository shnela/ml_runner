import os

from flask import render_template, url_for, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename, redirect

from . import bp
from .forms import CreateMLModelForm
from .models import MLModel


@bp.route('/models/')
@login_required
def models_list():
    models = MLModel.query.all()
    return render_template('ml_models/models_list.html', models=models)


@bp.route('/models/create/', methods=['GET', 'POST'])
@login_required
def model_create():
    form = CreateMLModelForm()
    if form.validate_on_submit():
        f = form.pickled_model.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            current_app.instance_path, 'pickled_ml_models', filename
        ))
        return redirect(url_for('.models_list'))

    return render_template('ml_models/model_create.html', form=form)
