from fastapi import APIRouter
from ..Controllers.vaccineController import createVaccineController, deleteVaccineController, editVaccineController, getVaccineByIdController, getVaccinesController, getVaccineVaccineBoxController

router = APIRouter()

router.post("/vaccine") (createVaccineController)
router.get("/vaccine") (getVaccinesController)
router.get("/vaccine/{id}") (getVaccineByIdController)
router.get("/vaccines/vaccineBox") (getVaccineVaccineBoxController)
router.put("/vaccine/{id}") (editVaccineController)
router.delete("/vaccine/{id}") (deleteVaccineController)
