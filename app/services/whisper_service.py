import whisper
import logging
import os

logger = logging.getLogger(__name__)

model = whisper.load_model("base")

def transcribe_audio(path: str) -> str:
    try:
        abs_path = os.path.abspath(path)
        print(f"Transcribiendo archivo en: {abs_path}")
        result = model.transcribe(abs_path, language="es")
        return result["text"].strip()
    except Exception as e:
        logger.error(f"Error en transcribe_audio: {e}")
        raise RuntimeError("Error al transcribir el audio.")
