from pydantic import BaseModel
from typing import Optional, List
class SensorsVaccineBase(BaseModel):
    measurementUnit : str
    nameSensor : str
    information : float
    idVaccineBox : int

    class Config:
        orm_mode = True  

class SensorsVaccine(SensorsVaccineBase):
    idSensorsVaccine: int

    class Config:
        orm_mode = True 

class SensorsVaccineEdit(BaseModel):
    measurementUnit: Optional[str] = None
    nameSensor: Optional[str] = None
    information: Optional[float] = None
    idVaccineBox: Optional[int] = None
    class Config:
        orm_mode = True

class GaussPoint(BaseModel):
    x: float  # Temperatura
    y: float  # Valor de la función de densidad (altura de la curva)

class GraficResponse(BaseModel):
    mean: float
    standarDeviation: float
    median: float
    mode: float
    range: float
    variance: float
    points: List[GaussPoint]