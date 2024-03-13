from flask import Blueprint, request
from app.services.planService import planService

class PlanController:
    plan = Blueprint('plan', __name__)

    @staticmethod
    @plan.route('/', methods=['POST'])
    def signin(): return planService.index()