from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv


load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

def connectDB():
    try:
        client = MongoClient(MONGODB_URI, server_api=ServerApi("1"))
        client.admin.command("ping")
        print("MongoDB connection succesful")

        cluster = client[os.getenv("CLUSTER")]
        col = cluster["medias"]
        
        if "name_1" not in (list(col.index_information())):
            try:
                col.create_index([("name")], unique=True)
                print("Created unique index on name")
            except Exception as e:
                print("Index creation failed: ", e)

        return client
    except Exception as err:
        print("MongoDB Connection failed", err)

