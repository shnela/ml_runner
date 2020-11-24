# Revision of FlaskWTF

New fields - email and passwords.

```python
email = StringField('email', validators=[DataRequired(), Email()])
password = PasswordField('password', validators=[DataRequired()])
password2 = PasswordField('password2', validators=[DataRequired(), EqualTo('password')])
```

But `Email` validator requires new plugin.
Install `email-validator` using
```
Preferences | Project: ml_runner | Python Interpreter | + 
```


### Additional tasks
* Allow email addresses from from 'protonmail.com' only.
* Add field where user can optionally chose sex from choices list (user can select only one option).
* Add field where user can select none or several of options [meat, cheese, chips]
