# Connecting to MariaDB

[README_PREVIOUS.md](./README_PREVIOUS.md)

## Test MariaDB connection

### Connect using dBeaver to MariaDB
Credentials will be sent on zoom.

### If database works - configure it in flask app

Set proper env variables in `main` config:
* `DB_USER`
* `DB_PASSWORD`
* `DB_HOST`
* `DB_NAME`

1. Run application and look at `Users list` and `Posts list`.
1. Run `regenerate_fake_models.py`
   1. Fails because of missing db configuration
   1. Copy `Environment variables` from `main` config
   1. Save configuration
1. Run `regenerate_fake_models.py` again.
1. Run application and check if `Users` and `Posts` were created.

## Connecting to MariaDB with Flask-`SQLAlchemy`
[Flask-SQLAlchemy - Connection URI Format](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format)
&rarr;
[SQLAlchemy supported databases](https://docs.sqlalchemy.org/en/14/core/engines.html)
&rarr;
[SQLAlchemy - MySQL and MariaDB](https://docs.sqlalchemy.org/en/14/dialects/mysql.html)

Also some [StackOverflow answer](https://stackoverflow.com/a/56418030/1565454)

### You have new requirements in `requirements.txt`
```
SQLAlchemy
PyMySQL
```

### We want to update `Config` with
```
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@host/dbname'
```

but at the same time be able to keep old values. Just in case...

Split `Config` to `ConfigLocal` and `ConfigRemote`,
but first, look at [./auxilary_code/python_inheritance.py](./auxilary_code/python_inheritance.py)

