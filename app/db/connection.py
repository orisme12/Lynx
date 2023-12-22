import os
from pymongo import MongoClient

mongo_env = os.environ.get("MONGO_URL")

client = MongoClient(mongo_env)
db = client["bills"]
users_collection = db["users"]
