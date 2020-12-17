from datetime import datetime

from flask import request
from flask_restful import Resource, reqparse
from flask_restful import fields, marshal_with

from . import api
from .. import db
from ..reflected_models import ReflectedShortMessageService

PER_PAGE = 10

sms_mfields = {
    'id': fields.Integer,
    'content': fields.String,
    'send_date': fields.DateTime,
    'sending_party_id': fields.Integer,
    'sent_party_id': fields.Integer,
}


class SMSsEndpoint(Resource):
    @marshal_with(sms_mfields, envelope='messages')
    def get(self):
        # initial queryset
        sms_qs = db.session.query(
            ReflectedShortMessageService
        )

        # filter by date_from
        date_from_isoformat = request.args.get('date_from')
        if date_from_isoformat is not None:
            date_from = datetime.fromisoformat(date_from_isoformat)
            sms_qs = sms_qs.filter(ReflectedShortMessageService.send_date > date_from)

        # paginate results
        page = int(request.args.get('page', 1))
        sms_qs = sms_qs.offset(PER_PAGE * (page - 1)).limit(PER_PAGE)

        return sms_qs.all()




class SMSEndpoint(Resource):
    @marshal_with(sms_mfields, envelope='message')
    def get(self, sms_id):
        return db.session.query(ReflectedShortMessageService).get_or_404(sms_id)


api.add_resource(SMSsEndpoint, '/sms/')
api.add_resource(SMSEndpoint, '/sms/<int:sms_id>/')
