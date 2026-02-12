from flask import Flask
from controllers.userController import user_bp
from controllers.HomeController import blueprint_home
from config import Config
from extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    app.register_blueprint(user_bp, url_prefix="/api/auth")
    app.register_blueprint(blueprint_home, url_prefix="/api")
    
    
    @app.route('/')
    def home():
        return {'msj': '********************hola hello world******************'}

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')