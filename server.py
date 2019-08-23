from flask import Flask
from face_distance import face_distance
from face_match import face_match

app = Flask(__name__)

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
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
