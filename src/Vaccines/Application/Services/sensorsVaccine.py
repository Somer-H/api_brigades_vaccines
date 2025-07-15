from sqlalchemy.orm import Session
from fastapi import HTTPException
from ...Infraestructure.Repositories.sensorsVaccine import createSensorsVaccineRepository
from ...Domain.Scheme.sensorsVaccine import SensorsVaccine, SensorsVaccineBase
def createSensorsVaccineService(sensorsVaccine: SensorsVaccineBase, db: Session) -> SensorsVaccine:
    try: 
        return createSensorsVaccineRepository(sensorsVaccine, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))