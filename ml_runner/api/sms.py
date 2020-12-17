from flask_restful import Resource
from flask_restful import fields, marshal_with

from . import api
from .. import db
from ..reflected_models import ReflectedShortMessageService

user_base_mfields = {
    'first_name': fields.String,
    'last_name': fields.String,
}

sms_mfields = {
    'id': fields.Integer,
    'content': fields.String,
    'send_date': fields.DateTime,
    'sending_party': fields.Nested(user_base_mfields),
    'sent_party': fields.Nested(user_base_mfields),
}


class SMSsEndpoint(Resource):
    @marshal_with(sms_mfields, envelope='messages')
    def get(self):
        return db.session.query(ReflectedShortMessageService).all()


class SMSEndpoint(Resource):
    @marshal_with(sms_mfields, envelope='message')
    def get(self, sms_id):
        return db.session.query(ReflectedShortMessageService).get_or_404(sms_id)


api.add_resource(SMSsEndpoint, '/sms/')
api.add_resource(SMSEndpoint, '/sms/<int:sms_id>/')
