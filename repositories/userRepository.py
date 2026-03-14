from models.user import User
from extensions import db

class userRepository:
    @staticmethod
    def create(username, email, password):
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    # Backwards compatible alias
    @staticmethod
    def create_user(username, email, password):
        return userRepository.create(username, email, password)

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()