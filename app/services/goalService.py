
from flask import jsonify
from app.models.goalModel import GoalModel

class goalService:
    @staticmethod
    def index():
        # GoalModel.something()
        return jsonify({'a': 1})