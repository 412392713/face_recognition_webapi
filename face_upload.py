# -*- coding: utf-8 -*-
import face_recognition
import os
from flask import Flask, jsonify, request, redirect
from werkzeug import secure_filename
from datetime import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#上传文件
def face_upload():
    if request.method == 'POST':
        if 'img1' not in request.files:
            return redirect(request.url)

        img1 = request.files['img1']

        if img1.filename == '':
            return redirect(request.url)

        if img1 and allowed_file(img1.filename):
            dt=datetime.now() #创建一个datetime类对象
            dt.strftime( '%Y-%m-%d %H:%M:%S %f')
            path = os.path.join(os.getcwd(), 'upload', dt.strftime('%Y%m'))
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = os.path.join(path, dt.strftime('%Y%m%d%H%M%S%f_')+ secure_filename(img1.filename))
            img1.save(file_path)
            result = {
                'filePath' : file_path
            }
            return jsonify(result)

    return '''
    <!doctype html>
    <title>Face Upload</title>
    <h1>上传文件</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="img1">
      <br/>
      <input type="submit" value="提交">
    </form>
    '''