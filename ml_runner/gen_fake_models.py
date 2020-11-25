from ml_runner import db
from ml_runner.models import User, Post
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
    for _ in range(n):
        p = Post(content=fake.unique.text())
        db.session.add(p)
    db.session.commit()


def delete_all_posts():
    Post.query.delete()
    db.session.commit()


if __name__ == '__main__':
    db.create_all()
    delete_all_users()
    delete_all_posts()
    create_posts(100)
    create_users(10)

