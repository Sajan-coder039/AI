import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from .vital import temperature, blood_pressure, respiration_rate, heartrate
from .config import Config
from .logger import logger

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
class VitalSigns(BaseModel):
    heart_rate: int
    temperature_rate: float
    systolic_bp: int
    diastolic_bp: int
    breathing_rate: int
    logger.info("Class is built for app_running")

@app.get("/")
async def health_check_up(request: Request):
    logger.info("Get requests going to run!!")
    return templates.TemplateResponse(request, "pro.html")

@app.post("/check", response_class=HTMLResponse)
async def checking(
    request: Request,
    heart_rate: int = Form(...),
    temperature_rate: float = Form(...),
    systolic_bp: int = Form(...),
    diastolic_bp: int = Form(...),
    breathing_rate: int = Form(...)
):
    
    vital = VitalSigns(
        heart_rate=heart_rate,
        temperature_rate=temperature_rate,
        systolic_bp=systolic_bp,
        diastolic_bp=diastolic_bp,
        breathing_rate=breathing_rate
    )
    result = {
        "Heart_Rate": heartrate(vital.heart_rate),
        "Temperature": temperature(vital.temperature_rate),
        "Blood_Pressure": blood_pressure(vital.systolic_bp, vital.diastolic_bp),
        "Respiration": respiration_rate(vital.breathing_rate)
    }
    logger.info("post requests response successfully")
    return templates.TemplateResponse(request, "result.html", {"result": result})

if __name__ == "__main__":
    logger.info("uvicorn run successfully")
    uvicorn.run("main:app", port=Config.PORT, log_level=Config.LOG_LEVEL)
