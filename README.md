# Work with Posts
[README_PREVIOUS.md](./README_PREVIOUS.md)

## Generate random Posts
Use [fake.unique.text()](https://pypi.org/project/Faker/) to generate new `Posts`.

### Generate posts in pyCharm or in flask shell

#### pyCharm
1. In `gen_fake_models.py`
1. Add `create_posts(100)` under `if __name__ == '__main__':` block
1. Run script by clicking green triangle on left


#### Flask shell
```
>>> from ml_runner.models import Post
>>> Post.query.count()
1010
>>> delete_all_posts()
>>> create_posts(100)
>>> Post.query.count()
100
```

### Look at posts in dBeaver
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
def create_posts(n=10):
    for _ in range(n):
        p = Post(content=fake.unique.text())
        db.session.add(p)
    db.session.commit()


def delete_all_posts():
    Post.query.delete()
    db.session.commit()
```


## Bonus - define list view and detail view for Posts
