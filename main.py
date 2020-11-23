from flask import Flask

app = Flask(__name__)


def index():
    return '<h1>Hello World!</h1>'


def hello_from_kwargs(name):
    return f'<h1>Hello string, {name}!</h1>'


def hello_number(number: int):
    return f'<h1>Hello number, {number}!</h1>'


def hello_uuid(uuid):
    return f'<h1>Hello uuid, {uuid}!</h1>'


def hello_both(text, number):
    return f'<h1>Hello, {text} ({number})!</h1>'


app.add_url_rule('/', 'index', index)
app.add_url_rule('/user/<name>/', 'hello_from_kwargs', hello_from_kwargs)
app.add_url_rule('/other_link/<name>/', 'other_hello_from_kwargs', hello_from_kwargs)
app.add_url_rule('/user/<int:number>/', 'hello_number', hello_number)
app.add_url_rule('/user/<uuid:uuid>/', 'hello_uuid', hello_uuid)
app.add_url_rule('/user/<path:text>/<int:number>/', 'hello_both', hello_both)


if __name__ == '__main__':
    app.run()
