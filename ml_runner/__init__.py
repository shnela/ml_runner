from flask import Flask
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)
Bootstrap(app)

# blueprint registration
from .main import bp as main_bp
from .api import bp as api_bp
app.register_blueprint(main_bp)
app.register_blueprint(api_bp, url_prefix='/api/v1')
