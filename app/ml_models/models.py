from app import db


class MLModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    pickle_filename = db.Column(db.String(256), unique=True, nullable=False)

    def __repr__(self):
        return f'<MLModel {self.model_name}>'
