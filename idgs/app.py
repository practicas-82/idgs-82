from flask import Flask
from controllers.HomeController import blueprint_home
from extensions import db, migrate
from models import user
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    
    
    
    app.register_blueprint(blueprint_home)
    @app.route('/')
    def home():
        return {'mensaje': 'hola mundo hhhh'}, 400   

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5001)