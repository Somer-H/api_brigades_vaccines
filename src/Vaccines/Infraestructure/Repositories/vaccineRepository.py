from ...Infraestructure.Models.vaccineModel import VaccineModel
from ...Domain.Scheme.vaccineScheme import VaccineScheme, VaccineBaseScheme, VaccineEditScheme
from sqlalchemy.orm import Session
from fastapi import HTTPException
def createVaccineRepository (vaccine: VaccineBaseScheme, db: Session) -> VaccineScheme: 
    try: 
        vaccinePost = VaccineModel(**vaccine.dict())
        db.add(vaccinePost)
        db.commit()
        db.refresh()
        return vaccinePost
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def getVaccinesRepository(db: Session) -> list[VaccineScheme]: 
    try: 
       vaccines = db.query(VaccineModel).all()
       return vaccines
    except Exception as e: 
        HTTPException(status_code=500, detail=str(e))

def getVaccineByIdRepository(id: int, db: Session) -> VaccineScheme:
    try:
        vaccine = db.query(VaccineModel).filter(VaccineModel.idVaccines == id).first()
        return vaccine
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))

def editVaccineRepository(vaccineToEdit: VaccineEditScheme, db: Session) -> VaccineScheme: 
    try: 
         db.commit()
         db.refresh(vaccineToEdit)
         return vaccineToEdit
    except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail = str(e))

def deleteVaccineRepository(id: int, db: Session) -> bool: 
    try:
        vaccineToDelete = db.query(VaccineModel).filter(VaccineModel.idVaccines == id).first()
        if not vaccineToDelete:
            #No la ha encontrado
            return False
        db.delete(vaccineToDelete)
        db.commit()
        return True
    except Exception as e: 
        return HTTPException(status_code=500, detail=str(e))