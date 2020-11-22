import os
from datetime import datetime

from flask import render_template, url_for, current_app, send_from_directory, session
from flask_login import login_required
from werkzeug.utils import secure_filename, redirect

from . import bp
from .forms import CreateMLModelForm, UploadCSVForm
from .models import MLModel
from .. import db


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
        filename = secure_filename(f'{datetime.now().isoformat()}_{f.filename}')
        f.save(os.path.join(
            current_app.config['ML_MODELS_DIR'], filename
        ))
        new_model = MLModel(
            model_name=form.data['model_name'],
            description=form.data.get('description'),
            pickle_filename=filename,
        )
        db.session.add(new_model)
        db.session.commit()
        return redirect(url_for('.models_list'))

    return render_template('ml_models/model_create.html', form=form)


@bp.route('/models/<int:model_id>/')
@login_required
def model_details(model_id):
    ml_model = MLModel.query.get_or_404(model_id)
    return render_template('ml_models/model_details.html', model=ml_model)


@bp.route('/models/<int:model_id>/download/')
@login_required
def model_download(model_id):
    ml_model = MLModel.query.get(model_id)
    return send_from_directory(current_app.config['ML_MODELS_DIR'], ml_model.pickle_filename)


@bp.route('/csv/display/', methods=['GET', 'POST'])
@login_required
def csv_display():
    """GET: renders form for uploading CSV and displays recently uploaded file
    POST: submits new CSV file and saves it on server, file path is stored in session"""
    form = UploadCSVForm()
    if form.validate_on_submit():
        f = form.csv_file.data
        filename = secure_filename(f'{datetime.now().isoformat()}_{f.filename}')
        f.save(os.path.join(
            current_app.config['CSV_DIR'], filename
        ))
        session['uploaded_csv'] = filename
        return redirect(url_for('.csv_display'))
    recent_csv_file = session.get('uploaded_csv')
    return render_template('ml_models/csv_display.html', form=form, recent_csv_file=recent_csv_file)
