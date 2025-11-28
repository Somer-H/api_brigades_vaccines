from ..Controllers.userController import (
    createUserController, 
    getUserController, 
    getUserByIdController, 
    editUserController, 
    deleteUserController, 
    loginController, 
    getLeadersAndNurseController
)
from ..Controllers.userCivilController import (
    getCivilUsersWithoutAccountController,
    getUserAccountsController
)
from fastapi import APIRouter

router = APIRouter()

router.post("/users")(createUserController)
router.get("/userMedicPersona")(getUserController)
router.get("/leadersAndNurse")(getLeadersAndNurseController)
router.get("/userMedicPersona/{id}")(getUserByIdController)
router.put("/userMedicPersona/{id}")(editUserController)
router.delete("/users/{id}")(deleteUserController)
router.post("/login/userMedicPersona")(loginController)
router.get("/users-civil/without-account")(getCivilUsersWithoutAccountController)
router.get("/user-accounts")(getUserAccountsController)