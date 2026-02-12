from repositories.userRepository import userRepository

class AuthService:
    @staticmethod
    def register(username, email, password):
        user = userRepository.create_user(username, email, password)
        return user
