import whisper
import logging

logger = logging.getLogger(__name__)

model = whisper.load_model("base")

def transcribe_audio(path: str) -> str:
    try:
        result = model.transcribe(path, language="es")
        return result["text"].strip()
    except Exception as e:
        logger.error(f"Error en transcribe_audio: {e}")
        raise RuntimeError("Error al transcribir el audio.")
