from flask_restful import Resource

from . import api


fake_user = {'username': 'Olo'}


class UsersEndpoint(Resource):
    def get(self, **kwargs):
        users = [fake_user for _ in range(10)]
        return {
            'users': users
        }


class UserEndpoint(Resource):
    def get(self, **kwargs):
        user = fake_user
        return {
            'user': user
        }


api.add_resource(UsersEndpoint, '/users/')
api.add_resource(UserEndpoint, '/users/<int:user_id>/')
