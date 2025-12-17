from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger
from modules.calcul import calcul

app = FastAPI()

class CalculRequest(BaseModel):
    value: int

@app.get("/")
def root():
    return {"message": "API FastIA"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/calcul")
def do_calcul(payload: CalculRequest):
    logger.info("Calcul demandé: {}", payload.value)
    return {"input": payload.value, "result": calcul(payload.value)}
