# REST API - Filtering and pagination

[README_PREVIOUS.md](./README_PREVIOUS.md)


## Reflected model is back to normal
`ml_runner/reflected_models.py`

```
ReflectedUser = Base.classes.user
ReflectedShortMessageService = Base.classes.short_message_service
```

`relation` fields aren't updated.

## `ml_runner/api/users.py` is updated

### Args arguments
Get parameters like this:  
http://127.0.0.1:5000/api/v1/users/?last_name=something

## `ml_runner/api/sms.py` is updated

### Args arguments
Look at endpoints
http://127.0.0.1:5000/api/v1/sms/
http://127.0.0.1:5000/api/v1/sms/?page=1
http://127.0.0.1:5000/api/v1/sms/?page=2
http://127.0.0.1:5000/api/v1/sms/?date_from=2020-12-01T22:52:37.596841
http://127.0.0.1:5000/api/v1/sms/?date_from=2021-12-01T22:52:37.596841


## Task 1
If `SMSsEndpoint` is called with parameter `text`, return only messages which `content` contains `text`.

You may use example from `auxilary_code/reflected_models_querying.py:get_message_containing`
