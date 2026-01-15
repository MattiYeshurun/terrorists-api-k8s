from pydantic import BaseModel
from pymongo import MongoClient
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
        db = client.threat_db
        collection = db.top_threats
    t = {
        "name": "Alpha",
        "location": "Metropolis",
        "danger_rate": 10
    }

    my_data = get_top_threats(t)
    print(my_data)

