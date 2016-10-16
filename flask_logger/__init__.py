import queue
import logging

from logging.handlers import QueueListener, QueueHandler


class FlaskLogger(object):


    que = queue.Queue(-1)
    queue_handler = QueueHandler(que)
    handler = logging.StreamHandler()
    listener = QueueListener(que, handler)
    root = logging.getLogger('aa')
    root.addHandler(queue_handler)
    fotmatter = logging.Formatter('%(threadName)s: %(message)s')
    handler.setFormatter(fotmatter)
    listener.start()
    logging.warning('haha')
    logging.error('heihie')
    listener.stop()

a1 = logging.getLogger('aa')
a2 = logging.getLogger('aa')

print(a1 is a2)
print(a2.handlers)