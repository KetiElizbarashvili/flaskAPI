from app.shared.db import db

class GoalModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(50), unique=True, nullable=False)