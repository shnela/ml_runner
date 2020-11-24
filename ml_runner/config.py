import os

current_dir = os.path.dirname(__file__)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(current_dir, '..', 'test.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
