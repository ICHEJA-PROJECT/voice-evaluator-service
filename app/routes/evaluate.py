from fastapi import APIRouter, UploadFile, Form, File, HTTPException, status
from app.services.evaluate_service import evaluate_audio
from app.schemas.evaluate_response import EvaluateResponse

router = APIRouter()

@router.post(
    "/evaluate",
    tags=["Evaluación de audio"],
    summary="Evalúa un audio contra una frase objetivo",
    response_description="Resultado de la evaluación",
    response_model=EvaluateResponse,
    responses={
        200: {
            "description": "Resultado de la evaluación",
            "content": {
                "application/json": {
                    "example": {
                        "objective_sentence": "Hola mundo",
                        "transcription": "Hola mundo",
                        "distance": 0,
                        "precision": 100.0
                    }
                }
            }
        },
        400: {"description": "Solicitud inválida"},
        500: {"description": "Error interno del servidor"}
    }
)
async def evaluate(
    audio: UploadFile = File(..., description="Archivo de audio a evaluar (WAV, MP3, etc.)"),
    objective_sentence: str = Form(..., description="Frase objetivo para comparar con la transcripción")
):
    try:
        if not audio or not objective_sentence:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Faltan datos requeridos.")
        return await evaluate_audio(audio, objective_sentence)
    except HTTPException:
        raise  
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
