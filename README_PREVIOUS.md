# REST API - Serializing models

[README_PREVIOUS.md](./README_PREVIOUS.md)

## [marshall](https://flask-restful.readthedocs.io/en/latest/api.html?highlight=marshall_with#flask_restful.marshal)

Look at `auxilary_code/marshalling_models.py`:
[Fields](https://flask-restful.readthedocs.io/en/latest/api.html?highlight=marshall_with#module-fields)


## Task1 implement sms api
Fill empty functions in file `ml_runner/api/sms.py`.  
You can base on `auxilary_code/marshalling_models.py`.

After it's done when request run on `Postman`:
### GET http://127.0.0.1:5000/api/v1/sms/
You should receive something like:
```
{
    "messages": [
        {
            "id": 401,
            "content": "Tree break become relationship practice especially. Become campaign do forget kitchen common.\nElse once religious. Establish grow common decision cause plan.",
            "send_date": "Wed, 02 Dec 2020 01:32:27 -0000",
            "sending_party_id": 41,
            "sent_party_id": 41
        },
        {
            "id": 402,
            "content": "Article charge care detail. Rate forget project or strategy.\nBeat might local opportunity. Myself choose end southern choice charge section.",
            "send_date": "Mon, 23 Nov 2020 21:37:50 -0000",
            "sending_party_id": 41,
            "sent_party_id": 41
        },
...
```

### GET http://127.0.0.1:5000/api/v1/sms/401/
**Make sure that id exists**

You should receive something like:
```
{
    "message": {
        "id": 401,
        "content": "Tree break become relationship practice especially. Become campaign do forget kitchen common.\nElse once religious. Establish grow common decision cause plan.",
        "send_date": "Wed, 02 Dec 2020 01:32:27 -0000",
        "sending_party_id": 41,
        "sent_party_id": 41
    }
}
```

### GET http://127.0.0.1:5000/api/v1/sms/9999/
You should receive something like:
```
{
    "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
}
```


## Task2 Pretty print related model
`ReflectedUser` defined in `ml_runner/reflected_models.py` is now updated.  
It contains `sent_messages` and `received_messages`, which defines back references to:
* `ReflectedShortMessageService.sending_party`
* `ReflectedShortMessageService.sent_party`

Use those new fields of `ReflectedShortMessageService` to return such detailed result:

### GET http://127.0.0.1:5000/api/v1/sms/401/
**Make sure that id exists**
So SMS details'd look like this:
```
{
    "message": {
        "id": 501,
        "content": "Spring ball west building this education job.\nView run leader measure little body. Possible during art address already hour expert.\nNight worry anyone paper anything. Role write tree billion true.",
        "send_date": "Fri, 27 Nov 2020 03:34:55 -0000",
        "sending_party": {
            "first_name": "Frank",
            "last_name": "Cook"
        },
        "sent_party": {
            "first_name": "Robert",
            "last_name": "Black"
        }
    }
}
```

### Hint
Update `sms_mfields`, and use [Advanced : Nested Field](https://flask-restful.readthedocs.io/en/latest/fields.html#advanced-nested-field).
