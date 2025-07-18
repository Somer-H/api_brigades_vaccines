from ...Application.Services.userMedicPersonalService import createUserMedicPersonalService, getUserMedicPersonalService, getUserMedicPersonalByIdService, editUserMedicPersonalService, deleteUserMedicPersonalService
from ...Domain.Scheme.userMedicPersonalScheme import UserMedicPersonalSchemeBase, UserMedicPersonalScheme, UserMedicPersonalEditScheme
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from ....Shared.mysql import get_db
def createUserMedicPersonalController(userMedicPersonal: UserMedicPersonalSchemeBase, db: Session = Depends(get_db)) -> UserMedicPersonalScheme:
    if not userMedicPersonal.name:
        raise HTTPException(status_code=400, detail="El nombre es obligatorio")
    if not userMedicPersonal.email:
        raise HTTPException(status_code=400, detail="El email es obligatorio")
    return createUserMedicPersonalService(userMedicPersonal, db)
def getUserMedicPersonalController(db: Session = Depends(get_db)) -> list[UserMedicPersonalScheme]:
    return getUserMedicPersonalService(db)
def getUserMedicPersonalByIdController(id: int, db: Session = Depends(get_db)) -> UserMedicPersonalScheme:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    userMedicPersonalToReturn = getUserMedicPersonalByIdService(id, db)
    if not userMedicPersonalToReturn:
        raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
    return userMedicPersonalToReturn
def editUserMedicPersonalController(id: int, userMedicPersonalToEdit: UserMedicPersonalEditScheme, db: Session = Depends(get_db)) -> UserMedicPersonalScheme:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    userMedicPersonalToEditNew = getUserMedicPersonalByIdService(id, db)
    if not userMedicPersonalToEditNew:
        raise HTTPException(status_code=404, detail="No se encontró el Usuario médico personal")
    if userMedicPersonalToEdit.name is not None:
        userMedicPersonalToEditNew.name = userMedicPersonalToEdit.name
    if userMedicPersonalToEdit.email is not None:
        userMedicPersonalToEditNew.email = userMedicPersonalToEdit.email
    updatedUserMedicPersonal = editUserMedicPersonalService(id, userMedicPersonalToEdit, db)
    if updatedUserMedicPersonal:
        return updatedUserMedicPersonal
    else:
        raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
def deleteUserMedicPersonalController(id: int, db: Session = Depends(get_db)) -> str:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    if deleteUserMedicPersonalService(id, db) == False:
        raise HTTPException(status_code=404, detail="No se encontró el Usuario médico personal")
    return "Eliminado con éxito"