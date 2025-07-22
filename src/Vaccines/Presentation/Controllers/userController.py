from ...Application.Services.userService import createUserMedicPersonalService, getUserMedicPersonalService, getUserMedicPersonalByIdService, editUserMedicPersonalService, deleteUserMedicPersonalService, loginMedicPersonalService
from ...Domain.Scheme.userScheme import UserSchemeBase, UserMedicPersonalScheme, UserMedicPersonalEditScheme, LoginMedicPersonal
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from ....Shared.auth import jwtAuth
from ....Shared.mysql import get_db
def createUserMedicPersonalController(userMedicPersonal: UserSchemeBase, db: Session = Depends(get_db)) -> UserMedicPersonalScheme:
    if not userMedicPersonal.name:
        raise HTTPException(status_code=400, detail="El nombre es obligatorio")
    if not userMedicPersonal.lastname:
        raise HTTPException(status_code=400, detail="El apellido es obligatorio")
    if not userMedicPersonal.password: 
        raise HTTPException(status_code=400, detail="Campo obligatirio")
    if not userMedicPersonal.groupIdGroup: 
        raise HTTPException(status_code=400, detail="Campo obligatorio")
    if not userMedicPersonal.role: 
        raise HTTPException (status_code=400, detail="Campo obligatorio")
    return createUserMedicPersonalService(userMedicPersonal, db)
def getUserMedicPersonalController(db: Session = Depends(get_db)) -> list[UserMedicPersonalScheme]:
    return getUserMedicPersonalService(db)
def getUserMedicPersonalByIdController(id: int, db: Session = Depends(get_db), userData = Depends(jwtAuth)) -> UserMedicPersonalScheme:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    userMedicPersonalToReturn = getUserMedicPersonalByIdService(id, db)
    if not userMedicPersonalToReturn:
        raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
    return userMedicPersonalToReturn
def editUserMedicPersonalController(id: int, userMedicPersonalToEdit: UserMedicPersonalEditScheme, db: Session = Depends(get_db), userData = Depends(jwtAuth)) -> UserMedicPersonalScheme:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    userMedicPersonalToEditNew = getUserMedicPersonalByIdService(id, db)
    if not userMedicPersonalToEditNew:
        raise HTTPException(status_code=404, detail="No se encontró el Usuario médico personal")
    if userMedicPersonalToEdit.name is not None:
        userMedicPersonalToEditNew.name = userMedicPersonalToEdit.name
    updatedUserMedicPersonal = editUserMedicPersonalService(id, userMedicPersonalToEdit, db)
    if updatedUserMedicPersonal:
        return updatedUserMedicPersonal
    else:
        raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
def deleteUserMedicPersonalController(id: int, db: Session = Depends(get_db), userData = Depends(jwtAuth)) -> str:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    if deleteUserMedicPersonalService(id, db) == False:
        raise HTTPException(status_code=404, detail="No se encontró el Usuario médico personal")
    return "Eliminado con éxito"

def loginMedicPersonalController(userToLog: LoginMedicPersonal, db: Session = Depends(get_db)) -> JSONResponse: 
    if not userToLog.username: 
        raise HTTPException(status_code=400, detail="Necesita proporcionar un nombre de usuario")
    if not userToLog.password: 
        raise HTTPException(status_code=400, detail="Necesita proporcionar una contraseña")
    return loginMedicPersonalService(userToLog.username,userToLog.password, db)