from ..Controllers.userController import createUserController, getUserController, getUserByIdController, editUserController, deleteUserController, loginController
from fastapi import APIRouter

router = APIRouter()

router.post("/userMedicPersona") (createUserController)
router.get("/userMedicPersona") (getUserController)
router.get("/userMedicPersona/{id}") (getUserByIdController)
router.put("/userMedicPersona/{id}") (editUserController)
router.delete("/userMedicPersona/{id}") (deleteUserController)
router.post("/login/userMedicPersona") (loginController)