# REST API - modifications

[README_PREVIOUS.md](./README_PREVIOUS.md)

## POST PUT [(CRUD)](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

[parsing input](https://flask-restful.readthedocs.io/en/latest/api.html?highlight=RequestParser#module-reqparse)


## Test endpoints in Postman

### POST http://127.0.0.1:5000/api/v1/sms/
Without Params, should inform about missing Parameters.


### POST http://127.0.0.1:5000/api/v1/sms/
With Params:
* content - 'sms content, text of sms'
* sending_party_id - some existing id of user
* sent_party_id - some existing id of user

Should return something like:
```
{
    "message": {
        "id": 603,
        "content": "content of SMS",
        "send_date": "Thu, 17 Dec 2020 02:34:11 -0000",
        "sending_party_id": 71,
        "sent_party_id": 72
    }
}
```

### PUT http://127.0.0.1:5000/api/v1/sms/<id from response above>/
With Params:
* content - 'New content of SMS'

Should return something like:
```
{
    "message": {
        "id": 603,
        "content": "new content",
        "send_date": "Thu, 17 Dec 2020 02:34:11 -0000",
        "sending_party_id": 71,
        "sent_party_id": 72
    }
}
```
