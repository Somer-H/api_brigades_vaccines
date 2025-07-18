from ..Controllers.userMedicPersonalController import createUserMedicPersonalController, getUserMedicPersonalController, getUserMedicPersonalByIdController, editUserMedicPersonalController, deleteUserMedicPersonalController
from fastapi import APIRouter

router = APIRouter()

router.post("/userMedicPersona") (createUserMedicPersonalController)
router.get("/userMedicPersona") (getUserMedicPersonalController)
router.get("/userMedicPersona/{id}") (getUserMedicPersonalByIdController)
router.put("/userMedicPersona/{id}") (editUserMedicPersonalController)
router.delete("/userMedicPersona/{id}") (deleteUserMedicPersonalController)