# -*- coding: utf-8 -*-
import face_recognition
import os
from flask import Flask, jsonify, request, redirect
from werkzeug import secure_filename
from datetime import datetime
from face_util import allowed_file
from face_util import file_ext


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
            path = os.path.join('upload', dt.strftime('%Y%m'))
            if not os.path.exists(os.path.join(os.getcwd(), path)):
                os.makedirs(path)
            filename = dt.strftime('%Y%m%d%H%M%S%f_.')+ file_ext(img1.filename)
            file_path = os.path.join(os.getcwd(),path, filename)
            img1.save(file_path)
            result = {
                'filePath' : os.path.join(path, filename)
            }
            return jsonify(result)

    return '''
    <!doctype html>
    <title>Face Upload</title>
    <h1>上传文件</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="img1">
      <br/><br/>
      <input type="submit" value="提交">
    </form>
    <br/>
      <br/>
      <br/>
      --------------说明----------------------------<br/>
      调用其他接口之前，先上传图片。图片路径可以多次使用。
      
      返回：
      {
        'filePath' : 图片路径
      }
      <br/>
      <br/>
      <br/>
    
    '''