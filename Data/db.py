import pymongo
from dotenv import load_dotenv
import os


class MongoDB:
    _instance = None

    @staticmethod
    def get_instance():
        if MongoDB._instance is None:
            MongoDB()
        return MongoDB._instance['wikiAPI']

    def __init__(self):
        if MongoDB._instance is not None:
            raise Exception("This class is a Singleton!")
        else:
            load_dotenv()
            MONGO_STRING = os.environ.get("MONGO_STRING")
            MongoDB._instance = pymongo.MongoClient(MONGO_STRING)