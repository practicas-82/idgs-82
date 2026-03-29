from flask import Blueprint, request, jsonify
from services.authService import AuthService

user_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    
    # Validar que los datos requeridos estén presentes
    if not data:
        return jsonify({"message": "Request body is required"}), 400
    
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    
    if not username or not email or not password:
        return jsonify({"message": "username, email and password are required"}), 400
    
    try:
        user = AuthService.register(username, email, password)
        return (
            jsonify({"message": "Usuario creado", "user": user.username}),
            201,
        )
    except ValueError as e:
        return jsonify({"message": "Validation error", "error": str(e)}), 400
    except Exception as e:
        return jsonify({"message": "Registration failed", "error": str(e)}), 500

