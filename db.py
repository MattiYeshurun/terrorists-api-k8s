from pydantic import BaseModel
from pymongo import MongoClient, errors
import os

class Terrorists(BaseModel):
    name: str
    lucation: str
    danger_rate: int

    def to_dict(self):
        return{
            "name": self.name,
            "location": self.lucation,
            "danger_rate": self.danger_rate
        }
    
class DataTerrorists:
    def __init__(self):
        host = os.getenv("MONGO_HOST", "localhost")
        port = os.getenv("MONGO_PORT", "27017")

        self.client = MongoClient(f"mongodb://{host}:{port}/", serverSelectionTimeoutMS=5000)
        self.db = self.client["threat_db"]
        self.collection = self.db["top_threats"]
        print("connected to MongoDB!")

    def get_top_threats(self, data: dict):
        terrorists_list = []
        for doc in self.collection.find():
            threat = Terrorists(
                name=doc["name"],
                lucation=doc["lucatione"],
                danger_rate=doc["danger_rate"]
            )
            terrorists_list.append(threat)
        return terrorists_list

    def get_database():
        client = MongoClient('mongodb://localhost:27017/')
        db = client["threat_db"]
        collection = db["top_threats"]
    t = {
        "name": "Alpha",
        "location": "Metropolis",
        "danger_rate": 10
    }

    my_data = get_top_threats(t)
    print(my_data)


# # Replace '<connection-string>' with your actual MongoDB connection string
# connection_string = "mongodb://localhost:27017/"

# # Connect to MongoDB
# try:
#    client = MongoClient(connection_string)
#    print("Successfully connected to MongoDB.")
# except errors.ConnectionError as e:
#    print("Failed to connect to MongoDB:", e)
#    exit()

# # Access the database and collection
# database = client["threat_db"]
# collection = database["top_threats"]

# # Insert a document into the collection
# try:
#    result = collection.insert_one({"title": "Back to the Future"})
#    print(f"Document inserted with _id: {result.inserted_id}")
# except Exception as e:
#    print("Failed to insert document:", e)

# # List search indexes for the collection (ensure method exists)
# try:
#    cursor = collection.list_search_indexes()
#    indexes = list(cursor)  # Convert cursor to list for ease
#    if indexes:
#       print("Search indexes found:")
#       for index in indexes:
#             print(index)
#    else:
#       print("No search indexes found.")
# except Exception as e:
#    print("Failed to list search indexes:", e)

# # Close the client connection (Optionally used here for resource management)
# client.close()