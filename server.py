from flask import Flask
from face_distance import face_distance
from face_match import face_match

app = Flask(__name__)

@app.route('/face_match')
def face_match_f():
    return face_match()

@app.route('/face_distance')
def face_distance_f():
    return face_distance()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
