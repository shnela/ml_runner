from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import relationship

from ml_runner import db

Base = automap_base()


class ReflectedUser(Base):
    __tablename__ = 'user'
    sent_messages = relationship(
        "short_message_service", collection_class=list,
        foreign_keys='short_message_service.sending_party_id', backref='sending_party')
    received_messages = relationship(
        "short_message_service", collection_class=list,
        foreign_keys='short_message_service.sent_party_id', backref='sent_party')


engine = db.engine

Base.prepare(engine, reflect=True)

ReflectedShortMessageService = Base.classes.short_message_service
