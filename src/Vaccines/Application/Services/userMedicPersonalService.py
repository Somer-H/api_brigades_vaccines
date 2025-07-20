from ...Infraestructure.Repositories.userMedicPersonal import createUserMedicPersonalRepository, getUserMedicPersonalRepository, getUserMedicPersonalByIdRepository, editUserMedicPersonalRepository, deleteUserMedicPersonalRepository, getUserMedicPersonalByUsernameRepository
from ...Domain.Scheme.userMedicPersonalScheme import UserMedicPersonalScheme, UserMedicPersonalSchemeBase, UserMedicPersonalEditScheme, LoginMedicPersonal, UserMedicPersonalResponse
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
import bcrypt
from ....Shared.MiddleWares.loginMiddlewWare import generateToken
from ....Shared.mysql import get_db
from sqlalchemy.orm import Session
def createUserMedicPersonalService(userMedicPersonal: UserMedicPersonalSchemeBase, db: Session) -> UserMedicPersonalResponse:
    try:
        password = bcrypt.hashpw(userMedicPersonal.password.encode('utf-8'), bcrypt.gensalt())
        print(password)
        password = password.decode('utf-8')
        print(password)
        userMedicPersonal.password = password
        return createUserMedicPersonalRepository(userMedicPersonal, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getUserMedicPersonalService(db: Session) -> list[UserMedicPersonalResponse]:
    try:
        userMedicPersonalList = getUserMedicPersonalRepository(db)
        if not userMedicPersonalList:
            raise HTTPException(status_code=404, detail="No se encontraron Usuarios médicos personales")
        return userMedicPersonalList
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getUserMedicPersonalByUsernameService(username: str, db: Session) -> UserMedicPersonalScheme:
    try: 
        user = getUserMedicPersonalByUsernameRepository(username, db)
        if not user: 
            raise HTTPException(status_code=404, detail="Usuario médico no encontrado")
        return user
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
def getUserMedicPersonalByIdService(id: int, db: Session) -> UserMedicPersonalResponse:
    try:
        userMedicPersonalToReturn = getUserMedicPersonalByIdRepository(id, db)
        if not userMedicPersonalToReturn:
            raise HTTPException(status_code=404, detail="Usuario médico personal no encontrado")
        return userMedicPersonalToReturn
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def editUserMedicPersonalService(id: int, userMedicPersonalToEdit: UserMedicPersonalEditScheme, db: Session) -> UserMedicPersonalResponse:
    try:
        userMedicPersonalToEditNew = getUserMedicPersonalByIdRepository(id, db)
        if not userMedicPersonalToEditNew:
            raise HTTPException(status_code=404, detail="No se encontró el Usuario médico personal")
        if userMedicPersonalToEdit.name is not None:
            userMedicPersonalToEditNew.name = userMedicPersonalToEdit.name

        if userMedicPersonalToEdit.username is not None: 
            userMedicPersonalToEditNew.username = userMedicPersonalToEdit.username

        if userMedicPersonalToEdit.groupIdGroup is not None: 
            userMedicPersonalToEditNew.groupIdGroup

        if userMedicPersonalToEdit.role is not None: 
            userMedicPersonalToEditNew.role = userMedicPersonalToEdit.role

        if userMedicPersonalToEdit.lastname is not None:
            userMedicPersonalToEditNew.lastname = userMedicPersonalToEdit.lastname

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
def loginMedicPersonalService(user: str, password: str, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        userFound = getUserMedicPersonalByUsernameService(user, db)
        if not userFound:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        if not bcrypt.checkpw(password.encode('utf-8'), userFound.password.encode('utf-8')):
            print(userFound.password)
            raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        token = generateToken(user, password)
        response_data = UserMedicPersonalResponse(
            username=userFound.username,
            role=userFound.role,
            groupIdGroup=userFound.groupIdGroup,
            name=userFound.name,
            lastname=userFound.lastname,
        )
        response_json = response_data.dict()
        response = JSONResponse(content=response_json, status_code=200)
        response.headers["Authorization"] = f"Bearer {token}"
        return response
    except Exception as e:
        print(f"Error en loginMedicRepository: {e}")
        raise HTTPException(status_code=500, detail=str(e))
