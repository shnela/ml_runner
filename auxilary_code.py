def display_urls():
    from flask import url_for
    from main import app
    with app.test_request_context():
        print(url_for('main.index'))
        print(url_for('main.user', name='Joe'))
        print(url_for('main.user', name='Joe', additional_arg='mess', additional_arg2='mess2'))
        print(url_for('main.index', _external=True))


def timezones():
    from datetime import datetime, timezone
    print(datetime.now())
    print(datetime.now(tz=timezone.utc))
    print(datetime.now(tz=timezone.utc).isoformat())


def env_variables():
    import os
    print(os.environ)
    print(os.environ.get('SOME_VAR'))


def sys_path():
    import os
    print(__file__)
    print(os.path.dirname(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))


def deco(f):
    print('start defining deco')

    def inner_func(*args, **kwargs):
        print('before call')
        result = f(*args, **kwargs)
        print('after call')
        return result

    print('stop defining deco')

    return inner_func


@deco
def some_func():
    print('some_func ran')

if __name__ == '__main__':
    # display_urls()
    # timezones()
    # env_variables()
    # sys_path()
    some_func()
