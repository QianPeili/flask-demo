import queue
import logging

from logging.handlers import QueueListener, QueueHandler


class FlaskLogger(object):

    def __init__(self):
        self.que = queue.Queue(-1)
        self.queue_handler = QueueHandler(self.que)
        self.queue_handler.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(
            '/usr/local/var/log/flask_app.log')
        self.listener = QueueListener(
            self.que, file_handler,
            respect_handler_level=logging.INFO)

    def init_app(self, app):

        app.logger.addHandler(self.queue_handler)
        self.listener.start()