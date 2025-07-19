from ...Infraestructure.Repositories.userMedicPersonal import createUserMedicPersonalRepository, getUserMedicPersonalRepository, getUserMedicPersonalByIdRepository, editUserMedicPersonalRepository, deleteUserMedicPersonalRepository
from ...Domain.Scheme.userMedicPersonalScheme import UserMedicPersonalScheme, UserMedicPersonalSchemeBase, UserMedicPersonalEditScheme
from fastapi import HTTPException
import bcrypt
from sqlalchemy.orm import Session
def createUserMedicPersonalService(userMedicPersonal: UserMedicPersonalSchemeBase, db: Session) -> UserMedicPersonalScheme:
    try:
        userMedicPersonal.password = bcrypt.hashpw(userMedicPersonal.password.encode('utf-8'), bcrypt.gensalt())
        return createUserMedicPersonalRepository(userMedicPersonal, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getUserMedicPersonalService(db: Session) -> list[UserMedicPersonalScheme]:
    try:
        userMedicPersonalList = getUserMedicPersonalRepository(db)
        if not userMedicPersonalList:
            raise HTTPException(status_code=404, detail="No se encontraron Usuarios médicos personales")
        return userMedicPersonalList
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getUserMedicPersonalByIdService(id: int, db: Session) -> UserMedicPersonalScheme:
    try:
        userMedicPersonalToReturn = getUserMedicPersonalByIdRepository(id, db)
        if not userMedicPersonalToReturn:
            raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
        return userMedicPersonalToReturn
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def editUserMedicPersonalService(id: int, userMedicPersonalToEdit: UserMedicPersonalEditScheme, db: Session) -> UserMedicPersonalScheme:
    try:
        userMedicPersonalToEditNew = getUserMedicPersonalByIdRepository(id, db)
        if not userMedicPersonalToEditNew:
            raise HTTPException(status_code=404, detail="No se encontró el Usuario médico personal")
        if userMedicPersonalToEdit.name is not None:
            userMedicPersonalToEditNew.name = userMedicPersonalToEdit.name
        if userMedicPersonalToEdit.email is not None:
            userMedicPersonalToEditNew.email = userMedicPersonalToEdit.email
        updatedUserMedicPersonal = editUserMedicPersonalRepository(userMedicPersonalToEditNew, db)
        if updatedUserMedicPersonal:
            return updatedUserMedicPersonal
        else:
            raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def deleteUserMedicPersonalService(id: int, db: Session) -> str:
    try:
        if deleteUserMedicPersonalRepository(id, db) == False:
            raise HTTPException(status_code=404, detail="No se encontró el Usuario médico personal")
        return "Eliminado con éxito"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))