from ...Application.Services.userCivilService import (
    getCivilUsersWithoutAccountService,
    getUserAccountsService
)
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from typing import List
from ....Shared.mysql import get_db

def getCivilUsersWithoutAccountController(db: Session = Depends(get_db)) -> List[dict]:
    """Controlador para obtener usuarios civiles sin cuenta"""
    try:
        return getCivilUsersWithoutAccountService(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getUserAccountsController(db: Session = Depends(get_db)) -> List[dict]:
    """Controlador para obtener todas las cuentas de usuario"""
    try:
        return getUserAccountsService(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))