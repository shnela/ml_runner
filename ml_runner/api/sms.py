from flask_restful import Resource
from flask_restful import fields, marshal_with

from . import api
from .. import db
from ..reflected_models import ReflectedShortMessageService

sms_mfields = {
}


class SMSsEndpoint(Resource):
    def get(self):
        pass


class SMSEndpoint(Resource):
    def get(self, sms_id):
        pass


api.add_resource(SMSsEndpoint, '/sms/')
api.add_resource(SMSEndpoint, '/sms/<int:sms_id>/')
