from sqlalchemy.ext.automap import automap_base

from ml_runner import db

Base = automap_base()

engine = db.engine

Base.prepare(engine, reflect=True)

ReflectedUser = Base.classes.user
ReflectedShortMessageService = Base.classes.short_message_service
