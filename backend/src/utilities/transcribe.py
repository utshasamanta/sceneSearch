import whisper
import tempfile
from moviepy import VideoFileClip
import os

model = whisper.load_model("tiny.en")


def getTranscription(videoPath):
    try:
        audioPath = None
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as audio:
            audioPath = audio.name

        videClip = VideoFileClip(videoPath)
        audioClip = videClip.audio
        audioClip.write_audiofile(audioPath)
        
        audioClip.close()
        videClip.close()

        result = model.transcribe(audioPath)
        print(result["text"])
        return result["text"]
    except Exception as err:
        print("Error in transcribe audio: ", err)
    finally:
        if audioPath and os.path.exists(audioPath):
            os.remove(audioPath)
