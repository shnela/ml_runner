from ml_runner.reflected_models import Base


if __name__ == '__main__':
    # analyze Base.classes
    # `dir`: https://www.w3schools.com/python/ref_func_dir.asp
    print(dir(Base.classes))  # or use debugger
    print([e for e in dir(Base.classes) if not e.startswith('__')])

    # what's inside particular class?
    # SA: https://stackoverflow.com/questions/2537471/method-of-iterating-over-sqlalchemy-models-defined-columns
    print(Base.classes.user.__table__.columns)
    print(Base.classes.short_message_service.__table__.columns)
    print(Base.classes.short_message_service.__table__.foreign_keys)
