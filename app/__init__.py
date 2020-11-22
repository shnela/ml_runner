from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

# modules initialization
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
mail = Mail()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if config is not None:
        app.config.update(config)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db=db)
    login_manager.init_app(app)

    from app.main import bp as main_bp
    from app.auth import bp as auth_bp
    from app.ml_models import bp as ml_models_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(ml_models_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # add error handlers
    # error handler can't be part of blueprint (https://github.com/pallets/flask/issues/1935)
    with app.app_context():
        from app import errors

    # generate context
    from app.auth.models import User
    from app.ml_models.models import MLModel, MLModelRun
    from app.utils import send_email

    @app.shell_context_processor
    def shell_context():
        return dict(User=User, db=db, mail=mail, send_email=send_email,
                    MLModel=MLModel, MLModelRun=MLModelRun)

    return app
