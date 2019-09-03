# -*- coding: utf-8 -*-
import face_recognition
from flask import Flask, jsonify, request, redirect
from face_util import allowed_file
import os

def face_locat():
    if request.method == 'POST':
        img1 = request.values.get("img1")
        #print img1
        if img1 and allowed_file(img1):
            file_path = os.path.join(os.getcwd(),img1)
            result = face_recognition.face_locations(face_recognition.load_image_file(file_path))
            #print(jsonify(result))
            return jsonify(result)

    return '''
    <!doctype html>
    <title>Face Location</title>
    <h1>人像定位</h1>
    <form method="POST" enctype="multipart/form-data">
      图片路径1：<input type="text" name="img1">
      <br/><br/>
      <input type="submit" value="提交">
    </form>
    <br/>
      <br/>
      <br/>
      --------------说明----------------------------<br/>
      注意返回的坐标顺序
      (top, right, bottom, left)
      
      <br/>
      <br/>
      <br/>
    
    '''