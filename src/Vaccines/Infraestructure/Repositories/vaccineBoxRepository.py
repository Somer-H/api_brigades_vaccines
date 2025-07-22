from ...Infraestructure.Models.vaccineBoxModel import VaccineBoxModel
from ...Domain.Scheme.vaccineBoxScheme import VaccineBox, EditVaccineBox, VaccineBoxBase
from sqlalchemy.orm import Session
from fastapi import HTTPException
def createVaccineBoxRepository(vaccineBox: VaccineBoxBase, db: Session) -> VaccineBox:
    try:
        vaccineToPost = VaccineBoxModel(**vaccineBox.dict())
        db.add(vaccineToPost)
        db.commit()
        db.refresh(vaccineToPost)
        return vaccineToPost
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
def getVaccineBoxRepository(db: Session) -> VaccineBox:
    try:
        vaccineBoxToReturn = db.query(VaccineBoxModel).all()
        return vaccineBoxToReturn
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getVaccineBoxByIdRepository(id: int, db: Session) -> VaccineBox:
    try:
        vaccineBoxToReturn = db.query(VaccineBoxModel).filter(VaccineBoxModel.idVaccineBox == id).first()
        return vaccineBoxToReturn
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def editVaccineBoxRepository(vaccineToEdit: EditVaccineBox, db: Session) -> VaccineBox:
     try: 
         db.commit()
         db.refresh(vaccineToEdit)
         return vaccineToEdit
     except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail = str(e))
     
def deleteVaccineBoxRepository(id: int, db: Session) -> bool:
    try:
        vaccineBoxToDelete = db.query(VaccineBoxModel).filter(VaccineBoxModel.idVaccineBox == id).first()
        if not vaccineBoxToDelete:
            #No la encontró
            return False
        db.delete(vaccineBoxToDelete)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))