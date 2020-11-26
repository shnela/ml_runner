from flask_restful import Resource, fields, marshal_with

from . import api
from ..models import User

post_fields = {
    'content': fields.String,
    'creation_date': fields.DateTime,
}
user_fields = {
    'username': fields.String,
    'posts': fields.List(fields.Nested(post_fields)),
}
user_list_fields = {
    'users': fields.List(fields.Nested(user_fields)),
}


class UsersEndpoint(Resource):
    @marshal_with(user_fields, envelope='users')
    def get(self, **kwargs):
        users = User.query.all()
        return users


class UserEndpoint(Resource):
    @marshal_with(user_fields, envelope='user')
    def get(self, **kwargs):
        user = User.query.get_or_404(kwargs['user_id'])
        return user


api.add_resource(UsersEndpoint, '/users/')
api.add_resource(UserEndpoint, '/users/<int:user_id>/')
