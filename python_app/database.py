from pymongo import MongoClient

def connect_to_database():
    client = MongoClient("mongodb://uzair:uzairyasin123@localhost:27017/my_database?authSource=admin")
    db = client["my_database"]
    collection = db["products"] 
    print("Connected to MongoDB")
    return collection






































































































# def connect_to_database():
#     client = MongoClient("mongodb://uzair:uzairyasin123@localhost:27017/my_database?authSource=admin")
#     db = client["my_database"]
#     collection = db["products"]
#     print("Connected to MongoDB")
#     return collection


