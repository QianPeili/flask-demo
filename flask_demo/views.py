from flask_demo import app
from flask import current_app, request


@app.route('/')
@app.route('/index')
def index():
    return "Hi, this is index, Welcome!"


@app.route('/log_test')
def log_test():
    current_app.logger.info('my test log')
    return "Send a log."

@app.route('/videos/upload')
def vedio_upload():
    pass
