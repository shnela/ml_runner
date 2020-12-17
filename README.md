# REST API - user authentication

[README_PREVIOUS.md](./README_PREVIOUS.md)

[Flask-BasicAuth](https://flask-basicauth.readthedocs.io/en/latest/)

## Add new env variables to configuration
* BASIC_AUTH_USERNAME=user
* BASIC_AUTH_PASSWORD=pass

**Remember that those data should be keep secret on production**

### In config
```
BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')
BASIC_AUTH_FORCE = True
```

### How to access api endpoints?
https://www.toolsqa.com/postman/basic-authentication-in-postman/

1. In postman add header: (Authorization: Basic user:pass)
1. But header must use Base64 encoding, use https://www.base64encode.org/
1. Finally set header: (Authorization: Basic dXNlcjpwYXNz)

Should work.  
http://127.0.0.1:5000/api/v1/users/

### What about python
```
import requests
r = requests.get('http://127.0.0.1:5000/api/v1/users/')
r.status_code
401
r = requests.get('http://127.0.0.1:5000/api/v1/users/', headers={'Authorization': 'Basic dXNlcjpwYXNz'})
r.status_code
200
```

### You may want to protect only part of views:
Disable `BASIC_AUTH_FORCE = True` in `Config`

And decorate protected endpoints with `@basic_auth.required`.

Endpoints which save to database are updated in `ml_runner/api/sms.py`