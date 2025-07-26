from sqlalchemy.orm import Session
from ...Infraestructure.Models.sensorsVaccineModel import SensorsVaccineModel
from ...Domain.Scheme.sensorsVaccine import SensorsVaccine, SensorsVaccineBase
from fastapi import HTTPException

def createSensorsVaccineRepository(sensorsVaccine: SensorsVaccineBase, db: Session) -> SensorsVaccine:
    try:
        sensorsVaccineToPost = SensorsVaccineModel(**sensorsVaccine.dict())
        db.add(sensorsVaccineToPost)
        db.commit()
        db.refresh(sensorsVaccineToPost)
        return sensorsVaccineToPost
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def getSensorsVaccineRepository(db: Session) -> list[SensorsVaccine]:
    try:
        sensorsVaccineList = db.query(SensorsVaccineModel).all()
        return sensorsVaccineList
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getTemperatureSensorRepository(db: Session) -> list[SensorsVaccine]: 
    try: 
        sensorsVaccineList = db.query(SensorsVaccineModel).filter(SensorsVaccineModel.nameSensor == "temperature").all()
        return sensorsVaccineList
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))