# -*- coding: utf-8 -*-
import face_recognition
from flask import Flask, jsonify, request, redirect


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def face_landmarks_alive():
    if request.method == 'POST':
        if 'img1' not in request.files:
            return redirect(request.url)

        img1 = request.files['img1']

        if img1.filename == '':
            return redirect(request.url)

        if img1 and allowed_file(img1.filename):
            result = {
                #landmarks : {},
                'openMouth' : False,
                'closeEyes' : False,
                'lookLeft' : False,
                'lookRight' : False
            }
            landmarks = face_recognition.face_landmarks(face_recognition.load_image_file(img1))
            #print(jsonify(landmarks))
            if len(landmarks) > 0 :
                result['landmarks'] = landmarks[0]
                #取到边框
                min_x=min_y=10000
                max_x=max_y=0
                for k in landmarks[0]:
                    for p in landmarks[0][k] : 
                        min_x = min(min_x, p[0])
                        min_y = min(min_y, p[1])
                        max_x = max(max_x, p[0])
                        max_y = max(max_y, p[1])
                #判断张嘴
                lip_top = landmarks[0]["top_lip"][9]
                lip_bottom = landmarks[0]["bottom_lip"][9]
                lip = abs((lip_top[1] - lip_bottom[1]) / (max_y - min_y))
                if lip > 0.03 :
                    result['openMouth'] = True
                print('lip='+lip)
                
            
            return jsonify(result)

    return '''
    <!doctype html>
    <title>face_landmarks_alive</title>
    <h1>Chose Images</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="img1">
      <input type="submit" value="Upload">
    </form>
    '''