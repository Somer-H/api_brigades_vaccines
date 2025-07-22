from ...Application.Services.groupService import createGroupService, deleteGroupService, editGroupService, getGroupByIdService, getGroupService
from ...Domain.Scheme.groupScheme import GroupSchemeBase, GroupScheme, GroupEditScheme
from fastapi import Depends, HTTPException
from ....Shared.mysql import get_db
from ....Shared.auth import jwtAuth
from sqlalchemy.orm import Session
def createGroupController(group: GroupSchemeBase, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director"))) -> GroupScheme:
    if not group.nameGroup or not group.dateGroup:
        raise HTTPException("El nombre y la fecha del grupo son obligatorios")
    if not group.idVaccineBox:
        raise HTTPException("Se requiere una Hielera de vacunas relacionada")
    if not group.dateGroup: 
        raise HTTPException("Se requiere una fecha para el grupo")    
    return createGroupService(group, db)

def getGroupController(db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director"))) -> list[GroupScheme]:
        groupGet = getGroupService(db)
        return groupGet 
def getGroupByIdController(id: int, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director"))) -> GroupScheme:
    if not id:
        raise HTTPException("Se requiere un ID")
    if id < 0:
        raise HTTPException("La ID no puede ser negativa")
    return getGroupByIdService(id, db)

def editGroupController(id: int, groupToEdit: GroupEditScheme, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director"))) -> GroupScheme:
    if not id:
        raise HTTPException("Se requiere un ID")
    if id < 0:
        raise HTTPException("La ID no puede ser negativa")
    return editGroupService(id, groupToEdit, db)

def deleteGroupController(id: int, db: Session = Depends(get_db), userData = jwtAuth(expectedRoles=("director"))) -> str:
    if not id:
        raise HTTPException("Se requiere un ID")
    if id < 0:
        raise HTTPException("La ID no puede ser negativa")
    return deleteGroupService(id, db)