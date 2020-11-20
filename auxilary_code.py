def display_urls():
    from flask import url_for
    from main import app
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('user', name='Joe'))
        print(url_for('user', name='Joe', additional_arg='mess', additional_arg2='mess2'))
        print(url_for('index', _external=True))


def timezones():
    from datetime import datetime, timezone
    print(datetime.now())
    print(datetime.now(tz=timezone.utc))
    print(datetime.now(tz=timezone.utc).isoformat())


def env_variables():
    import os
    print(os.environ)
    print(os.environ.get('SOME_VAR'))


if __name__ == '__main__':
    display_urls()
    timezones()
    env_variables()
