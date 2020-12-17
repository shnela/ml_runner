from flask_restful import Resource

from . import api


fake_user = {'first_name': 'Olo'}


class UsersEndpoint(Resource):
    def get(self):
        # returns list of all users
        users = [fake_user for _ in range(10)]
        return {
            'users': users
        }


class UserEndpoint(Resource):
    def get(self, user_id):
        # downloads particular user
        user = fake_user
        return {
            'user': user
        }

    def put(self, user_id):
        # updates user
        user = fake_user
        return {
            'user': user
        }


api.add_resource(UsersEndpoint, '/users/')
api.add_resource(UserEndpoint, '/users/<int:user_id>/')
