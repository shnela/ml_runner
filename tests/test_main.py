from app import db
from app.auth.models import User


def test_index_page(client):
    user = User(username='username', email='some@email.com')
    db.session.add(user)
    db.session.commit()

    response = client.get('/')
    assert response.status_code == 200
    assert 'username' in response.data.decode()
    assert 'some@email.com' in response.data.decode()
