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
            landmarks = face_recognition.face_landmarks(face_recognition.load_image_file(img1))
            #print(jsonify(landmarks))
            result = {
                landmarks : landmarks
            }
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