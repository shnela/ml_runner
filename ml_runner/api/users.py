from flask_restful import Resource, fields, marshal_with, reqparse

from .. import db
from ..reflected_models import ReflectedUser
from . import api

post_fields = {
    'content': fields.String,
    'creation_date': fields.DateTime,
}
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    # 'posts': fields.Nested(post_fields),  # what's the difference?
    'posts': fields.List(fields.Nested(post_fields)),
}

simple_user_fields = {
    'id': fields.Integer,
    'username': fields.String,
}
post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'username', dest='username', required=True,
    help='The user\'s username',
)


class UsersEndpoint(Resource):
    @marshal_with(user_fields, envelope='users')
    def get(self):
        users = db.session.query(ReflectedUser).all()
        return users

    @marshal_with(simple_user_fields)
    def post(self):
        args = post_parser.parse_args()
        user = ReflectedUser(**args)
        db.session.add(user)
        db.session.commit()
        return user


class UserEndpoint(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        user = db.session.query(ReflectedUser).get_or_404(user_id)
        return user

    @marshal_with(simple_user_fields)
    def put(self, user_id):
        args = post_parser.parse_args()
        user = db.session.query(ReflectedUser).get_or_404(user_id)
        user.username = args['username']
        db.session.add(user)
        db.session.commit()
        return user

    @marshal_with(simple_user_fields)
    def delete(self, user_id):
        user = db.session.query(ReflectedUser).get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return user


api.add_resource(UsersEndpoint, '/users/')
api.add_resource(UserEndpoint, '/users/<int:user_id>/')
