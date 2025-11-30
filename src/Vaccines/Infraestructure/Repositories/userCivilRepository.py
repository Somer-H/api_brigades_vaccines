from ..Models.userCivilModel import UserCivilModel
from ..Models.userModel import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List

def getCivilUsersWithoutAccountRepository(db: Session) -> List[UserCivilModel]:
    """Obtiene usuarios civiles que no tienen cuenta de usuario"""
    try:
        # Subconsulta para obtener IDs de civiles que ya tienen cuenta
        users_with_account = db.query(User.idUserCivil).filter(
            User.idUserCivil.isnot(None)
        ).subquery()
        
        # Consulta principal: civiles sin cuenta
        civil_users = db.query(UserCivilModel).filter(
            ~UserCivilModel.idUserCivil.in_(users_with_account)
        ).all()
        
        return civil_users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios civiles: {str(e)}")

def getUserAccountsRepository(db: Session) -> List[User]:
    """Obtiene todas las cuentas de usuario con rol de paciente y su información de usuario civil"""
    try:
        accounts = db.query(User).filter(
            User.idUserCivil.isnot(None),
            User.role == "paciente"
        ).all()
        return accounts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener cuentas: {str(e)}")