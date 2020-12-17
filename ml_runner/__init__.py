from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth

from .config import ConfigRemote as Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)
basic_auth = BasicAuth(app)

# blueprint registration
from .main import bp as main_bp
from .api import bp as api_bp
app.register_blueprint(main_bp)
app.register_blueprint(api_bp, url_prefix='/api/v1')
