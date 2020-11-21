import os
import tempfile
import unittest

from app import create_app, db


class FlaskBaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.db_fd, db_path = tempfile.mkstemp()
        config = {
            'SQLALCHEMY_DATABASE_URI': f"sqlite:///{db_path}.db",
            'WTF_CSRF_ENABLED': False,
            'TESTING': True
        }
        app_instance = create_app(config=config)
        self.app_context = app_instance.app_context()
        self.app_context.push()
        db.create_all()
        self.client = app_instance.test_client()

    def tearDown(self) -> None:
        self.app_context.pop()
        os.close(self.db_fd)
