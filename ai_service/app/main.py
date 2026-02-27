from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import torch

app = FastAPI(title="Justina AI Service")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TelemetryData(BaseModel):
    x: float
    y: float
    z: float
    timestamp: str
    sessionId: str

class AnalysisResponse(BaseModel):
    status: str
    feedback: str
    precision_score: float

@app.get("/")
def read_root():
    return {"status": "online", "pytorch": torch.__version__}

@app.post("/analisar", response_model=AnalysisResponse)
async def analyze_movement(data: List[TelemetryData]):
    if not data:
        raise HTTPException(status_code=400, detail="Sem dados")
    
    return AnalysisResponse(
        status="SUCCESS",
        feedback="Simulação capturada. IA processando trajetória...",
        precision_score=0.95
    )
