import pymongo
from pymongo import  MongoClient
import certifi
nom=certifi.where()




client = pymongo.MongoClient('mongodb+srv://test:test@cluster0.nqkny.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', ssl=True)

db = client["test"]
collection=db["test"]
post ={"_id":7,"name":"tim","score":5}
collection.insert_one(post)




