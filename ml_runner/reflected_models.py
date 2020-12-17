from ml_runner import db


class ReflectedUser(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'user'


class ReflectedShortMessageService(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'short_message_service'
    __bind_key__ = 'db2'
