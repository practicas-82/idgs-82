from extensions import db
from passlib.hash import pbkdf2_sha256


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password: str):
        # Truncate to 72 bytes to avoid issues with some hashing algorithms
        password_bytes = password.encode("utf-8")[:72]
        self.password = pbkdf2_sha256.hash(password_bytes)

    def check_password(self, password: str) -> bool:
        password_bytes = password.encode("utf-8")[:72]
        return pbkdf2_sha256.verify(password_bytes, self.password)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}
