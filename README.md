# Serializing models and modifying them

[README_PREVIOUS.md](./README_PREVIOUS.md)

## [marshall](https://flask-restful.readthedocs.io/en/latest/api.html?highlight=marshall_with#flask_restful.marshal)

Look at `marshalling.py`:
[Fields](https://flask-restful.readthedocs.io/en/latest/api.html?highlight=marshall_with#module-fields)

Exercises on marshall.


### POST PUT [(CRUD)](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)


[parsing input](https://flask-restful.readthedocs.io/en/latest/api.html?highlight=RequestParser#module-reqparse)

#### Create
```
>>> new_user = ReflectedUser(username='just_created')
>>> db.session.query(ReflectedUser).filter_by(username='just_created').first()
>>> db.session.add(new_user)
>>> db.session.commit()
>>> new_u = db.session.query(ReflectedUser).filter_by(username='just_created').first()
>>> new_u.username, new_u.posts
('just_created', [])
```

#### Update

In shell
```
>>> u_by_id = db.session.query(ReflectedUser).get(5)
>>> u_by_id.username, len(u_by_id.posts), u_by_id.posts[0].content[:10]
('Miranda', 10, 'Money myse')
>>> u_by_id.username = 'new name'
>>> db.session.add(u_by_id)
>>> db.session.commit()
>>> u_by_id = db.session.query(ReflectedUser).get(6)
>>> u_by_id.username, len(u_by_id.posts), u_by_id.posts[0].content[:10]
('new name', 10, 'Money myse')
```

#### Delete

In shell
```
>>> u = db.session.query(ReflectedUser).first()
>>> u
<ml_runner.reflected_models.ReflectedUser object at 0x102f8adc0>
>>> u.username
'Brooke'
>>> u.id, u.username
(5, 'Brooke')
>>> u_by_id = db.session.query(ReflectedUser).get(5)
>>> u_by_id.id, u_by_id.username
(5, 'Brooke')
>>> db.session.delete(u_by_id)
>>> db.session.commit()
>>> u_by_id = db.session.query(ReflectedUser).get(5)
>>> u_by_id
```