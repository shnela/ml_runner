# Faker

Generate randomized users with [Faker](https://pypi.org/project/Faker/)

* create `create_user` with const name in `gen_fake_users`.

### Test faker in Python console.
```python
from gen_fake_users import Faker
fake = Faker()
```

* Test `name`, `email` and `first_name`.
* rename to `create_users(n)`
* show how to delete user `db.session.delete(u)`
* show importance of session commit
