from app import db
from app.auth.models import User
from tests.conftest import FlaskBaseTest


class TestMain(FlaskBaseTest):
    def setUp(self) -> None:
        super().setUp()
        user = User(username='username', email='some@email.com')
        db.session.add(user)
        db.session.commit()

    def test_index_page(self):
        response = self.client.get('/')
        assert response.status_code == 200
        assert User.query.count() == 1
        assert 'username' in response.data.decode()
        assert 'some@email.com' in response.data.decode()

    def test_index_page(self):
        user = User(username='username2', email='some2@email.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.get('/')
        assert response.status_code == 200
        assert 'username2' in response.data.decode()
        assert 'some2@email.com' in response.data.decode()
        assert User.query.count() == 2
