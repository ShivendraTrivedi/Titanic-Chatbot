from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .chatbot import analyze_data

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/analyze")
async def analyze(query: Query):
    try:
        response = analyze_data(query.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))