from faker import Faker
from werkzeug.security import generate_password_hash

from . import db
from .auth.models import User
from .ml_models.models import MLModel, MLModelRun

fake = Faker()


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
