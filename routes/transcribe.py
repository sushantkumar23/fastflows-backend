import os

import openai
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from auth import get_current_user

router = APIRouter(prefix="/transcribe", tags=["Transcribe"])


@router.post("/", description="Get transcription for an audio file")
async def transcribe_audio(
    file: UploadFile = File(...), user_id=Depends(get_current_user)
):
    # Save the file to disk
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    openai.api_key = os.getenv("OPENAI_API_KEY")
    audio_file = open(file_location, "rb")
    try:
        transcript = openai.Audio.translate("whisper-1", audio_file)
        # remove the file from disk
        os.remove(file_location)
        return {"transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error transcribing audio: {e}")
