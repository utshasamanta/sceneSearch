from pydantic import BaseModel, Field
from typing import List, Optional
from bson.objectid import ObjectId

class MediaBase(BaseModel):
    name: str = Field(..., description="Name of the media")
    url: str = Field(default="", description="url of the media")
    mediaContext: str = Field(default="", description="Context of the media")
    contextVector: List[float] = Field(default=[], description="Vector embedding of the context")
    mediaTranscript: str = Field(default="", description="Transcript of the media")
    transcriptVector: List[float] = Field(default=[], description="Vector embedding of the transcript")

class Media(MediaBase):
    id: str = Field(alias="_id", description="MongoDB Object ID")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }

class MediaCreate(MediaBase):
    pass