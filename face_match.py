import face_recognition
from flask import Flask, jsonify, request, redirect


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def face_match():
    if request.method == 'POST':
        if 'img1' not in request.files or 'img2' not in request.files:
            return redirect(request.url)

        img1 = request.files['img1']
        img2 = request.files['img2']

        if img1.filename == '' or img2.filename == '' :
            return redirect(request.url)

        if img1 and img2 and allowed_file(img1.filename) and allowed_file(img2.filename):
            return detect_faces_in_image(img1, img2)

    return '''
    <!doctype html>
    <title>Face Match</title>
    <h1>Chose Tow Images</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="img1">
	  <input type="file" name="img2">
      <input type="submit" value="Upload">
    </form>
    '''

def detect_faces_in_image(file_stream1, file_stream2):
    img1 = face_recognition.load_image_file(file_stream1)
    known_face_encoding = face_recognition.face_encodings(img1)
	
    img2 = face_recognition.load_image_file(file_stream2)
    unknown_face_encodings = face_recognition.face_encodings(img2)

    is_match = False

    if len(unknown_face_encodings) > 0:
        match_results = face_recognition.compare_faces([known_face_encoding], unknown_face_encodings[0], 0.4)
        print(jsonify(match_results))
        if match_results[0][0]:
            is_match = True

    # Return the result as json
    result = {
        "is_match": is_match
    }
    return jsonify(result)