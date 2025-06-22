from Levenshtein import distance
import logging
import re
import difflib

logger = logging.getLogger(__name__)

def calculate_precision(objective_sentence: str, transcription: str):
    try:
        dist = distance(objective_sentence.lower(), transcription.lower())
        max_len = max(len(objective_sentence), len(transcription))
        precision = 1 - (dist / max_len) if max_len > 0 else 0.0

        objective_words = re.findall(r'\b[\w\']+\b', objective_sentence)
        transcription_words = re.findall(r'\b[\w\']+\b', transcription)
        
        objective_words_lower = [word.lower() for word in objective_words]
        transcription_words_lower = [word.lower() for word in transcription_words]

        wrong_words = []
        matcher = difflib.SequenceMatcher(None, objective_words_lower, transcription_words_lower)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == 'replace' or tag == 'insert':
                wrong_words.extend(transcription_words[j1:j2])

        return dist, precision, wrong_words
    except Exception as e:
        logger.error(f"Error en calculate_precision: {e}")
        raise ValueError("Error al calcular precisión entre frases.")
