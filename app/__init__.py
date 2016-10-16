from flask import Flask
from flask_login import LoginManager
from pymongo import MongoClient


login_manager = LoginManager()
mongo = MongoClient()


def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)

    global mongo
    mongo = MongoClient(config['MONGODB_URL'])

    login_manager.init_app(app)


    from .views import main
    app.register_blueprint(main)

    return app