import os
from fastapi import UploadFile
from app.services.whisper_service import transcribe_audio
from app.utils.text_compare import calculate_precision

async def evaluate_audio(audio: UploadFile, objective_sentence: str):
    temp_path = "temp_audio.wav"

    with open(temp_path, "wb") as f:
        f.write(await audio.read())

    transcription = transcribe_audio(temp_path)
    os.remove(temp_path)

    dist, precision = calculate_precision(objective_sentence, transcription)

    return {
        "objective_sentence": objective_sentence,
        "transcription": transcription,
        "distance": dist,
        "precision": round(precision * 100, 2)
    }
