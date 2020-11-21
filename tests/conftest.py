import os
import tempfile

import pytest

from app import create_app, db


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    config = {
        'SQLALCHEMY_DATABASE_URI': f"sqlite:///{db_path}.db",
        'WTF_CSRF_ENABLED': False,
        'TESTING': True,
    }
    app_instance = create_app(config=config)

    with app_instance.test_client() as client:
        with app_instance.app_context():
            db.create_all()
            yield client

    os.close(db_fd)
