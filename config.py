import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    ENV = os.getenv("FLASK_ENV")
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("SQLALCHEMY_DATABASE_URI")
        or "mysql+pymysql://root:@localhost:3306/api_82"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
