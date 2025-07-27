from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from ...Domain.Scheme.vaccineScheme import VaccineBaseScheme, VaccineEditScheme, VaccineScheme, VaccineVaccineBoxScheme
from ...Application.Services.vaccineService import createVaccineService, editVaccineService, deleteVaccineService, getVaccinesService, getVaccineByIdService, getVaccineVaccineBoxService
from ....Shared.mysql import get_db
from ....Shared.auth import jwtAuth

def createVaccineController (vaccine: VaccineBaseScheme, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles="director")) -> VaccineScheme: 
    if not vaccine.nameVaccine: 
        raise HTTPException("El campo del nombre de la vacuna es obligatorio")
    return createVaccineService(vaccine, db)

def getVaccinesController (db: Session = Depends(get_db), userData = jwtAuth(expectedRoles="director")) -> list[VaccineScheme]: 
    return getVaccinesService(db)
def getVaccineByIdController (id: int, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles="director")) -> VaccineScheme: 
    if not id: 
        raise HTTPException(status_code=400,detail="Debe ingresar una ID")
    if id < 0: 
        raise HTTPException(status_code=400, detail="La ID no debe ser menor a 0")
    return getVaccineByIdService(id, db)

def getVaccineVaccineBoxController (db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director","enfermero", "lider"))) -> list[VaccineVaccineBoxScheme]: 
    return getVaccineVaccineBoxService(db)
def editVaccineController (id: int, vaccine: VaccineEditScheme, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles="director")) -> VaccineScheme: 
    if not id: 
        raise HTTPException(status_code=400, detail="Debe ingresar una ID")
    if id <= 0: 
        raise HTTPException(status_code=400, detail="La ID no debe ser menor o igual a 0")
    return editVaccineService(id, vaccine, db)

def deleteVaccineController (id: int, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles="director")) -> str: 
    if not id: 
        raise HTTPException(status_code=400, detail="Debe ingresar una ID")
    if id <= 0: 
        raise HTTPException(status_code=400, detail="La ID no debe ser menor o igual a 0")
    return deleteVaccineService(id, db)