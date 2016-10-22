from flask import Flask
from flask_login import LoginManager
from pymongo import MongoClient
from flask_logger import FlaskLogger


login_manager = LoginManager()
mongo = MongoClient()
flask_logger = FlaskLogger()


def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)

    global mongo
    mongo = MongoClient(config['MONGODB_URL'])

    login_manager.init_app(app)
    flask_logger.init_app(app)

    return app


app = create_app({'MONGODB_URL': "mongodb://localhost"})

from . import views