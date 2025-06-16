from fastapi import FastAPI, Request, HTTPException, UploadFile
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
from models.mediaModel import Media
from models.mediaModel import MediaCreate
from pymongo.errors import DuplicateKeyError, PyMongoError
from utilities.db import connectDB
from bson import ObjectId
import os
from dotenv import load_dotenv
from utilities.s3 import uploadFileToS3
import tempfile
import shutil

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    cluster_name = os.getenv("CLUSTER")
    client = connectDB()
    cluster = client[cluster_name]
    app.state.mediaCollection = cluster["medias"]
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
def index():
    content = """
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="file" type="file" multiple>
        <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)

@app.get("/media/{mediaId}")
def index(mediaId: str, req: Request):
    mediaCollection = req.app.state.mediaCollection

    try:
        mediaId = ObjectId(mediaId)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid media ID")

    media = mediaCollection.find_one({"_id": mediaId})

    if not media:
        raise HTTPException(status_code=404, detail="Media not found")

    media['_id'] = str(media['_id'])
    return Media(**media)


@app.post("/media")
def postMedia(media: MediaCreate, req: Request):
    collection = req.app.state.mediaCollection
    media = media.model_dump()

    try:
        res = collection.insert_one(media)
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Media with this key already exist")
    except PyMongoError as err:
        print("Error in postMedia controller: ", err)
        raise HTTPException(status_code=500, detail="Internal server error")
    
    return str(res.inserted_id)


@app.post("/uploadfiles")
async def upload(file: UploadFile):
    
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file found")
    print(file)
    print(file.file)

    
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tempFile:
            tempPath = tempFile.name
            await file.seek(0)
            shutil.copyfileobj(file.file, tempFile)
    except Exception as e:
        print("Error in upload tempFile: ", e)
        raise HTTPException(status_code=400, detail="Failed to upload file")
    

    #todo
    # pass the media to transfomer function to get the context

    #todo
    #embed the context
    
    res = uploadFileToS3(file.file, file.filename)

    if not res:
        raise HTTPException(status_code=400, detail="Failed to upload file")

    return {"filenames": res}

