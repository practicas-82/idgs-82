from flask import Blueprint, request, jsonify
from sqlalchemy import true
from auth.cognito_service import create_cognito_user
from models import User
from extensions import db


auth_bpc = Blueprint("cognito_auth", __name__)

@auth_bpc.route("/register", methods=["POST"])
def register():
    """
    REGISTRAR UN USUARIO
    ---
    tags:
        - cognito
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
            password:
              type: string
            nombre:
              type: string
    responses:
        201:
            description: Usuario registrado exitosamente
        400:
            description: Error en la solicitud
    """
    data = request.json
    email = data.get("email")
    password = data.get("password")
    nombre = data.get("nombre")

    if not email or not password:
        return jsonify({"error": "Email y contraseña son requeridos"}), 400

    try:
        # Crear usuario en Cognito
        #create_cognito_user(email, password)
        sub = create_cognito_user(email, password)

        # Guardar usuario en la base de datos local
        #new_user = User(email=email, nombre=nombre)
        #db.session.add(new_user)
        #db.session.commit()
        
        user = User(email=email, cognito_sub=sub)
        db.session.add(user)
        db.session.commit()
        
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500