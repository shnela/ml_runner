from functools import wraps

from flask_login import current_user
from flask import abort


def admin_required(f):
    @wraps(f)
    def inner_func(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        result = f(*args, **kwargs)
        return result
    return inner_func
