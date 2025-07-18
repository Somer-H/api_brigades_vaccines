from sqlalchemy.orm import Session
from fastapi import HTTPException
from ...Domain.Scheme.groupScheme import GroupSchemeBase, GroupScheme
from ...Infraestructure.Repositories.groupRepository import createGroupRepository, getGroupRepository, getGroupByIdRepository, editGroupRepository, deleteGroupRepository
def createGroupService(group: GroupSchemeBase, db: Session) -> GroupScheme:
      try: 
        return createGroupRepository(group, db)
      except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))
def getGroupService(db: Session) -> list[GroupScheme]:
    try: 
        groupGet = getGroupRepository(db)
        if not groupGet:
            raise HTTPException(status_code=404, detail="No se encontraron Grupos")
        return groupGet
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getGroupByIdService(id: int, db: Session) -> GroupScheme:
    try:
        groupToReturn = getGroupByIdRepository(id, db)
        if not groupToReturn:
            raise HTTPException(status_code=404, detail="Grupo no encontrado")
        return groupToReturn
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def editGroupService(id: int, groupToEdit: GroupScheme, db: Session) -> GroupScheme:
    try: 
        groupToEditNew = getGroupByIdRepository(id, db)
        if not groupToEditNew:
            raise HTTPException(status_code=404, detail="No se encontró el Grupo")
        if groupToEdit.nameGroup is not None:
            groupToEditNew.nameGroup = groupToEdit.nameGroup
        if groupToEdit.dateGroup is not None:
            groupToEditNew.dateGroup = groupToEdit.dateGroup
        updatedGroup = editGroupRepository(groupToEditNew, db)
        if updatedGroup:
            return updatedGroup
        else:
            raise HTTPException(status_code=404, detail="Grupo no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def deleteGroupService(id: int, db: Session) -> str:
    try:
        if deleteGroupRepository(id, db) == False:
            raise HTTPException(status_code=404, detail="No se encontró el Grupo")
        return "Eliminado con éxito"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))