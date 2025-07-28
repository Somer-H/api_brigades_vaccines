from fastapi import APIRouter
from ..Controllers.vaccineController import createVaccineController, deleteVaccineController, editVaccineController, getVaccineByIdController, getVaccinesController, getVaccineVaccineBoxController, getUsersVaccinatedController

router = APIRouter()

router.post("/vaccine") (createVaccineController)
router.get("/vaccine") (getVaccinesController)
router.get("/vaccine/{id}") (getVaccineByIdController)
router.get("/vaccines/vaccineBox") (getVaccineVaccineBoxController)
router.get("/usersVaccinated") (getUsersVaccinatedController)
router.put("/vaccine/{id}") (editVaccineController)
router.delete("/vaccine/{id}") (deleteVaccineController)
