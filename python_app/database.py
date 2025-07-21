from mongoengine import connect

def connect_db():
    connect(
        db="testdb",
        host="localhost",
        port=27017
    )
    print("Connected to MongoDB")