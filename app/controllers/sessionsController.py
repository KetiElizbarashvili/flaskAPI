from flask import Blueprint, request
from app.services.sessionService import sessionService

class SessionController:
    session = Blueprint('sessions', __name__)

    @staticmethod
    @session.route('/', methods=['POST'])
    def signin(): return sessionService.index()
