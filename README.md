# REST API

[README_PREVIOUS.md](./README_PREVIOUS.md)

## REST
* REpresentational
* State
* Transfer

## API
* Application
* Programming
* Interface


## Facebook

* [https://www.facebook.com/](https://www.facebook.com/)
* [https://graph.facebook.com/](https://graph.facebook.com/)

### Let's look at it

#### In web browser

Just type in the request

#### Using [httpie](https://httpie.io/docs)  (It uses `http` command)
`python` library installed by pip (in our `requirements.txt`)

**update and activate cygwin venv**
In cygwin:
```bash
$ http https://graph.facebook.com/
$ http https://www.facebook.com
```

#### Using [requests](https://requests.readthedocs.io/en/master/)
`python` library installed by pip (in our `requirements.txt`)

```python
import requests
r = requests.get('https://graph.facebook.com/')
r.text
r.json()
```
##### JSON
* JavaScript
* Object
* Notation

```python
d = dict(zip('abc', '123'))
d['a'] = 0.1
import json
json.dumps(d)
dict_text = json.dumps(d)
json.loads(dict_text)
```

### Our API
1. check address using debug toolbar
1. go there:
  1. with browser
  1. with `httpie`
  1. with python (console e.g.)

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

## Please do not look there if you can.
* http://127.0.0.1:5000/api/v1/users/
* `http http://127.0.0.1:5000/api/v1/users/`
```python
r = requests.get('http://127.0.0.1:5000/api/v1/users/')
r.json()['users']

r = requests.get('http://127.0.0.1:5000/api/v1/users/10/')
r.json()
```
