
def heartrate(hr: int)->str:
    if hr<60:
        return "LOW"
    elif hr>110:
        return "HIGH"
    else:
        return "NORMAL"
    
def temperature(temp:float)->str:
    if temp<35.0:
        return "LOW"
    elif temp >38.0:
        return "HIGH"
    else:
        return "NORMAL"
    

def blood_pressure(lower_bp:int,higher_bp:int)->str:
    if lower_bp<55 or higher_bp<100:
        return "LOW"

    elif lower_bp>90 or higher_bp>140:
        return "HIGH"
    
    else:
        return "NORMAL"
    
def respiration_rate(rate:int)->str:
    if  rate<12:
        return "LOW"
    elif rate>20:
        return "HIGH"
    else:
        return "NORMAL"

