from flask import Flask
from flask_login import LoginManager
from pymongo import MongoClient
from flask_logger import FlaskLogger
from flask_demo.models import VedioDAO


login_manager = LoginManager()
flask_logger = FlaskLogger()
database = MongoClient()
vedio_dao = VedioDAO(database)


app = Flask(__name__)

login_manager.init_app(app)
flask_logger.init_app(app)


from . import views