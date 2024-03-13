
from flask import jsonify
from app.models.workoutModel import WorkoutModel

class workoutService:
    @staticmethod
    def index():
        # WorkoutModel.something()
        return jsonify({'a': 1})