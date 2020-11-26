from flask_restful import Resource, fields, marshal_with

from .. import db
from ..reflected_models import ReflectedPost
from . import api


user_fields = {
    'username': fields.String,
}
post_fields = {
    'id': fields.Integer,
    # 'user_id': fields.Integer(attribute='id'),
    'content': fields.String,
    'creation_date': fields.DateTime,
    'author': fields.Nested(user_fields, attribute='user'),
    'details_url': fields.Url('api.postendpoint'),
}


class PostsEndpoint(Resource):
    @marshal_with(post_fields, envelope='posts')
    def get(self):
        users = db.session.query(ReflectedPost).all()
        return users


class PostEndpoint(Resource):
    @marshal_with(post_fields, envelope='post')
    def get(self, id):
        user = db.session.query(ReflectedPost).get_or_404(id)
        return user


api.add_resource(PostsEndpoint, '/posts/')
api.add_resource(PostEndpoint, '/posts/<int:id>/')
