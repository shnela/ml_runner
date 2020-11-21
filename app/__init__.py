from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)


# modules initialization
Bootstrap(app)
Moment(app)
db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db)

from app import views
from app import errors

# @app.shell_context_processor
# def shell_context():
#     return dict(User=User, db=db, mail=mail, send_email=send_email)
