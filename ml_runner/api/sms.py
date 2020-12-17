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

post_parser = reqparse.RequestParser()
post_parser.add_argument('content', dest='content', required=True, help='SMS content')
post_parser.add_argument('sending_party_id', dest='sending_party_id', required=True)
post_parser.add_argument('sent_party_id', dest='sent_party_id', required=True)


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

        # filter by text
        text = request.args.get('text')
        if text is not None:
            sms_qs = sms_qs.filter(ReflectedShortMessageService.content.contains(text))

        # paginate results
        page = int(request.args.get('page', 1))
        sms_qs = sms_qs.offset(PER_PAGE * (page - 1)).limit(PER_PAGE)

        return sms_qs.all()

    @marshal_with(sms_mfields, envelope='message')
    def post(self):
        args = post_parser.parse_args()
        sms = ReflectedShortMessageService(
            send_date=datetime.now(),
            **args,
        )
        db.session.add(sms)
        db.session.commit()
        return sms


put_parser = reqparse.RequestParser()
put_parser.add_argument('content', dest='content', required=True, help='SMS content')


class SMSEndpoint(Resource):
    @marshal_with(sms_mfields, envelope='message')
    def get(self, sms_id):
        return db.session.query(ReflectedShortMessageService).get_or_404(sms_id)

    @marshal_with(sms_mfields, envelope='message')
    def put(self, sms_id):
        args = put_parser.parse_args()
        sms = db.session.query(ReflectedShortMessageService).get_or_404(sms_id)
        sms.content = args['content']
        db.session.add(sms)
        db.session.commit()
        return sms

    @marshal_with(sms_mfields, envelope='message')
    def delete(self, sms_id):
        sms = db.session.query(ReflectedShortMessageService).get_or_404(sms_id)
        db.session.delete(sms)
        db.session.commit()
        return sms


api.add_resource(SMSsEndpoint, '/sms/')
api.add_resource(SMSEndpoint, '/sms/<int:sms_id>/')
