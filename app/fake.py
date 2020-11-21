from faker import Faker

from . import db
from .auth.models import User
from .ml_models.models import MLModel

fake = Faker()


def generate_users(count=10):
    for i in range(count):
        u = User(
            username=fake.first_name(),
            email=fake.email(),
            password_hash='a',
        )
        db.session.add(u)
    db.session.commit()


def generate_ml_models(count=1):
    for i in range(count):
        model_name = f'{fake.name()} model'
        u = MLModel(
            model_name=model_name,
            description=fake.text(),
            pickle_path=f"/some/path/{model_name.replace(' ', '_')}",
        )
        db.session.add(u)
    db.session.commit()
