from ...Domain.Scheme.userMedicPersonalScheme import UserMedicPersonalScheme, UserMedicPersonalSchemeBase, UserMedicPersonalEditScheme
from ...Domain.Models.userMedicPersonalModel import UserMedicPersonalModel
from sqlalchemy.orm import Session
from fastapi import HTTPException

def createUserMedicPersonalRepository(userMedicPersonal: UserMedicPersonalSchemeBase, db: Session) -> UserMedicPersonalScheme:
    try:
        userMedicPersonalToPost = UserMedicPersonalModel(**userMedicPersonal.dict())
        db.add(userMedicPersonalToPost)
        db.commit()
        db.refresh(userMedicPersonalToPost)
        return userMedicPersonalToPost
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
def getUserMedicPersonalRepository(db: Session) -> list[UserMedicPersonalScheme]:
    try:
        userMedicPersonalList = db.query(UserMedicPersonalModel).all()
        return userMedicPersonalList
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getUserMedicPersonalByIdRepository(id: int, db: Session) -> UserMedicPersonalScheme:
    try:
        userMedicPersonalToReturn = db.query(UserMedicPersonalModel).filter(UserMedicPersonalModel.idUserMedicPersonal == id).first()
        if not userMedicPersonalToReturn:
            raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
        return userMedicPersonalToReturn
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def editUserMedicPersonalRepository(userMedicPersonalToEdit: UserMedicPersonalScheme, db: Session) -> UserMedicPersonalScheme:
    try:
        db.commit()
        db.refresh(userMedicPersonalToEdit)
        return userMedicPersonalToEdit
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
def deleteUserMedicPersonalRepository(id: int, db: Session) -> bool:
    try:
        userMedicPersonalToDelete = db.query(UserMedicPersonalModel).filter(UserMedicPersonalModel.idUserMedicPersonal == id).first()
        if not userMedicPersonalToDelete:
            return False  # No se encontró el usuario médico personal
        db.delete(userMedicPersonalToDelete)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))