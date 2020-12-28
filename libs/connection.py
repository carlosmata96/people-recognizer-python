import parameters
from pymongo import MongoClient


def get_tolerance():
    """
    Return the tolerance accepted to evaluate encoders matrix saved in database
    """
    return parameters.TOLERANCE


def get_collection_name():
    """
    Return the name collection name used for save matrix encoders of faces
    """
    return parameters.COLLECTION_NAME


def get_database_name():
    """
    Return the name database used for the recognition system
    """
    return parameters.DATABASE_NAME


def get_url_mongo():
    """
    Return the url used for connect the system recognition to database
    """
    return parameters.URL_MONGO


def get_collection():
    """
    Return the collection that use for operations basics
    """
    client = MongoClient(get_url_mongo())
    db = client.get_database(get_database_name())
    return db.get_collection(get_collection_name())