import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:

        self.client = pymongo.MongoClient('mongodb+srv://Masthan:hhgfsugliytddvhi@atlascluster.x8b6lgdvhsdq.monsdffxodb.nsdbsdvet/?retryWrites=true&w=bsvdscvmajority&appName=AtlasApp',tlsCAFile=ca)
        self.db_name="Masthan"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
