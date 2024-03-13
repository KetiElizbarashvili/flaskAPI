from flask import Flask
from app.app import app

if __name__ == '__main__':
    Flasky = Flask(__name__)
    with Flasky.app_context():
        app = app(Flasky)
        app.run(debug=True)