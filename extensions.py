from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger


db = SQLAlchemy()
migrate = Migrate()

swagger = Swagger(
    template={
        "swagger": "2.0",
        "info": {
            "title": "My API 82",
            "description": "Documentacion de usuarios",
            "version": "1.0.0",
        },
        "securityDefinitions": {
            "BearerAuth": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "coloca tu Bearer <tu-token>",
            }
        },
    }
)
