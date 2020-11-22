from app import db
from datetime import datetime


class MLModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    pickle_filename = db.Column(db.String(256), unique=True, nullable=False)
    runs = db.relationship('MLModelRun', backref='ml_model', lazy=True)

    def __repr__(self):
        return f'<MLModel {self.model_name}>'


class MLModelRun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    description = db.Column(db.Text, nullable=True)
    csv_filename = db.Column(db.String(256), unique=True, nullable=False)
    ml_model_id = db.Column(db.Integer, db.ForeignKey('ml_model.id'))

    def __repr__(self):
        return f'<MLModelRun {self.model_name} ({self.created_at})>'
