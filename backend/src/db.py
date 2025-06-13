from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
import certifi

load_dotenv()
ca = certifi.where()
MONGODB_URI = os.getenv("MONGODB_URI")

try:
    client = MongoClient(MONGODB_URI, tls=True, tlsCAFile=ca, server_api=ServerApi("1"))
    client.admin.command("ping")
    print("MongoDB connection succesful")
except Exception as err:
    print("MongoDB Connection failed", err)
