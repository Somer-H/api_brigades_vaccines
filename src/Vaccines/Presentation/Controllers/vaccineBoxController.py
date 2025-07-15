from ...Application.Services.vaccineBoxService import createVaccineBoxService, getVaccineBoxService, editVaccineBoxService, deleteVaccineBoxService, getVaccineBoxByIdService
from ...Domain.Scheme.vaccineScheme import VaccineBox, VaccineBoxBase, EditVaccineBox
from fastapi import HTTPException, Depends
from ....Shared.mysql import get_db
from sqlalchemy.orm import Session

def createVaccineBoxController(vaccine: VaccineBoxBase, db: Session = Depends(get_db)) -> VaccineBox:
    if not vaccine.amountVaccines:
        raise HTTPException(status_code=400, detail="Se requiere una cantidad de vacunas")
    if vaccine.amountVaccines < 0:
        raise HTTPException(status_code=400, detail="La cantidad de vacunas no puede ser negativa")
    return createVaccineBoxService(vaccine, db)

def getVaccineBoxController(db: Session = Depends(get_db)) -> list[VaccineBox]:
    return getVaccineBoxService(db)

def getVaccineBoxByIdController(id: int, db: Session = Depends(get_db)) -> VaccineBox:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    return getVaccineBoxByIdService(id, db)

def editVaccineBoxController(id: int, vaccineToEdit: EditVaccineBox, db: Session = Depends(get_db)) -> VaccineBox:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    return editVaccineBoxService(id, vaccineToEdit, db)
def deleteVaccineBoxController(id: int, db: Session = Depends(get_db)) -> str:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    return deleteVaccineBoxService(id, db)