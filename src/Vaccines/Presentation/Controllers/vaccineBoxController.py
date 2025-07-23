from ...Application.Services.vaccineBoxService import createVaccineBoxService, getVaccineBoxService, editVaccineBoxService, deleteVaccineBoxService, getVaccineBoxByIdService, createVaccineBoxVaccineService
from ...Domain.Scheme.vaccineBoxScheme import VaccineBox, VaccineBoxBase, EditVaccineBox, VaccineBoxVaccinesScheme
from fastapi import HTTPException, Depends
from ....Shared.mysql import get_db
from ....Shared.auth import jwtAuth
from sqlalchemy.orm import Session

def createVaccineBoxController(vaccine: VaccineBoxBase, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director"))) -> VaccineBox:
    if not vaccine.amountVaccines:
        raise HTTPException(status_code=400, detail="Se requiere una cantidad de vacunas")
    if vaccine.amountVaccines < 0:
        raise HTTPException(status_code=400, detail="La cantidad de vacunas no puede ser negativa")
    return createVaccineBoxService(vaccine, db)

def createVaccineBoxVaccineController(vaccineBoxVaccine: VaccineBoxVaccinesScheme, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director"))) -> VaccineBoxVaccinesScheme: 
    if not vaccineBoxVaccine.idVaccineBox:
        raise HTTPException(status_code=400, detail="Debe ingresar un ID de caja de vacunas")
    if not vaccineBoxVaccine.idVaccines: 
        raise HTTPException(status_code=400, detail="Debe ingresar al menos un ID de vacunas")
    if vaccineBoxVaccine.idVaccineBox < 0: 
        raise HTTPException(status_code=400, detail="La ID no puede ser menor a 0")
    return createVaccineBoxVaccineService(vaccineBoxVaccine, db)
def getVaccineBoxController(db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director"))) -> list[VaccineBox]:
    return getVaccineBoxService(db)

def getVaccineBoxByIdController(id: int, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director"))) -> VaccineBox:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    return getVaccineBoxByIdService(id, db)

def editVaccineBoxController(id: int, vaccineToEdit: EditVaccineBox, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director"))) -> VaccineBox:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    return editVaccineBoxService(id, vaccineToEdit, db)
def deleteVaccineBoxController(id: int, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director"))) -> str:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    return deleteVaccineBoxService(id, db)