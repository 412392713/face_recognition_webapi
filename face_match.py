# -*- coding: utf-8 -*-
import face_recognition
from flask import Flask, jsonify, request, redirect
from face_util import allowed_file
import os


def face_match():
    if request.method == 'POST':
        img1 = request.files['img1']
        img2 = request.files['img2']

        if img1 and img2 and allowed_file(img1) and allowed_file(img2):
            file_path1 = os.path.join(os.getcwd(),img1)
            file_path2 = os.path.join(os.getcwd(),img2)
            return detect_faces_in_image(file_path1, file_path2, request.values.get("tolerance"))

    return '''
    <!doctype html>
    <title>人像匹配</title>
    <h1>人像匹配</h1>
    <form method="POST" enctype="multipart/form-data">
      图片路径1：<input type="text" name="img1">
	  图片路径2：<input type="text" name="img2">
      <br/>
      ----------参数：越小越严格---------------
      <br/>
	  <input type="text" name="tolerance" value="0.4">
      <br/>
      <input type="submit" value="提交">
      <br/>
      <br/>
      <br/>
      --------------说明----------------------------
      返回：
      {
        "is_match": 是否匹配(true/false)
      }
      <br/>
      <br/>
      <br/>
    </form>
    '''

def detect_faces_in_image(file_stream1, file_stream2, tolerance):
    img1 = face_recognition.load_image_file(file_stream1)
    known_face_encoding = face_recognition.face_encodings(img1)
	
    img2 = face_recognition.load_image_file(file_stream2)
    unknown_face_encodings = face_recognition.face_encodings(img2)

    is_match = False
    tolerance_num = 0.4
    if tolerance:
        tolerance_num = float(tolerance)

    if len(unknown_face_encodings) > 0:
        match_results = face_recognition.compare_faces(known_face_encoding, unknown_face_encodings[0], tolerance_num)
        #print(jsonify(match_results))
        if match_results[0]:
            is_match = True

    # Return the result as json
    result = {
        "is_match": is_match
    }
    return jsonify(result)