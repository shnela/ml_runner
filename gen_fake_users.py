from main import db, User
from faker import Faker

fake = Faker()


def create_users(n=10):
    for _ in range(n):
        u = User(username=fake.unique.first_name())
        db.session.add(u)
    db.session.commit()


def delete_all():
    for user in User.query.all():
        db.session.delete(user)
    db.session.commit()


if __name__ == '__main__':
    db.create_all()
    delete_all()
    print(User.query.count())
    create_users(100)
    print(User.query.count())
