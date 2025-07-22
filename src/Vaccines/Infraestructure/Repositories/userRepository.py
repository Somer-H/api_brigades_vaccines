from ...Domain.Scheme.userScheme import UserMedicPersonalScheme, UserSchemeBase, UserMedicPersonalEditScheme, UserMedicPersonalResponse
from ..Models.userModel import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
def createUserMedicPersonalRepository(userMedicPersonal: UserSchemeBase, db: Session) -> UserMedicPersonalResponse:
    try:
        userMedicPersonalToPost = User(**userMedicPersonal.dict())
        db.add(userMedicPersonalToPost)
        db.commit()
        db.refresh(userMedicPersonalToPost)
        return userMedicPersonalToPost
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
def getUserMedicPersonalRepository(db: Session) -> list[UserMedicPersonalResponse]:
    try:
        userMedicPersonalList = db.query(User).all()
        return userMedicPersonalList
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getUserMedicPersonalByIdRepository(id: int, db: Session) -> UserMedicPersonalResponse:
    try:
        userMedicPersonalToReturn = db.query(User).filter(User.idUserMedicPersonal == id).first()
        if not userMedicPersonalToReturn:
            raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
        return userMedicPersonalToReturn
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def editUserMedicPersonalRepository(userMedicPersonalToEdit: UserMedicPersonalEditScheme, db: Session) -> UserMedicPersonalResponse:
    try:
        db.commit()
        db.refresh(userMedicPersonalToEdit)
        return userMedicPersonalToEdit
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
def deleteUserMedicPersonalRepository(id: int, db: Session) -> bool:
    try:
        userMedicPersonalToDelete = db.query(User).filter(User.idUserMedicPersonal == id).first()
        if not userMedicPersonalToDelete:
            return False  # No se encontró el usuario
        db.delete(userMedicPersonalToDelete)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
def getUserMedicPersonalByUsernameRepository(username: str, db: Session) -> UserMedicPersonalScheme: 
    try:
        userMedicPersonal = db.query(User).filter(User.username == username).first()
        return userMedicPersonal
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))