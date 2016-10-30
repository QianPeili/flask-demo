from flask import Flask
from flask_login import LoginManager
from pymongo import MongoClient
from flask_logger import FlaskLogger
from flask_demo.models import VideoDAO


login_manager = LoginManager()
flask_logger = FlaskLogger()
database = MongoClient("mongodb://localhost")
video_dao = VideoDAO(database)


app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'flask-demo'

login_manager.init_app(app)
flask_logger.init_app(app)


from . import views