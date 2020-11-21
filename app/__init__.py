from flask import Flask
from flask_bootstrap import Bootstrap
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


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db=db)

    from app.main import bp as main_bp
    from app.auth import bp as auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    # generate context
    from app.auth.models import User
    from app.utils import send_email

    @app.shell_context_processor
    def shell_context():
        return dict(User=User, db=db, mail=mail, send_email=send_email)

    return app
