from repositories.userRepository import userRepository
from flask_jwt_extended import create_access_token
from datetime import timedelta


class AuthService:
    @staticmethod
    def register(username, email, password):
        user = userRepository.create(username, email, password)
        return user

    @staticmethod
    def login(username, password):
        user = userRepository.find_by_username(username)
        if not user or not user.check_password(password):
            return None

        claims = {"username": user.username}

        token = create_access_token(
            identity=str(user.id),
            additional_claims=claims,
            expires_delta=timedelta(hours=2),
        )
        return {"access_token": token, "user": username}
