from ...Application.Services.userService import createUserService, getUserService, getUserByIdService, editUserService, deleteUserService, loginService, getLeadersAndNurseService
from ...Domain.Scheme.userScheme import UserSchemeBase, UserResponse, UserEditScheme, Login
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from ....Shared.auth import jwtAuth
from ....Shared.mysql import get_db
def createUserController(user: UserSchemeBase, db: Session = Depends(get_db)) -> UserResponse:
    if not user.name:
        raise HTTPException(status_code=400, detail="El nombre es obligatorio")
    if not user.lastname:
        raise HTTPException(status_code=400, detail="El apellido es obligatorio")
    if not user.password: 
        raise HTTPException(status_code=400, detail="Campo obligatirio")
    if not user.role: 
        raise HTTPException (status_code=400, detail="Campo obligatorio")
    return createUserService(user, db)
def getUserController(db: Session = Depends(get_db)) -> list[UserResponse]:
    return getUserService(db)

def getLeadersAndNurseController(db: Session = Depends(get_db)) -> list[UserResponse]:
    return getLeadersAndNurseService(db)
def getUserByIdController(id: int, db: Session = Depends(get_db)) -> UserResponse:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    userMedicPersonalToReturn = getUserByIdService(id, db)
    if not userMedicPersonalToReturn:
        raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
    return userMedicPersonalToReturn
def editUserController(id: int, userToEdit: UserEditScheme, db: Session = Depends(get_db)) -> UserResponse:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    updatedUserMedicPersonal = editUserService(id, userToEdit, db)
    if updatedUserMedicPersonal:
        return updatedUserMedicPersonal
    else:
        raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
def deleteUserController(id: int, db: Session = Depends(get_db)) -> str:
    if not id:
        raise HTTPException(status_code=400, detail="Se requiere un ID")
    if id < 0:
        raise HTTPException(status_code=400, detail="La ID no puede ser negativa")
    if deleteUserService(id, db) == False:
        raise HTTPException(status_code=404, detail="No se encontró el Usuario médico personal")
    return "Eliminado con éxito"

def loginController(userToLog: Login, db: Session = Depends(get_db)) -> JSONResponse: 
    # Validaciones básicas
    if not userToLog.username or userToLog.username.strip() == "": 
        raise HTTPException(
            status_code=400, 
            detail="El nombre de usuario es obligatorio"
        )
    
    if not userToLog.password or userToLog.password.strip() == "": 
        raise HTTPException(
            status_code=400, 
            detail="La contraseña es obligatoria"
        )
    
    print("username", userToLog.username)
    
    # Llamar al servicio (que maneja los errores específicos)
    return loginService(userToLog.username, userToLog.password, db)