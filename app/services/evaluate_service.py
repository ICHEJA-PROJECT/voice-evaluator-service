import os
import logging
from fastapi import UploadFile, HTTPException, status
from app.services.whisper_service import transcribe_audio
from app.utils.text_compare import calculate_precision

logger = logging.getLogger(__name__)

async def evaluate_audio(audio: UploadFile, objective_sentence: str):
    temp_path = "temp_audio.wav"
    try:
        with open(temp_path, "wb") as f:
            f.write(await audio.read())
        try:
            transcription = transcribe_audio(temp_path)
        except Exception as e:
            logger.error(f"Error transcribiendo audio: {e}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al transcribir el audio.")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
        try:
            dist, precision, wrong_words = calculate_precision(objective_sentence, transcription)
        except Exception as e:
            logger.error(f"Error calculando precisión: {e}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al calcular precisión.")
        return {
            "objective_sentence": objective_sentence,
            "transcription": transcription,
            "distance": dist,
            "precision": round(precision * 100, 2),
            "wrong_words": wrong_words
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error general en evaluate_audio: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno en la evaluación de audio.")
