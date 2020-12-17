# Several databases

[README_PREVIOUS.md](./README_PREVIOUS.md)

## Update environment
Add other database to `SQLALCHEMY_DATABASE_URI2`

## Flask multi database support
https://flask-appbuilder.readthedocs.io/en/latest/multipledbs.html

## Just use `__table_args__ = {'extend_existing': True}`
https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Table.params.extend_existing

