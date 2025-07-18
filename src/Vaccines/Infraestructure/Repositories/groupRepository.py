from ...Domain.Models.groupModel import GroupModel
from ...Domain.Scheme.groupScheme import GroupSchemeBase, GroupScheme
from sqlalchemy.orm import Session

def createGroupRepository(group: GroupSchemeBase, db: Session) -> GroupScheme:
    try:
        groupToPost = GroupModel(**group.dict())
        db.add(groupToPost)
        db.commit()
        db.refresh(groupToPost)
        return groupToPost
    except Exception as e:
        db.rollback()
        raise e
def getGroupRepository(db: Session) -> list[GroupScheme]:
    try:
        groupList = db.query(GroupModel).all()
        return groupList
    except Exception as e:
        raise e
def getGroupByIdRepository(id: int, db: Session) -> GroupScheme:
    try:
        groupToReturn = db.query(GroupModel).filter(GroupModel.idGroup == id).first()
        return groupToReturn
    except Exception as e:
        raise e
def editGroupRepository(groupToEdit: GroupScheme, db: Session) -> GroupScheme:
    try: 
        db.commit()
        db.refresh(groupToEdit)
        return groupToEdit
    except Exception as e:
        db.rollback()
        raise e
def deleteGroupRepository(id: int, db: Session) -> bool | None:
    try:
        groupToDelete = db.query(GroupModel).filter(GroupModel.idGroup == id).first()
        if not groupToDelete:
            # No la encontró
            return False
        db.delete(groupToDelete)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise e