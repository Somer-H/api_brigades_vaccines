from ...Application.Services.brigadeService import createBrigadeService, getBrigadesService, getBrigadeWithLocationsByIdService, editBrigadeService
from ...Domain.Scheme.brigadeScheme import BrigateRequestScheme, BrigateResponseWithLocationsScheme, BrigadeAndLocationsScheme, BrigadeUpdateScheme, BrigadeFullScheme
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

def getBrigadeWithLocationsByIdController(id: int, db: Session = Depends(get_db)) -> list[BrigadeAndLocationsScheme]: 
    brigade = getBrigadeWithLocationsByIdService(id, db)
    return brigade

def editBrigadeController(id: int, brigade: BrigadeUpdateScheme, db: Session = Depends(get_db)) -> BrigadeFullScheme: 
    if not id: 
        raise HTTPException(status_code=400, detail="Debe ingresar un ID")
    if id <= 0: 
        raise HTTPException(status_code=400, detail="La ID no debe ser igual o menor que 0")
    return editBrigadeService(id, brigade, db)