from ...Infraestructure.Repositories.vaccineRepository import createVaccineRepository, getVaccineByIdRepository, getVaccinesRepository, deleteVaccineRepository, editVaccineRepository, getVaccinesWithVaccinesBoxRepository
from fastapi import HTTPException
from ...Domain.Scheme.vaccineScheme import VaccineBaseScheme, VaccineEditScheme, VaccineScheme, VaccineVaccineBoxScheme
from sqlalchemy.orm import Session

def createVaccineService (vaccine: VaccineBaseScheme, db: Session) -> VaccineScheme: 
    try:
        cretedVaccine = createVaccineRepository(vaccine, db)
        return cretedVaccine
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getVaccinesService (db: Session) -> list[VaccineScheme]: 
    try: 
        vaccines = getVaccinesRepository(db)
        if not vaccines: 
            raise HTTPException(status_code=400, detail=("No se han encontrado vacunas"))
        return vaccines
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
def getVaccineByIdService (id: int, db: Session) -> VaccineScheme: 
    try: 
        vaccine = getVaccineByIdRepository(id, db)
        if not vaccine: 
            raise HTTPException(status_code=400, detail="No se ha encontrado la vacuna")
        return vaccine
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))

def getVaccineVaccineBoxService(db: Session) -> list[VaccineVaccineBoxScheme]:
    try: 
        vaccines = getVaccinesWithVaccinesBoxRepository(db)
        if not vaccines: 
            raise HTTPException(status_code=400, detail="No se ha encontrado nada")
        return vaccines
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
def editVaccineService(id: int, vaccineToEdit: VaccineEditScheme, db: Session) -> VaccineScheme: 
    try:
        vaccineToEditNew = getVaccineByIdService(id, db)
        if not vaccineToEditNew: 
            raise HTTPException(status_code=500, detail="No se ha encontrado la vacuna")
        if vaccineToEdit.nameVaccine: 
            vaccineToEditNew.nameVaccine =vaccineToEdit.nameVaccine
        updatedVaccine = editVaccineRepository(vaccineToEditNew, db)
        if updatedVaccine:
            return updatedVaccine
        else: 
            HTTPException(status_code=400, detail="No se ha encontrado la vacuna")
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
def deleteVaccineService(id: int, db: Session) -> str: 
    try: 
        if deleteVaccineRepository(id, db) == False:
            raise HTTPException(status_code=400, detail="No se ha encontrado la vacuna")
        return "Eliminado con éxito"
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))