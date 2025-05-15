from fastapi.testclient import TestClient
from app.main import app

from app.vital import (
    heartrate,
    temperature,
    blood_pressure,
    respiration_rate
)

def test_heartrate():
    assert heartrate(50) == "LOW"
    assert heartrate(75) == "NORMAL"
    assert heartrate(130) == "HIGH"

def test_temperature():
    assert temperature(33.0) == "LOW"
    assert temperature(36.8) == "NORMAL"
    assert temperature(39.0) == "HIGH"

def test_blood_pressure():
    assert blood_pressure(51, 80) == "LOW"
    assert blood_pressure(80, 120) == "NORMAL"
    assert blood_pressure(110,160) == "HIGH"

def test_respiration_rate():
    assert respiration_rate(11)=="LOW"
    assert respiration_rate(14)=="NORMAL"
    assert respiration_rate(21)=="HIGH"


client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "<html" in response.text.lower()

def test_vital_check():
    response = client.post(
        "/check",
        data={
            "heart_rate": 85,
            "temperature_rate": 36.6,
            "systolic_bp": 120,
            "diastolic_bp": 80,
            "breathing_rate": 16
        }
    )
    assert response.status_code == 200
    assert "Heart Rate:" in response.text
    assert "Temperature:" in response.text
    assert "Blood Pressure:" in response.text
    assert "Respiration:" in response.text
    assert any(label in response.text for label in ["NORMAL", "HIGH", "LOW"])  # optional
