
from flask import jsonify
from flask_jwt_extended import create_access_token
from app.models.userModel import UserModel

class authService:
    @staticmethod
    def signIn(email, password):
        # Find the user by username
        user = UserModel.query.filter_by(email=email).first()

        # Check if the user exists and the password is correct
        if user and user.check_password(str(password)):
            # Generate JWT token
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({'message': 'Invalid username or password'}), 401

    @staticmethod
    def signUp(email, password):
        # Check if the username is already taken
        if UserModel.query.filter_by(email=email).first():
            return jsonify({'message': 'Username already exists'}), 400

        # Create a new user
        new_user = UserModel(email=email)
        new_user.set_password(str(password))
        UserModel.createNew(NewUser=new_user)

        return jsonify({'message': 'User created successfully'}), 201
