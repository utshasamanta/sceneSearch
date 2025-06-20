from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI, server_api=ServerApi)
client.admin.command("ping")
print("Query MongoDB connection successful")

MediaCollection = client[os.getenv("CLUSTER")]["medias"]


def vectorQuery(indexName, dbField, vector):
    pipeline = [
        {
            "$vectorSearch": {
                "index": indexName,
                "path": dbField,
                "queryVector": vector,
                "numCandidates": 20,
                "limit": 5
            }
        }, 
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "url": 1,
                "mediaContext": 1,
                "mediaVector": 0,
                "mediaTranscript": 1,
                "transcriptVector": 0,
                "score": {
                    "$meta": "vectorSearchScore"
                }
            }
        }
    ]

    result = MediaCollection.aggregate(pipeline)
    return result

