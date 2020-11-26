import os

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import relationship

from ml_runner import db

Base = automap_base()


if os.environ.get('DO_NOT_REFLECT'):
    ReflectedUser = None
    ReflectedPost = None

else:
    # when generating db, reflecting db will cause errors

    # class ReflectedUser(Base):
    #     __tablename__ = 'user'
    #     posts = relationship("post", collection_class=list, backref='user')

    engine = db.engine
    Base.prepare(engine, reflect=True)

    ReflectedUser = Base.classes.user
    ReflectedPost = Base.classes.post
