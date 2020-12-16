# Work with external database schema

[README_PREVIOUS.md](./README_PREVIOUS.md)

## [Specifying Classes Explicitly](https://docs.sqlalchemy.org/en/13/orm/extensions/automap.html#specifying-classes-explicitly)
Classes are defined in `reflected_models.py`.

### Where do they come form?
Explained in `auxilary_code/reflected_models_discovery.py`


### We now use `reflected models` **only**

Look at new `auxilary_code/reflected_models_querying.py`

But [SQLAlchemy query style](https://docs.sqlalchemy.org/en/14/orm/session_basics.html#querying-1-x-style)
was required...

Instead of:
```
User.query.all()
```

There's
```
db.session.query(ReflectedUser).all()
```