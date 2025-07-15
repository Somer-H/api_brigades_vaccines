from sqlalchemy.orm import Session
from fastapi import HTTPException
from ...Domain.Scheme.vaccineScheme import VaccineBox, EditVaccineBox, VaccineBoxBase
from ...Infraestructure.Repositories.vaccineBoxRepository import createVaccineBoxRepository, getVaccineBoxRepository, editVaccineBoxRepository, deleteVaccineBoxRepository, getVaccineBoxByIdRepository

def createVaccineBoxService(vaccine: VaccineBoxBase, db: Session) -> VaccineBox:
    try:
        createVaccineBox = createVaccineBoxRepository(vaccine, db)
        return createVaccineBox
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getVaccineBoxService(db: Session) -> list[VaccineBox]:
    try:
        vaccineBoxToReturn = getVaccineBoxRepository(db)
        if not vaccineBoxToReturn:
            raise HTTPException(status_code=404, detail="No se encontraron Hieleras de vacunas")
        return vaccineBoxToReturn
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getVaccineBoxByIdService(id: int, db: Session) -> VaccineBox:
    try:
        vaccineBoxToReturn = getVaccineBoxByIdRepository(id, db)
        if not vaccineBoxToReturn:
            raise Exception("Hielera de vacunas no encontrada")
        if vaccineBoxToReturn:
            return vaccineBoxToReturn
        else:
            raise HTTPException(status_code=404, detail="Vaccine Box not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def editVaccineBoxService(id: int, vaccineToEdit: EditVaccineBox, db: Session) -> VaccineBox:
    try: 
        vaccineToEditNew= getVaccineBoxRepository(id, db)
        if not vaccineToEditNew:
            raise HTTPException(status_code=404, detail="No se encontró la Hielera de vacunas")
        if vaccineToEdit.amountVaccines is not None:
            vaccineToEditNew.amountVaccines = vaccineToEdit.amountVaccines
        updatedVaccineBox = editVaccineBoxRepository(vaccineToEditNew, db)
        if updatedVaccineBox:
            return updatedVaccineBox
        else:
            raise HTTPException(status_code=404, detail="Vaccine Box not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def deleteVaccineBoxService(id: int, db: Session) -> str:
    try:
        if deleteVaccineBoxRepository(id, db) == False:
            raise HTTPException(status_code=404, detail="No se encontró la Hielera de vacunas")
        return "Eliminado con éxtito"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))