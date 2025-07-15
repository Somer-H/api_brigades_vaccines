from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from ...Domain.Scheme.sensorsVaccine import SensorsVaccineBase, SensorsVaccine
from ...Application.Services.sensorsVaccine import createSensorsVaccineService
from ....Shared.mysql import get_db
def createSensorsVaccineController(sensorsVaccine: SensorsVaccineBase, db: Session = Depends(get_db)) -> SensorsVaccine:
    try:
        return createSensorsVaccineService(sensorsVaccine, db)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))