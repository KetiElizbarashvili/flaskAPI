# controllers/__init__.py

from flask import Blueprint
from app.controllers import authController
from app.controllers import goalsController
from app.controllers import plansController
from app.controllers import sessionsController
from app.controllers import workoutsController

def controllers():
    root = Blueprint('api', __name__, url_prefix='/api')
    root.register_blueprint(authController.AuthController.auth, url_prefix='/auth')
    root.register_blueprint(goalsController.GoalController.goal, url_prefix='/goals')
    root.register_blueprint(plansController.PlanController.plan, url_prefix='/plans')
    root.register_blueprint(sessionsController.SessionController.session, url_prefix='/sessions')
    root.register_blueprint(workoutsController.WorkoutController.workout, url_prefix='/workouts')
    return root