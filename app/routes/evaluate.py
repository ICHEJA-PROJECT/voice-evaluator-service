from fastapi import APIRouter, UploadFile, Form, File
from app.services.evaluate_service import evaluate_audio

router = APIRouter()

@router.post("/evaluate")
async def evaluate(audio: UploadFile = File(...), objective_sentence: str = Form(...)):
    return await evaluate_audio(audio, objective_sentence)
