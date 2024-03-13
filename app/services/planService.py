
from flask import jsonify
from app.models.planModel import PlanModel

class planService:
    @staticmethod
    def index():
        # PlanModel.something()
        return jsonify({'a': 1})