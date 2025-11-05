from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from ...Domain.Scheme.sensorsVaccine import SensorsVaccineBase, SensorsVaccine, GraficResponse, TemperatureInput
from ...Application.Services.sensorsVaccine import createSensorsVaccineService, getSensorsVaccineService, sendToGuassCurveService, pointInGaussCurveService
from ....Shared.mysql import get_db
from ....Shared.auth import jwtAuth
def createSensorsVaccineController(sensorsVaccine: SensorsVaccineBase, db: Session = Depends(get_db)) -> SensorsVaccine:
    if not sensorsVaccine.nameSensor:
        raise HTTPException(status_code=400, detail="Se requiere un nombre para el sensor")
    if not sensorsVaccine.measurementUnit: 
        raise HTTPException(status_code=400, detail="Se requiere una unidad de medida descriptiva del sensor")
    if not sensorsVaccine.information: 
        raise HTTPException(status_code=400, detail="Se requiere información de el sensor")
    if not sensorsVaccine.idVaccineBox:
        raise HTTPException(status_code=400, detail="Se requiere una Hielera de vacunas relacionada")
    return createSensorsVaccineService(sensorsVaccine, db)

def getSensorsVaccineController(db: Session = Depends(get_db)) -> list[SensorsVaccine]:
        return getSensorsVaccineService(db)

def sendToGaussController(db: Session = Depends(get_db)) -> GraficResponse: 
     return sendToGuassCurveService(db)

def inputGaussController(point: TemperatureInput, db: Session = Depends(get_db)) -> GraficResponse: 
     if not point.value: 
          raise HTTPException(status_code=400, detail="debe ingresar algún valor")
     return pointInGaussCurveService(point, db)