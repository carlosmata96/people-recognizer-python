import sys
import face_recognition
import numpy as np
from libs import connection

"""
Return the DATABASE collection main that utilice the system
"""
def get_collection():
    return connection.get_collection()


"""
Register matrix with Encodings of a face to DataBase
"""
def upload_file(filePath, identification):
    collection = get_collection()
    people = sys.argv[1]
    filePath = sys.argv[2]
    docPeople = collection.find_one({'name': people})
    if docPeople:
        print('{0} ya se encuentra registrado/a'.format(people))
        exit()
    image = face_recognition.load_image_file(filePath)
    face_location = face_recognition.face_locations(image, model='cnn')
    face_encoding = face_recognition.face_encodings(image, known_face_locations=face_location)
    if len(face_encoding) == 0:
        print("error to find face")
        exit()
    document = {
        'name': people,
        'encode': face_encoding[0].tolist()
    }
    result = collection.insert_one(document)
    print(result.inserted_id)


"""
Compare a list pictures to evaluate an identity
"""
def compare_pictures(pictures):
    listDistances = []
    collection = get_collection()
    people = collection.find()
    image = face_recognition.load_image_file(pictures)
    face_encoding = face_recognition.face_encodings(image)

    for p in people:
        distance = face_recognition.face_distance(np.matrix(p.get('encode')), face_encoding[0])
        if distance.tolist()[0] < connection.get_tolerance():
            listDistances.append({'name': p.get('name'), 'distance': distance.tolist()[0]})
    return listDistances
