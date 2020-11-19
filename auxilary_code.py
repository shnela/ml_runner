from flask import url_for, current_app

from main import app


def display_urls():
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('user', name='Joe'))
        print(url_for('user', name='Joe', additional_arg='mess', additional_arg2='mess2'))
        print(url_for('index', _external=True))


if __name__ == '__main__':
    display_urls()
