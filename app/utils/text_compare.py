from Levenshtein import distance

def calculate_precision(objective_sentence: str, transcription: str):
    dist = distance(objective_sentence.lower(), transcription.lower())
    max_len = max(len(objective_sentence), len(transcription))
    precision = 1 - (dist / max_len) if max_len > 0 else 0.0
    return dist, precision
