from ...Domain.Scheme.userScheme import UserScheme, UserSchemeBase, UserEditScheme, UserResponse
from ..Models.userModel import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
def createUserRepository(user: UserSchemeBase, db: Session) -> UserResponse:
    try:
        userMedicPersonalToPost = User(**user.dict())
        db.add(userMedicPersonalToPost)
        db.commit()
        db.refresh(userMedicPersonalToPost)
        return userMedicPersonalToPost
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
def getUserRepository(db: Session) -> list[UserResponse]:
    try:
        userMedicPersonalList = db.query(User).all()
        return userMedicPersonalList
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getUserByIdRepository(id: int, db: Session) -> UserResponse:
    try:
        userMedicPersonalToReturn = db.query(User).filter(User.idUser == id).first()
        if not userMedicPersonalToReturn:
            raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
        return userMedicPersonalToReturn
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def editUserRepository(userMedicPersonalToEdit: UserEditScheme, db: Session) -> UserResponse:
    try:
        db.commit()
        db.refresh(userMedicPersonalToEdit)
        return userMedicPersonalToEdit
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
def deleteUserRepository(id: int, db: Session) -> bool:
    try:
        userMedicPersonalToDelete = db.query(User).filter(User.idUser == id).first()
        if not userMedicPersonalToDelete:
            return False  # No se encontró el usuario
        db.delete(userMedicPersonalToDelete)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
def getUserByUsernameRepository(username: str, db: Session) -> UserResponse: 
    try:
        userMedicPersonal = db.query(User).filter(User.username == username).first()
        return userMedicPersonal
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))