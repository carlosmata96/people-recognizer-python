from flask import Flask, request, jsonify
from re import sub
from io import BytesIO
from base64 import b64decode
from libs import load

app = Flask(__name__)


@app.route('/registerPerson', methods=['POST'])
def load_person():
    data = request.json
    if 'profile_picture' not in data:
        app.logger.error('profile picture not found')
        return 'False'
    identification = data['identification']
    picture = data['profile_picture']
    photo = sub('^data:image/.+;base64,', '', picture)
    return load.upload_file(binary=BytesIO(b64decode(photo)), identification=identification)



@app.route('/recognize', methods=['POST'])
def recognize():
    data = request.json
    if 'picture' not in data:
        app.logger.error('picture not found')
        return 'False'
    photo_base = data['picture']
    photo_comparison = sub('^data:image/.+;base64,', '', photo_base)
    return jsonify(load.compare_pictures(binaries=BytesIO(b64decode(photo_comparison))))
