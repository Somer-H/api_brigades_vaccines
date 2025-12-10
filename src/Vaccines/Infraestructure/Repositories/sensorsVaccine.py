from sqlalchemy.orm import Session
from ...Infraestructure.Models.sensorsVaccineModel import SensorsVaccineModel
from ...Domain.Scheme.sensorsVaccine import SensorsVaccine, SensorsVaccineBase
from ...Infraestructure.Models.userCivilModel import UserCivilModel
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


def getTemperatureSensorRepository(db: Session) -> list[float]:
    """
    Obtiene todas las temperaturas corporales de los usuarios civiles.
    Retorna una lista de valores float.
    """
    try: 
        # ✅ Query directo a la columna corporalTemperature
        temperatures = db.query(UserCivilModel.corporalTemperature).all()
        
        # ✅ Convertir tuplas a lista de floats y filtrar valores None
        temperature_list = [temp[0] for temp in temperatures if temp[0] is not None]
        
        return temperature_list
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))