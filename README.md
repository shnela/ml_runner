# REST API basics

[README_PREVIOUS.md](./README_PREVIOUS.md)

## What's REST API?
API - Application Programming Interface

https://restfulapi.net/

## Look at our custom api
In file `ml_runner/api/users.py`


## And send some GET requests
With `postman`:
* http://127.0.0.1:5000/api/v1/users/
* http://127.0.0.1:5000/api/v1/users/<some_id>

## POST doesn't work

#### Using [requests](https://requests.readthedocs.io/en/master/)
`python` library installed by pip (in our `requirements.txt`)

```python
import requests
r = requests.get('https://graph.facebook.com/')
r.text
r.json()
```
