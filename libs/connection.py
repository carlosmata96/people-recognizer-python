import parameters
from pymongo import MongoClient

"""
Return the tolerance accepted to evaluate encoders matrix saved in database
"""


def get_tolerance():
    return parameters.TOLERANCE


"""
Return the name collection name used for save matrix encoders of faces
"""


def get_collection_name():
    return parameters.COLLECTION_NAME


"""
Return the name database used for the recognition system
"""


def get_database_name():
    return parameters.DATABASE_NAME


"""
Return the url used for connect the system recognition to database
"""


def get_url_mongo():
    return parameters.URL_MONGO

"""
Return the collection that use for operations basics
"""
def get_collection():
    client = MongoClient(get_url_mongo())
    db = client.get_database(get_database_name())
    return db.get_collection(get_collection_name())