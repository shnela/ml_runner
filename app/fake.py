import os
from datetime import datetime

from faker import Faker
from flask import current_app
from werkzeug.security import generate_password_hash

from . import db
from .auth.models import User
from .ml_models.models import MLModel, MLModelRun

fake = Faker()


def save_test_file(filename, output_dir_key):
    in_file = os.path.join(current_app.config['FAKE_DIR'], filename)
    out_filename = f'{datetime.now().isoformat()}_{filename}'
    out_file = os.path.join(current_app.config[output_dir_key], out_filename)
    with open(in_file, 'rb') as f_in:
        with open(out_file, 'wb') as f_out:
            f_out.write(f_in.read())
    return out_filename


def generate_users(count=10):
    for i in range(count):
        u = User(
            username=fake.first_name(),
            email=fake.email(),
            password_hash=generate_password_hash('a'),
        )
        db.session.add(u)
    db.session.commit()


def generate_ml_models(models_count=1, runs_count=0):
    for i in range(models_count):
        model_name = f'{fake.unique.name()} model'
        u = MLModel(
            model_name=model_name,
            description=fake.text(),
            pickle_filename=f"/some/path/{model_name.replace(' ', '_')}",
        )
        db.session.add(u)
        db.session.commit()
        generate_ml_model_runs(u.id, runs_count)


def generate_ml_model_runs(ml_model_id, runs_count=10):
    for i in range(runs_count):
        model_name = f'{fake.unique.name()} model'
        u = MLModelRun(
            description=fake.text(),
            csv_filename=f"/some/path/{model_name.replace(' ', '_')}",
            ml_model_id=ml_model_id,
        )
        db.session.add(u)
    db.session.commit()
