from flask import request
from flask_restful import Resource
from flask_restful import fields, marshal_with

from . import api
from .. import db
from ..reflected_models import ReflectedUser

user_mfields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'msisdn': fields.String,
}


class UsersEndpoint(Resource):
    @marshal_with(user_mfields, envelope='users')
    def get(self):
        users_qs = db.session.query(ReflectedUser)
        last_name = request.args.get('last_name')
        if last_name:
            users_qs = users_qs.filter_by(last_name=last_name)
        return users_qs.all()


class UserEndpoint(Resource):
    @marshal_with(user_mfields, envelope='user')
    def get(self, user_id):
        # downloads particular user
        user = db.session.query(ReflectedUser).get_or_404(user_id)
        return user

    def put(self, user_id):
        # updates user (not yet)
        user = db.session.query(ReflectedUser).get_or_404(user_id)
        return user


api.add_resource(UsersEndpoint, '/users/')
api.add_resource(UserEndpoint, '/users/<int:user_id>/')
