from pydantic import BaseModel
from typing import List

class EvaluateResponse(BaseModel):
    objective_sentence: str
    transcription: str
    distance: float
    precision: float
    wrong_words: List[str] 