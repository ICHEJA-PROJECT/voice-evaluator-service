from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import evaluate

app = FastAPI(
    title="Voice Evaluator API",
    version="1.0.0",
    description="Backend para la evaluación automática de voz usando FastAPI."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(evaluate.router)
