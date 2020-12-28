import face_recognition
import numpy as np
from libs import connection, fields


def get_collection():
    """
    Return the DATABASE collection main that utilice the system
    """
    return connection.get_collection()


def upload_file(identification, file_path=None, binary=None):
    """
    Register matrix with Encodings of a face to DataBase
    """
    collection = get_collection()
    doc_people = collection.find_one({fields.get_field_main(): identification})
    if doc_people:
        print('{0} Already Registered'.format(identification))
        exit()
    if binary is not None:
        image = face_recognition.load_image_file(binary)
    else:
        image = face_recognition.load_image_file(file_path)
    face_location = face_recognition.face_locations(image, model='cnn')
    face_encoding = face_recognition.face_encodings(image, known_face_locations=face_location)
    if len(face_encoding) == 0:
        print("error to find face")
        exit()
    document = {
        fields.get_field_main(): identification,
        'encode': face_encoding[0].tolist()
    }
    result = collection.insert_one(document)
    return str(result.inserted_id)


def get_list_identification():
    """
    Return list of identifications from database
    """
    collection = get_collection()
    identifications = collection.find({'field': [fields.get_field_main()]})
    return identifications


def compare_pictures(paths=None, binaries=None):
    """
    Compare a list pictures to evaluate an identity
    """
    list_distances = []
    collection = get_collection()
    people = collection.find()
    if binaries is not None:
        image = face_recognition.load_image_file(binaries)
    else:
        image = face_recognition.load_image_file(paths)
    face_encoding = face_recognition.face_encodings(image)
    for p in people:
        distance = face_recognition.face_distance(np.matrix(p.get('encode')), face_encoding[0])
        if distance.tolist()[0] < connection.get_tolerance():
            list_distances.append(
                {fields.get_field_main(): p.get(fields.get_field_main()), 'distance': distance.tolist()[0]})
    return list_distances
