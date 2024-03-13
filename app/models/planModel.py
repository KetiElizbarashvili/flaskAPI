from app.shared.db import db

class PlanModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.String(50), unique=True, nullable=False)