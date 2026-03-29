import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENV = os.getenv('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = 'mysql:///root::@localhost:3306/api_82'
    SQLALCEMY_TRACK_MODIFICATIONS= False
