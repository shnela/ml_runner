# Blueprints
[Modular Applications with Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/#modular-applications-with-blueprints)

* Create `main` directory for `main` blueprint
* Move `views` and `forms` to it
* still works, let's make blueprint out of it
* make import of `LoginForm` in `views.py` relative
* create `Blueprint` in `main/__init__.py`
```python
bp = Blueprint('main', __name__)
```
* Replace `app` usages with `bp` in `views.py`
* and register in `__init__.py`
* After removing views imoprt in `__init__.py` add it in `main/__init__.py`
* Fix url_for (add blueprint scope)
  * `base.html` `url_for('` -> `url_for('main.`