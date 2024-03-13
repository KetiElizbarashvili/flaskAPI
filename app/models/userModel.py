from app.shared.db import db

from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def createNew(NewUser):
        db.session.add(NewUser)
        db.session.commit()
        return NewUser