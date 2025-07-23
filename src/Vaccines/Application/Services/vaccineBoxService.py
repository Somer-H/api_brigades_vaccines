from sqlalchemy.orm import Session
from fastapi import HTTPException
from ...Domain.Scheme.vaccineBoxScheme import VaccineBox, EditVaccineBox, VaccineBoxBase, VaccineBoxVaccinesScheme, VaccineBoxVaccineScheme
from ...Infraestructure.Repositories.vaccineBoxRepository import createVaccineBoxRepository, getVaccineBoxRepository, editVaccineBoxRepository, deleteVaccineBoxRepository, getVaccineBoxByIdRepository, createVaccineBoxVaccinesRepository

def createVaccineBoxService(vaccine: VaccineBoxBase, db: Session) -> VaccineBox:
    try:
        createVaccineBox = createVaccineBoxRepository(vaccine, db)
        return createVaccineBox
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def createVaccineBoxVaccineService(vaccineBoxVaccine: VaccineBoxVaccinesScheme, db: Session) -> VaccineBoxVaccinesScheme: 
    try:
        boxWithVaccines : list[int] = []
        for vaccine in vaccineBoxVaccine.idVaccines:
            vaccineBoxVaccineToPost = VaccineBoxVaccineScheme(
                idVaccineBox=vaccineBoxVaccine.idVaccineBox, 
                idVaccines = vaccine
            )
            createVaccineBoxVaccinesRepository(vaccineBoxVaccineToPost, db)
            boxWithVaccines.append(vaccine)
        vaccineBoxAndVaccineList = VaccineBoxVaccinesScheme (
            idVaccineBox=vaccineBoxVaccine.idVaccineBox,
            idVaccines=boxWithVaccines
        )
        return vaccineBoxAndVaccineList
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
        vaccineToEditNew= getVaccineBoxByIdRepository(id, db)
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
        return "Eliminado con éxito"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))