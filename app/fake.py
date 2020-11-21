from faker import Faker

from . import db
from .auth.models import User

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
