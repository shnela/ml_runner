# Separate config

[Load config from object](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Config.from_object)

* Save config values in `Config` object in `__init__.py`

```python
class Config:
    SECRET_KEY = ...

...
app.config.from_object(Config)
```

* Move config object to new `config.py` file