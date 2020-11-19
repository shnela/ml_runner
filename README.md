# README

## Dynamic routes
[Instrukcja](https://flask.palletsprojects.com/en/1.1.x/api/#url-route-registrations)


## Set `FLASK_ENV=development`

### Cygwin
```bash
# run application
$ FLASK_APP='main.py' FLASK_ENV=development flask run
```

### pyCharm
Add `FLASK_ENV=development` in `Run configuration` -> `Environment variables`

## Remember about trailing slashes
```python
@app.route('/user/<string:name>')  # wrong
@app.route('/user/<string:name>/')
```

## Zadanie
### url converters
Define functions:
* hello_number(number: int):
* hello_uuid(uuid):
* hello_both(text, number):

Visit:
* http://127.0.0.1:5000/user/name/
* http://127.0.0.1:5000/user/42/
* http://127.0.0.1:5000/user/123e4567-e89b-12d3-a456-426614174000/
* http://127.0.0.1:5000/user/he/man/42/  # make it work


### `hello_from_kwargs` available in two urls
Make `hello_from_kwargs` view available under `/other_link/<name>/`

### Use `add_url_rule`
Use [`add_url_rule`](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.add_url_rule) instead of `app.route`
decorator.