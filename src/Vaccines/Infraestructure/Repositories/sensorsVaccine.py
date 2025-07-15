from sqlalchemy.orm import Session
from ...Application.Models.sensorsVaccineModel import SensorsVaccineModel
from ...Domain.Scheme.sensorsVaccine import SensorsVaccine, SensorsVaccineBase

def createSensorsVaccineRepository(sensorsVaccine: SensorsVaccineBase, db: Session) -> SensorsVaccine:
    try:
        sensorsVaccineToPost = SensorsVaccineModel(**sensorsVaccine.dict())
        db.add(sensorsVaccineToPost)
        db.commit()
        db.refresh(sensorsVaccineToPost)
        return sensorsVaccineToPost
    except Exception as e:
        db.rollback()
        raise e

def getSensorsVaccineRepository(db: Session) -> list[SensorsVaccine]:
    try:
        sensorsVaccineList = db.query(SensorsVaccineModel).all()
        return sensorsVaccineList
    except Exception as e:
        raise e