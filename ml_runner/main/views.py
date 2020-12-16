from flask import render_template

from . import bp
from ..models import ShortMessageService


@bp.route('/')
def index():
    sms_count = ShortMessageService.query.count()
    return render_template('index.html', sms_count=sms_count)
