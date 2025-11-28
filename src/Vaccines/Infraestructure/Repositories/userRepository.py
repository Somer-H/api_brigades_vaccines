from ...Domain.Scheme.userScheme import UserScheme, UserSchemeBase, UserEditScheme, UserResponse
from ..Models.userModel import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import or_
def createUserRepository(user: UserSchemeBase, db: Session) -> UserResponse:
    try:
        # Verificar si ya existe una cuenta para este usuario civil
        if user.idUserCivil:
            existing_user = db.query(User).filter(
                User.idUserCivil == str(user.idUserCivil)
            ).first()
            if existing_user:
                raise HTTPException(
                    status_code=400, 
                    detail="Este usuario civil ya tiene una cuenta asociada"
                )
        
        # Verificar si el username ya existe
        existing_username = db.query(User).filter(
            User.username == user.username
        ).first()
        if existing_username:
            raise HTTPException(
                status_code=400,
                detail="El nombre de usuario ya está en uso"
            )
        
        userMedicPersonalToPost = User(**user.dict())
        db.add(userMedicPersonalToPost)
        db.commit()
        db.refresh(userMedicPersonalToPost)
        return userMedicPersonalToPost
    except HTTPException:
        db.rollback()
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
def getUserRepository(db: Session) -> list[UserResponse]:
    try:
        userMedicPersonalList = db.query(User).all()
        return userMedicPersonalList
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getLeaderAndNurseRepository(db: Session) -> list[UserResponse]:
    try: 
        usersMedic = db.query(User).filter(or_(User.role == "lider", User.role == "enfermero")).all()
        return usersMedic
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