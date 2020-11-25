from ml_runner import db
from ml_runner.models import User
from faker import Faker

fake = Faker()


def create_users(n=10):
    for _ in range(n):
        u = User(username=fake.unique.first_name())
        db.session.add(u)
    db.session.commit()


def delete_all_users():
    User.query.delete()
    db.session.commit()


def create_posts(n=10):
    # define creation of n Posts here
    pass


def delete_all_posts():
    # delete all Posts here
    pass


if __name__ == '__main__':
    db.create_all()
    delete_all_users()
    delete_all_posts()
