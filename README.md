# `User` has written the `Post` - one to many

[README_PREVIOUS.md](./README_PREVIOUS.md)

## Look at our `User` and `Post` models in dBeaver
```
test.db -> Tables -> ER Diagram
```

And compare with [this](https://fmhelp.filemaker.com/help/18/fmp/en/index.html#page/FMP_Help/one-to-many-relationships.html)
explanation.

## One to many in `Flask-SQLAlchemy`

[link](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships)

```python
posts = db.relationship('Post', backref='user', lazy=True)
user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
```

We edited only `post` **database table** - we've added `user_id` column.  

### Test new model in flask shell
[how to run flask shell](INSTRUCTIONS_TO_COPY.md)

```
>>> from ml_runner.models import Post
>>> Post.query.first()
# doesn't work :(
>>> from ml_runner import db
>>> db.create_all()
>>> Post.query.first()
# did it help?
```

But we have to **delete** Post tables and recreate it again.
[Flask-sqlalchemy](https://flask-migrate.readthedocs.io/en/latest/) would help.

1. **Close flask shell - ctrl-D**
1. **Delete db file**

Then run in shell
```
>>> from ml_runner import db
>>> from ml_runner.models import Post
>>> db.create_all()
>>> Post.query.first()
# nice!
```

Generate some users and posts in `gen_fake_models.py`

```
>>> from ml_runner.models import User, Post
>>> u = User.query.first()
>>> p1 = Post.query.first()
>>> p2 = Post.query.offset(1).first()
>>> p1.user_id = u.id
>>> p2.user_id = u.id
>>> from ml_runner import db
>>> db.session.add(p1, p2)
>>> db.session.commit()

# pause for dBeaver

>>> u.posts
[<Post 1>, <Post 2>]
>>> p1.user
<User 'Debra'>
```
