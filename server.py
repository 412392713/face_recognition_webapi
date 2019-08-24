# -*- coding: utf-8 -*-
from flask import Flask
from face_distance import face_distance
from face_match import face_match
from face_locat import face_locat
from face_landmarks_alive import face_landmarks_alive
from face_upload import face_upload


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/face_upload', methods=['GET', 'POST'])
def face_upload_f():
    return face_upload()
    
@app.route('/face_alive', methods=['GET', 'POST'])
def face_landmarks_alive_f():
    return face_landmarks_alive()

@app.route('/face_match', methods=['GET', 'POST'])
def face_match_f():
    return face_match()
    
@app.route('/face_locat', methods=['GET', 'POST'])
def face_locat_f():
    return face_locat()

@app.route('/face_distance', methods=['GET', 'POST'])
def face_distance_f():
    return face_distance()

@app.route('/', methods=['GET', 'POST'])
def index():
    return '''
    <!doctype html>
    <title>人脸识别</title>
    <p> <a href="face_upload" target="mainframe">图片上传</a> 
    &nbsp;&nbsp; <a href="face_locat" target="mainframe">人像定位</a>
    &nbsp;&nbsp; <a href="face_match" target="mainframe">图片匹配</a>
    &nbsp;&nbsp; <a href="face_alive" target="mainframe">活体识别</a></p>
    <iframe src="face_upload" id="mainframe" name="mainframe" width="100%" height="100%"></iframe>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
