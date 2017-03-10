from flask import Flask
from pymongo import MongoClient
# from flask_logger import FlaskLogger
from flask_demo.models import VideoDAO


# flask_logger = FlaskLogger()
database = MongoClient("mongodb://localhost")
video_dao = VideoDAO(database)


app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'flask-demo'

# flask_logger.init_app(app)


import views