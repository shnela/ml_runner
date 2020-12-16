from ml_runner import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    msisdn = db.Column(db.Text(16), nullable=False, unique=True)


class ShortMessageService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    send_date = db.Column(db.DateTime(), nullable=False)
    sending_party_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sent_party_id = db.Column(db.Integer, db.ForeignKey('user.id'))
