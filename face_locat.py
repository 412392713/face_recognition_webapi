# -*- coding: utf-8 -*-
import face_recognition
from flask import Flask, jsonify, request, redirect


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def face_locat():
    if request.method == 'POST':
        if 'img1' not in request.files:
            return redirect(request.url)

        img1 = request.files['img1']

        if img1.filename == '':
            return redirect(request.url)

        if img1 and allowed_file(img1.filename):
            result = face_recognition.face_locations(face_recognition.load_image_file(img1))
            print(jsonify(result))
            return jsonify(result)

    return '''
    <!doctype html>
    <title>Face Location</title>
    <h1>人像定位</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="img1">
      <br/>
      <input type="submit" value="Upload">
    </form>
    '''