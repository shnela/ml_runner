from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>/')
@app.route('/other_link/<name>/')
def hello_from_kwargs(name):
    return f'<h1>Hello string, {name}!</h1>'


@app.route('/user/<int:number>/')
def hello_number(number: int):
    return f'<h1>Hello number, {number}!</h1>'


@app.route('/user/<uuid:uuid>/')
def hello_uuid(uuid):
    return f'<h1>Hello uuid, {uuid}!</h1>'


@app.route('/user/<path:text>/<int:number>/')
def hello_both(text, number):
    return f'<h1>Hello, {text} ({number})!</h1>'


if __name__ == '__main__':
    app.run()
