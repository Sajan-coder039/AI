import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from app.vital import temperature,blood_pressure,respiration_rate,heartrate

app=FastAPI()

class VitalSigns(BaseModel):
    heart_rate: int
    temperature_rate: float
    systolic_bp: int
    diastolic_bp: int
    breathing_rate: int

# vital=VitalSigns()

@app.get("/")
async def health_check_up():
    return {"status": "ok"}

@app.post("/check")
async def checking(vital:VitalSigns):
    return {
        "Heart_Rate":heartrate(vital.heart_rate),
        "Temperature":temperature(vital.temperature_rate),
        "Blood_pressure":blood_pressure(vital.systolic_bp,vital.diastolic_bp),
        "Respiration":respiration_rate(vital.breathing_rate)
    }

if __name__=="__main__":
    uvicorn.run("app:app",port=9999,log_level="info")