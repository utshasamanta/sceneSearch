from fastapi import APIRouter, UploadFile, HTTPException
from utilities.imageCaption import getVideoContext, getPhotoContext
from utilities.s3 import uploadFileToS3
from utilities.transcribe import getTranscription
import tempfile
import shutil
import os

router = APIRouter()



@router.get("/getMedia")
def getMedia(query: str):
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    #todo
    #embed the query

    #todo
    #search in db

    #todo
    #get the best media based on score
    #presign the aws url
    #return media object


@router.post("/upload")
async def uploadMedia(file: UploadFile):
    tempPath = None
    try:
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file to upload")
        

        suffix = ".png" if file.content_type.startswith("image/") else ".mp4"

        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as t:
                tempPath = t.name
                await file.seek(0)
                shutil.copyfileobj(file.file, t)
        except Exception as err:
            print("Error while making temp file in upload route: ", err)
            raise HTTPException(status_code=400, detail="Failed to upload file")



        if file.content_type.startswith("image/"):            
            mediaContext = getPhotoContext(tempPath)
        elif file.content_type.startswith("video/"):
            mediaContext = getVideoContext(tempPath)
            transcript = getTranscription(tempPath)
        else:
            raise HTTPException(status_code=400, detail="Upload only video or images")


        if not mediaContext:
            raise HTTPException(status_code=400, detail="Failed to get context")
        
        #todo
        #vector embbed transcript and context

        res = uploadFileToS3(file.file, file.filename)

        if not res:
            raise HTTPException(status_code=400, detail="Failed to upload file")
        
        #todo
        #insert to database
        
        return {"Message": "Sucessfully uploaded media"}
    except Exception as err:
        print("Error in upload route: ", err)
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        if tempPath and os.path.exists(tempPath):
            os.remove(tempPath)
