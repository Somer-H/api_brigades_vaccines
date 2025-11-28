from ...Infraestructure.Repositories.userCivilRepository import (
    getCivilUsersWithoutAccountRepository,
    getUserAccountsRepository
)
from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List

def getCivilUsersWithoutAccountService(db: Session) -> List[dict]:
    """Servicio para obtener usuarios civiles sin cuenta"""
    try:
        civil_users = getCivilUsersWithoutAccountRepository(db)
        
        if not civil_users:
            return []
        
        # Formatear la respuesta
        result = []
        for user in civil_users:
            result.append({
                "idUserCivil": user.idUserCivil,
                "name": user.name or "",
                "firstLastname": user.firstLastname or "",
                "secondLastname": user.secondLastname or "",
                "CURP": user.CURP or "",
                "fol": user.fol or ""
            })
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getUserAccountsService(db: Session) -> List[dict]:
    """Servicio para obtener todas las cuentas de usuario"""
    try:
        accounts = getUserAccountsRepository(db)
        
        if not accounts:
            return []
        
        # Formatear la respuesta
        result = []
        for account in accounts:
            result.append({
                "idUser": account.idUser,
                "username": account.username,
                "name": account.name,
                "lastname": account.lastname,
                "role": account.role,
                "idUserCivil": account.idUserCivil or ""
            })
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))