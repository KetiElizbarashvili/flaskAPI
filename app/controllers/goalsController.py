from flask import Blueprint, request
from app.services.goalService import goalService

class GoalController:
    goal = Blueprint('goals', __name__)

    @staticmethod
    @goal.route('/', methods=['POST'])
    def signin(): return goalService.index()