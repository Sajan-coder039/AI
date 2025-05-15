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
