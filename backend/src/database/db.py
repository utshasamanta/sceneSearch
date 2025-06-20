from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.operations import SearchIndexModel
import os
from dotenv import load_dotenv
import time


load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

def connectDB():
    try:
        client = MongoClient(MONGODB_URI, server_api=ServerApi("1"))
        client.admin.command("ping")
        print("MongoDB connection succesful")

        # cluster = client[os.getenv("CLUSTER")]
        # col = cluster["medias"]

        # contextIndexModel = SearchIndexModel(
        #     definition={
        #         "fields": [
        #             {
        #                 "type": "vector",
        #                 "path": "context_embedding",
        #                 "numDimensions": 1024,
        #                 "similarity": "dotProduct",
        #                 "quantization": "scalar"
        #             }
        #         ]
        #     },
        #     name="vector_index",
        #     type="vectorSearch"
        # )


        # res = col.create_search_index(model=contextIndexModel)
        # print("Polling to check if the index is ready")
        # predicate = None
        # if predicate is None:
        #     predicate = lambda index: index.get("queryable") is True
        
        # while True:
        #     indices = list(col.list_search_indexes(res))
        #     if len(indices) and predicate(indices[0]):
        #         break
        #     time.sleep(5)
        # print(res + " is ready")

        
        # if "name_1" not in (list(col.index_information())):
        #     try:
        #         col.create_index([("name")], unique=True)
        #         print("Created unique index on name")
        #     except Exception as e:
        #         print("Index creation failed: ", e)

        return client
    except Exception as err:
        print("MongoDB Connection failed", err)

