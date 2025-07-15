from sqlalchemy.orm import Session
from fastapi import HTTPException
from ...Infraestructure.Repositories.sensorsVaccine import createSensorsVaccineRepository, getSensorsVaccineRepository
from ...Domain.Scheme.sensorsVaccine import SensorsVaccine, SensorsVaccineBase
def createSensorsVaccineService(sensorsVaccine: SensorsVaccineBase, db: Session) -> SensorsVaccine:
    try: 
        return createSensorsVaccineRepository(sensorsVaccine, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getSensorsVaccineService(db: Session) -> list[SensorsVaccine]:
    try: 
        sensorsGet = getSensorsVaccineRepository(db)
        if not sensorsGet:
            raise HTTPException(status_code=404, detail="No se encontraron Sensores de vacunas")
        return sensorsGet
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))