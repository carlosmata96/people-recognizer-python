from pymongo import MongoClient
import sys
import face_recognition
import parameters

client = MongoClient(parameters.URL_MONGO)
db = client.get_database(parameters.DATABASE_NAME)
collection = db.get_collection(parameters.COLLECTION_NAME)
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