from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from ...Domain.Scheme.sensorsVaccine import SensorsVaccineBase, SensorsVaccine
from ...Application.Services.sensorsVaccine import createSensorsVaccineService, getSensorsVaccineService
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