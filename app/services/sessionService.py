
from flask import jsonify
from app.models.sessionModel import SessionModel

class sessionService:
    @staticmethod
    def index():
        # SessionModel.something()
        return jsonify({'a': 1})