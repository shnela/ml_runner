from flask_restful import Resource, fields, marshal_with

from . import api
from ..models import User

user_fields = {
    'username': fields.String,
}
user_list_fields = {
    'users': fields.List(fields.Nested(user_fields)),
}

fake_user = User(username="I'm pretending that I'm from db")  # remove this cheater


class UsersEndpoint(Resource):
    @marshal_with(user_fields, envelope='users')
    def get(self, **kwargs):
        users = [fake_user for _ in range(10)]  # get real user from db
        return users


class UserEndpoint(Resource):
    @marshal_with(user_fields, envelope='user')
    def get(self, **kwargs):
        user = fake_user  # get real user from db
        return user


api.add_resource(UsersEndpoint, '/users/')
api.add_resource(UserEndpoint, '/users/<int:user_id>/')
