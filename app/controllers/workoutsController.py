from flask import Blueprint, request
from app.services.workoutService import workoutService

class WorkoutController:
    workout = Blueprint('workout', __name__)

    @staticmethod
    @workout.route('/', methods=['POST'])
    def signin(): return workoutService.index()