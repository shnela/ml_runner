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


def generate_ml_models(count=1):
    for i in range(count):
        model_name = f'{fake.name()} model'
        u = MLModel(
            model_name=model_name,
            description=fake.text(),
            pickle_filename=f"/some/path/{model_name.replace(' ', '_')}",
        )
        db.session.add(u)
    db.session.commit()


def generate_ml_model_runs(ml_model_id, count=10):
    for i in range(count):
        model_name = f'{fake.name()} model'
        u = MLModelRun(
            description=fake.text(),
            csv_filename=f"/some/path/{model_name.replace(' ', '_')}",
            ml_model_id=ml_model_id,
        )
        db.session.add(u)
    db.session.commit()
