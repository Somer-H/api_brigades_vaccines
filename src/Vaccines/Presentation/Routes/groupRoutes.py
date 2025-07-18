from fastapi import APIRouter
from ..Controllers.groupController import createGroupController, getGroupController, getGroupByIdController, editGroupController, deleteGroupController

router = APIRouter()

router.post("/groups") (createGroupController)
router.get("/groups") (getGroupController)
router.get("/groups/{id}") (getGroupByIdController)
router.put("/groups/{id}") (createGroupController)
router.delete("/groups/{id}") (getGroupController)