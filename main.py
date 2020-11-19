from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>/')
def hello_from_kwargs(name):
    return f'<h1>Hello string, {name}!</h1>'


if __name__ == '__main__':
    app.run()
