from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .auth import bp as auth_bp
from .main import bp as main_bp

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
Bootstrap(app)

# blueprint registration
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
