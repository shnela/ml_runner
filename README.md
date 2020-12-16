# Run project, test models

[README_PREV.md](./README_PREV.md)

## Initialize new models
Run `ml_runner/regenerate_fake_models.py`.
Remember about updating `Environment variables`:
* FLASK_ENV=development
* SECRET_KEY=123
* SQLALCHEMY_DATABASE_URI=<sent in zoom>

## Run flask app
Run `main.py`
Remember about updating `Environment variables`: as for `regenerate_fake_models`.

Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and see if you see:
> Course index page 100

## Play with models in debugger

### Parcitice querying
[Querying docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#querying-records)

See `auxilary_code/models_querying.py`.
* Remember about calling function in `if __name__ == '__main__':`.
* Remember about copying `Environment variables` from other run configuration.

#### Define empty functions
