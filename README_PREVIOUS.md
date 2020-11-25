# Flask Debug Toolbar
[README_PREVIOUS.md](./README_PREVIOUS.md)

[Documentation](https://flask-debugtoolbar.readthedocs.io/en/latest/)

## Installation
Your requirements.txt is updated, pyCharm will do the job


## Update `ml_runner/__init__.py`

Add following in proper places of `ml_runner/__init__.py`.
```python
from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)
```

## Flask application MUST run in **debug** mode

We did it previously when settings `FLASK_ENV=development`

## Python play (dict accessing)
```
# NOT IMPORTANT, I'M JUST GENERATING DICT IN FANCY WAY
>>> letters = 'abcdefgh'
>>> numbers = range(8)
>>> zip(letters, numbers)
<zip object at 0x10222cbc0>
>>> zip(letters, numbers)[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'zip' object is not subscriptable
>>> list(zip(letters, numbers))
[('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6), ('h', 7)]
>>> dict(zip(letters, numbers))
{'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
>>> d = dict(zip(letters, numbers))

# EXTREMLY IMPORTANT - ACCESSING DICT ELEMENTS IS CRUCIAL
>>> d.keys()
dict_keys(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
>>> d.values()
dict_values([0, 1, 2, 3, 4, 5, 6, 7])
>>> d.items()
dict_items([('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6), ('h', 7)])
```

## `session_kv_storage` view in `views.py`
Test:
* 127.0.0.1:5000/session_kv_storage/key1/42/
* 127.0.0.1:5000/session_kv_storage/k2/42/
* 127.0.0.1:5000/session_kv_storage/k3/55/

### Do debugging
`list(session.items())`