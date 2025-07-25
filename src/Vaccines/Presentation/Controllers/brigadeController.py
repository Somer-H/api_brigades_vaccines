from ...Application.Services.brigadeService import createBrigadeService, getBrigadesService
from ...Domain.Scheme.brigadeScheme import BrigateRequestScheme, BrigateResponseWithLocationsScheme, BrigadeAndLocationsScheme
from fastapi import Depends, HTTPException
from ....Shared.mysql import get_db
from ....Shared.auth import jwtAuth
from sqlalchemy.orm import Session

def createBrigadeController(brigade: BrigateRequestScheme, db: Session = Depends(get_db), userData = jwtAuth("director")) -> BrigateResponseWithLocationsScheme:
    if not brigade.referenceBrigade: 
        raise HTTPException(status_code=400, detail="Debe ingresar una referencia de la brigada")
    if not brigade.startDate: 
        raise HTTPException(status_code=400, detail="Debe ingresar una fecha de inicio para la brigada")
    if not brigade.endDate: 
        raise HTTPException(status_code=400, detail="Debe ingresar una fecha de finalización para la brigada")
    if not brigade.locations: 
        raise HTTPException(status_code=400, detail="Debe ingresar al menos una localización")
    return createBrigadeService(brigade, db)

def getBrigadesController(db: Session = Depends(get_db), userData = jwtAuth("director")) -> list[BrigadeAndLocationsScheme]: 
    brigades = getBrigadesService(db)
    return brigades