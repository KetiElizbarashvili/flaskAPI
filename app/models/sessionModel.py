from app.shared.db import db

class SessionModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session = db.Column(db.String(50), unique=True, nullable=False)