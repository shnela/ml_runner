from datetime import datetime, timezone

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
Bootstrap(app)
Moment(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.args)
    print(request.form)
    return render_template('index.html', right_now=datetime.now(tz=timezone.utc))


@app.route('/user/<name>/')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    app.run()
