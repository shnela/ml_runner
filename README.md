# Users displayed only

## Create new model `Post` (blog post)

`Post` should have:
* `id`
* `content`
* `creation_date` (default now)

What type should we use for blog post?  
[Available examples](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example)

```python
from datetime import datetime, timezone
datetime.now()
datetime.now(tz=timezone.utc)
```

**Always use utc timezone in backend code**

But remember, [datetime handling is mess](https://zachholman.com/talk/utc-is-enough-for-everyone-right)
> So you’ve got a bunch of scientist types around 1960 who are like, hey, time is all screwy we should totes make a standard. And some of them spoke English, and some of them spoke French, which, of course, is the cause of so much conflict over so many generations. (In hindsight, maybe we should have split all those troublemakers up from the start.)

> The English-speaking folk were like yo, this definitely sounds like Coordinated Universal Time, boom, ship it. And the French speakers were like yeah that makes total sense! Temps Universel Coordonné DOES work out well in our language, too, ship it! Then they both looked up and realized cool, they’ve created both CUT and TUC for acronyms. Shit.

> When your standard — that is expressly meant to standardize time — doesn’t even standardize on a standard acronym, well, damn, that probably doesn’t bode well for your standard.

Let's see `default` datetime for `creation_date` `Column`: `datetime.now`

## Post model created - let's play with it in flask shell
*To run `Flask shell` see [INSTRUCTIONS_TO_COPY.md](INSTRUCTIONS_TO_COPY.md) file*
```
>>> from ml_runner.models import User, Post
>>> User.query.count()
100
>>> Post.query.count()
Error...

>>> from ml_runner import db
>>> db.create_all()
>>> Post.query.count()
```

`db.create_all()` creates **new** tables.  
It doesn't handle modifications (like new field). For that we'd need
[migrations](https://flask-migrate.readthedocs.io/en/latest/).

```
>>> Post.query.count()
# now it works

# Let's add new post
>>> p = Post(content='Some short tweet')
>>> p.id
>>> p.content
'Some short tweet'
>>> p.creation_date
>>> from ml_runner import db
>>> db.session.add(p)
>>> p.id, p.content, p.creation_date
(None, 'Some short tweet', None)
AttributeError: 'scoped_session' object has no attribute 'save'
>>> db.session.commit()
>>> p.id, p.content, p.creation_date
(1, 'Some short tweet', datetime.datetime(2020, 11, 25, 21, 13, 8, 719911))
```

**`id` and `creation_date` are generated when saving to database.**

.

.

.

.

.

.

.

.

## Pls, do not look here if you can
```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)

```