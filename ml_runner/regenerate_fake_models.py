import random

from ml_runner import db
from ml_runner.models import User, ShortMessageService
from faker import Faker

fake = Faker()


def create_users(users_number=10, *, messages_per_user=0):
    users_to_add = list()
    for _ in range(users_number):
        new_user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            msisdn=fake.unique.msisdn(),
        )
        db.session.add(new_user)
        users_to_add.append(new_user)
        # we don't want to call `db.session.commit()` here,
        # to prevent many db connections
        # at the same time we can't add `Posts` here,
        # because `User.id` will be set in database after calling `db.session.commit()`
    db.session.commit()
    # now user instances have assigned `User.id`

    for new_user in users_to_add:
        receiver = random.choice(users_to_add)
        create_message(messages_per_user, sending_party_id=new_user.id, sent_party_id=receiver.id)


def delete_all_users():
    User.query.delete()
    db.session.commit()


def create_message(n=10, *, sending_party_id, sent_party_id):
    for _ in range(n):
        message = ShortMessageService(
            content=fake.text(),
            send_date=fake.past_datetime(),
            sending_party_id=sending_party_id,
            sent_party_id=sent_party_id,
        )
        db.session.add(message)
    db.session.commit()


def delete_all_messages():
    ShortMessageService.query.delete()
    db.session.commit()


if __name__ == '__main__':
    db.create_all()
    delete_all_messages()
    delete_all_users()
    # create_users(10, messages_per_user=10)
    create_users(10, messages_per_user=0)
