import os
from datetime import timedelta
from app.shared.db import db
from app.controllers import controllers
from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv()
def app(app):
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=1)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', '\x92\xb4\x1c\x17\xb3\xb7\x8f\x1bK\xae1\xcd&V\xe6r')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    from .models import userModel, goalModel, sessionModel, workoutModel, planModel
    db.create_all()

    JWTManager(app)
    app.register_blueprint(controllers())
    return app

