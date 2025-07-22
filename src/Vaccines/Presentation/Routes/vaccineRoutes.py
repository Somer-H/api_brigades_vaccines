from fastapi import APIRouter
from ..Controllers.vaccineController import createVaccineController, deleteVaccineController, editVaccineController, getVaccineByIdController, getVaccinesController

router = APIRouter()

router.post("/vaccine") (createVaccineController)
router.get("/vaccine") (getVaccinesController)
router.get("/vaccine/{id}") (getVaccineByIdController)
router.put("/vaccine/{id}") (editVaccineController)
router.delete("/vaccine/{id}") (deleteVaccineController)