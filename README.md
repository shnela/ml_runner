# README

## New requirements
Flask-SQLAlchemy  # https://flask-sqlalchemy.palletsprojects.com/en/2.x/

## flask shell
```
# Go to WorkingDir
cd /cygdrive/c/Users/NobleProg/WorkingDir/
# activate environment
source ./virtualenvs/cygin_env/bin/activate
# go to project dir
cd ./ml_runner
# install all missing requirements
pip install -r requirements.txt

# run flask shell
FLASK_APP='main.py' SECRET_KEY='123' flask shell
```

In flask shell:
```python
# import user model
from main import User

# try to query elements
User.query.all()

# wrong, look at database in DBeaver
# then initialize models
from main import db
db.create_all()

# look at database in DBeaver
User.query.all()

# new user
u = User(username='Joe', email='joe@foo.bar')
db.session.add(u)
db.session.commit()

# query all users
User.query.all()

# get first user
User.query.all()

# filter
User.query.filter_by(username='Joe')
User.query.filter_by(username='Mark')

# when queryset is empty first returns None
User.query.filter_by(username='Mark').first()
```