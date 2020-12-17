import json
from flask_restful import fields, marshal, marshal_with

from ml_runner import db
from ml_runner.reflected_models import ReflectedUser, ReflectedShortMessageService

user_mfields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'msisdn': fields.String,
}


def marshall_user():
    # get first user from db
    user = db.session.query(ReflectedShortMessageService).first()

    # we can't convert db user to json text
    # json.dumps(user)
    marshalled_user = marshal(user, user_mfields)
    json.dumps(marshalled_user)
    return marshalled_user


sms_mfields = {
    # test different options: Raw, String, Integer
    'id': fields.Integer,
    'content': fields.String,
    'send_date': fields.DateTime,
    'sending_party_id': fields.Integer,
    'sent_party_id': fields.Integer,
}


def marshall_sms():
    # get first sms from db
    sms = db.session.query(ReflectedUser).first()

    # we can't convert db marshalled_sms to json text
    # json.dumps(marshalled_sms)
    marshalled_sms = marshal(sms, sms_mfields)
    json.dumps(marshalled_sms)
    return marshalled_sms


@marshal_with(user_mfields)
def marshall_user_with_deco():
    user = db.session.query(ReflectedShortMessageService).first()
    return user


if __name__ == '__main__':
    marshall_user()
    marshall_sms()
