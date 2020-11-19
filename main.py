from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user_info = {
        'name': 'Mike',
        'age': 42,
    }
    return render_template('index.html', user_info=user_info)


@app.route('/user/<name>/')
def hello_from_kwargs(name):
    return f'<h1>Hello string, {name}!</h1>'


if __name__ == '__main__':
    app.run()
