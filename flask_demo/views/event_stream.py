from flask_demo import app
from flask import Response, render_template

import time


@app.route("/event_source")
def event_source():

    def generate():
        count = 0
        while count < 20:
            count += 1
            yield "data: %s\n\n" % count
            time.sleep(0.3)
        yield "data: \n\n"

    resp = Response(generate(), mimetype="text/event-stream")
    return resp


@app.route("/event_index")
def event_index():

    return render_template("source_event.html")