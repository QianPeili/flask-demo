from flask_demo import app, video_dao
from flask import current_app, request, render_template, redirect, url_for, flash


@app.route('/')
@app.route('/index')
def index():
    return "Hi, this is index, Welcome!"


@app.route('/log_test')
def log_test():
    current_app.logger.info('my test log')
    return "Send a log."


@app.route('/videos/upload', methods=['GET', 'POST'])
def video_upload():
    if request.method == 'GET':
        return render_template('video_upload.html')

    if not request.files or 'video' not in request.files:
        flash(u"找不到上传文件", 'warning')
        return redirect(url_for("video_upload"))

    file_obj = request.files['video']
    name = request.form.get('video_name', file_obj.filename)
    video_dao.save_video(request.files['video'], name)
    flash(u"上传成功")
    return redirect(url_for("video_upload"))


