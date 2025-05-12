from pydantic import BaseModel

class EvaluateResponse(BaseModel):
    objective_sentence: str
    transcription: str
    distance: float
    precision: float 