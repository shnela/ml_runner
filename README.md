# Work with external database schema

[README_PREVIOUS.md](./README_PREVIOUS.md)

## Make sure that we always can re-create database
Add `DO_NOT_REFLECT=1` to `regenerate_fake_models` creation.

## make_shell_context
Automatic imports in `flask shell`

## Prepare flask shell
1. Go to flask shell and check how it works now.
[How to run flask shell](./INSTRUCTIONS_TO_COPY.md)
1. Copy `environment_template.env` to `environment.env`
1. Edit `environment.env`
1. Save it with **LF** endline option (bottom right corner).

## Reflect external db schema
Code defined in reflected_models.py

###[Basic use](https://docs.sqlalchemy.org/en/13/orm/extensions/automap.html#basic-use)

```
>>> u = User.query.first()
>>> u.id, u.username, u.posts[:2]
(7, 'Christopher', [<Post 61>, <Post 62>])
>>> p = Post.query.first()
>>> p.id, p.content[:10], p.creation_date, p.user_id, p.user
(1, 'Cover blue', datetime.datetime(2020, 11, 26, 21, 15, 47), 1, <User 'rook2'>)

>>> ReflectedUser.query
Error
>>> ru = db.session.query(ReflectedUser).first()  # SQLAlchemy notation
>>> ru.id, ru.username, ru.posts
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'user' object has no attribute 'posts'
>>> ru.id, ru.username
(7, 'Christopher')

But the way back works!
>>> rp = db.session.query(ReflectedPost).first()
>>> rp.id, rp.content[:10], rp.creation_date, rp.user_id, rp.user
(1, 'Cover blue', datetime.datetime(2020, 11, 26, 21, 15, 47), 1, <sqlalchemy.ext.automap.user object at 0x104dfca90>)
```

## [Specifying Classes Explicitly](https://docs.sqlalchemy.org/en/13/orm/extensions/automap.html#specifying-classes-explicitly)
Replace `ReflectedUser` with class definition in `reflected_models.py`

```
>>> ru = db.session.query(ReflectedUser).first() 
>>> ru.id, ru.username, ru.posts[:2]
(7, 'Christopher', [<sqlalchemy.ext.automap.post object at 0x10545b190>, <sqlalchemy.ext.automap.post object at 0x10545b400>])
>>> rp = db.session.query(ReflectedPost).first()
>>> rp.id, rp.content[:10], rp.creation_date, rp.user_id, rp.user
(1, 'Cover blue', datetime.datetime(2020, 11, 26, 21, 15, 47), 1, <ml_runner.reflected_models.ReflectedUser object at 0x10545bcd0>)
```

**`backref='user'`** Was crucial.

[SQLAlchemy query style](https://docs.sqlalchemy.org/en/14/orm/session_basics.html#querying-1-x-style)

## Change models usage in `main/views.py`
User `ReflectedUser` and `ReflectedPost` models instead of `User` and `Post`
