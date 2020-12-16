from datetime import datetime, timedelta

from sqlalchemy import and_

from ml_runner import db
from ml_runner.reflected_models import ReflectedUser, ReflectedShortMessageService


def get_all_users():
    users = db.session.query(ReflectedUser).all()
    return users


def get_user_by_id(user_id):
    user = db.session.query(ReflectedUser).get(user_id)
    return user


def get_users_by_first_name(first_name):
    users = db.session.query(ReflectedUser).filter_by(first_name=first_name)
    return users.all()


def get_users_first_name_other_method(first_name):
    users = db.session.query(ReflectedUser).filter(ReflectedUser.first_name == first_name)
    return users.all()


def get_user_by_msisdn_prefix(msisdn_prefix):
    users = db.session.query(ReflectedUser).filter(ReflectedUser.msisdn.startswith(msisdn_prefix))
    return users.all()


def get_all_messages_sent_n_days_ago(days_ago):
    since = datetime.now() - timedelta(days=days_ago)
    messages = db.session.query(ReflectedShortMessageService).filter(ReflectedShortMessageService.send_date > since)
    return messages.all()


# TASK 1

def get_all_messages():
    return db.session.query(ReflectedShortMessageService).all()


def get_message_by_id(message_id):
    return db.session.query(ReflectedShortMessageService).get(message_id)


def get_messages_send_by(user_id):
    return db.session.query(ReflectedShortMessageService).filter_by(sending_party_id=user_id)


def get_messages_send_to(user_id):
    return db.session.query(ReflectedShortMessageService).filter_by(sent_party_id=user_id)


def get_message_containing(text):
    # should return all messages which have `text` in `content`
    return db.session.query(ReflectedShortMessageService).filter(
        ReflectedShortMessageService.content.contains(text)
    )


# TASK 2

def get_messages_sent_between(datetime_after, datetime_before=None):
    # return messages sent between datetimes if datetime_before is None, don't specify this parameter
    # use `from sqlalchemy import and_`
    # http://www.leeladharan.com/sqlalchemy-query-with-or-and-like-common-filters
    if datetime_before is None:
        datetime_before = datetime.now()
    messages = db.session.query(ReflectedShortMessageService).filter(
        and_(
            datetime_after < ReflectedShortMessageService.send_date,
            ReflectedShortMessageService.send_date < datetime_before,
        )
    )
    return messages.all()


def get_messages_received_by_users_with_last_name(last_name):
    # return all messages received by users whose last_name is `last_name` (there may be several such users)
    messages = list()
    for user in db.session.query(ReflectedUser).filter_by(last_name=last_name).all():
        for message in db.session.query(ReflectedShortMessageService).filter_by(sent_party_id=user.id).all():
            messages.append(message)
    return messages


def get_messages_received_by_users_with_last_name_nice_way(last_name):
    # return all messages received by users whose last_name is `last_name` (there may be several such users)
    for user in db.session.query(ReflectedUser).filter_by(last_name=last_name).all():
        yield from db.session.query(ReflectedShortMessageService).filter_by(sent_party_id=user.id).all()


if __name__ == '__main__':
    # invoke function you want to run here or invoke it in debugger
    users = get_all_users()
    first_user = users[0]
    user_by_id = get_user_by_id(first_user.id)
    users_by_first_name = get_users_by_first_name(first_user.first_name)
    users_by_first_name2 = get_users_first_name_other_method(first_user.first_name)
    assert users_by_first_name == users_by_first_name2
    get_with_msisdn_prefix = get_user_by_msisdn_prefix('1')
    messages_sent_n_days_ago = get_all_messages_sent_n_days_ago(5)
    print('done')
