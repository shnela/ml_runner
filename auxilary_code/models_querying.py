from datetime import datetime, timedelta

from ml_runner.models import User, ShortMessageService


def get_all_users():
    users = User.query.all()
    return users


def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return user


def get_users_by_first_name(first_name):
    users = User.query.filter_by(first_name=first_name)
    return users.all()


def get_users_first_name_other_method(first_name):
    users = User.query.filter(User.first_name == first_name)
    return users.all()


def get_user_by_msisdn_prefix(msisdn_prefix):
    users = User.query.filter(User.msisdn.startswith(msisdn_prefix))
    return users.all()


def get_all_messages_sent_n_days_ago(days_ago):
    since = datetime.now() - timedelta(days=days_ago)
    messages = ShortMessageService.query.filter(ShortMessageService.send_date > since)
    return messages.all()


# TASK 1

def get_all_messages():
    pass

def get_message_by_id(message_id):
    pass


def get_messages_send_by(user_id):
    pass


def get_messages_send_to(user_id):
    pass


def get_message_containing(text):
    # should return all messages which have `text` in `content`
    pass


# TASK 2

def get_messages_sent_between(datetime_after, datetime_before=None):
    # return messages sent between datetimes if datetime_before is None, don't specify this parameter
    pass


def get_messages_received_by_users_with_last_name(last_name):
    # return all messages received by users whose last_name is `last_name` (there may be several such users)
    pass


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
