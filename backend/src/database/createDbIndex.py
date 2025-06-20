from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.operations import SearchIndexModel
import os
from dotenv import load_dotenv
import time


load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI, server_api=ServerApi)
client.admin.command("ping")
print("Index MongoDB connection successful")

cluster = client[os.getenv("CLUSTER")]
col = cluster["medias"]

contextIndexModel = SearchIndexModel(
    definition={
        "fields": [
            {
                "type": "vector",
                "path": "context_embedding",
                "numDimensions": 1024,
                "similarity": "dotProduct",
                "quantization": "scalar"
            }
        ]
    },
    name="context_index",
    type="vectorSearch"
)


transcriptIndexModel = SearchIndexModel(
    definition={
        "fields": [
            {
                "type": "vector",
                "path": "transcript_embedding",
                "numDimensions": 1024,
                "similarity": "dotProduct",
                "quantization": "scalar"
            }
        ]
    },
    name="transcript_index",
    type="vectorSearch"
)


allSearchIndex = list(col.list_search_indexes())
searchIndexNames = [idx["name"] for idx in allSearchIndex]

if "context_index" not in searchIndexNames:
    try:
        res = col.create_search_index(model=contextIndexModel)
        print("Polling to see if context search index is ready")
        predicate = None
        if predicate is None:
            predicate = lambda index: index.get("queryable") is True
        
        while True:
            indices = list(col.list_search_indexes(res))
            if len(indices) and predicate(indices[0]):
                break
            time.sleep(5)

        print(res + " is ready to query")
    except Exception as e:
        print("Context index creation failed: ", e)


if "transcript_index" not in searchIndexNames:
    try:
        res = col.create_search_index(model=contextIndexModel)
        print("Polling to see if transcript search index is ready")
        predicate = None
        if predicate is None:
            predicate = lambda index: index.get("queryable") is True
        
        while True:
            indices = list(col.list_search_indexes(res))
            if len(indices) and predicate(indices[0]):
                break
            time.sleep(5)

        print(res + " is ready to query")
    except Exception as e:
        print("Transcript index creation failed: ", e)


if "name_1" not in (list(col.index_information())):
    try:
        col.create_index([("name")], unique=True)
        print("Created unique index on name")
    except Exception as e:
        print("Index creation failed: ", e)