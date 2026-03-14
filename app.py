from flask import Flask
from controllers.userController import user_bp
from controllers.HomeController import blueprint_home
from config import Config
from settings.Secret import Secret
from extensions import db, migrate, swagger
from routes.auth import auth_bpc

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #secret 
    aws_secret = Secret()
    secrets = aws_secret.get_secret("api82")
    
    if secrets:
        user = secrets.get("username")
        password = secrets.get("password")
        host = secrets.get("host")
        db_name = secrets.get("dbname")
        app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{user}:{password}@{host}/{db_name}"

    #------
    
    
    
    
    
    db.init_app(app)
    migrate.init_app(app, db)
    swagger.init_app(app)
    
    # Register blueprints
    app.register_blueprint(user_bp, url_prefix="/api/auth")
    app.register_blueprint(blueprint_home, url_prefix="/api")
    app.register_blueprint(auth_bpc, url_prefix="/api/auth")
    
    
    @app.route('/')
    def home():
        return {'msj': '********************hola hello world******************'}

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')