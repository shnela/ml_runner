import os

current_dir = os.path.dirname(__file__)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')
    BASIC_AUTH_FORCE = True


class ConfigLocal(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(current_dir, '..', 'test.db')}"


class ConfigRemote(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
