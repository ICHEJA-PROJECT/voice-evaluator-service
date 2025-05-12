from Levenshtein import distance
import logging

logger = logging.getLogger(__name__)

def calculate_precision(objective_sentence: str, transcription: str):
    try:
        dist = distance(objective_sentence.lower(), transcription.lower())
        max_len = max(len(objective_sentence), len(transcription))
        precision = 1 - (dist / max_len) if max_len > 0 else 0.0
        return dist, precision
    except Exception as e:
        logger.error(f"Error en calculate_precision: {e}")
        raise ValueError("Error al calcular precisión entre frases.")
