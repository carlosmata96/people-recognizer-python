from pymongo import MongoClient
import sys
import face_recognition
import numpy
import parameters

TOLERANCE = parameters.TOLERANCE

client = MongoClient(parameters.URL_MONGO)
db = client.get_database(parameters.DATABASE_NAME)
collection = db.get_collection(parameters.COLLECTION_NAME)

fileCompare = sys.argv[1]

listDistances = []

people = collection.find()
image = face_recognition.load_image_file(fileCompare)
face_encoding = face_recognition.face_encodings(image)

for p in people:
    distance = face_recognition.face_distance(numpy.matrix(p.get('encode')), face_encoding[0])
    if distance.tolist()[0] < TOLERANCE:
        listDistances.append({'name': p.get('name'), 'distance': distance.tolist()[0]})
print(listDistances)