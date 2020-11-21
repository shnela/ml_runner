from flask import Blueprint

bp = Blueprint('ml_models', __name__)

from . import views
