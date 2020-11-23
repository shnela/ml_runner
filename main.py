from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from werkzeug.exceptions import abort

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    user_info = {
        'name': request.args.get('name', 'Mike'),
        'age': int(request.args.get('age', 42)),
    }
    return render_template('index.html', user_info=user_info)


@app.route('/user/<name>/<amount>/')
def hello_from_kwargs(name, amount):
    amount = int(amount)
    return render_template('hello_from_kwargs.html', name=name, amount=amount)


@app.route('/return_error/<int:response_code>/')
def return_response_with_code(response_code):
    return f'Return {response_code}', response_code


@app.route('/abort_error/<int:response_code>/')
def abort_response_with_code(response_code):
    abort(response_code)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    app.run()

