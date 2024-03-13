from flask import Blueprint, request
from app.services.authService import authService

class AuthController:
    auth = Blueprint('auth', __name__)

    @staticmethod
    @auth.route('/signin', methods=['POST'])
    def signin():
        return authService.signIn(
            email=request.json.get("email"),
            password=request.json.get("password")
        )

    @staticmethod
    @auth.route('/signup', methods=['POST'])
    def signUp(): return authService.signUp(
            email=request.json.get("email"),
            password=request.json.get("password")
        )