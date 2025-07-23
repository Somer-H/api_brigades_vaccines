from fastapi import APIRouter
from ..Controllers.vaccineBoxController import createVaccineBoxController, getVaccineBoxByIdController, editVaccineBoxController, deleteVaccineBoxController, getVaccineBoxController, createVaccineBoxVaccineController

router = APIRouter()

router.post("/vaccineBox") (createVaccineBoxController)
router.post("/vaccineBoxVaccine") (createVaccineBoxVaccineController)
router.get("/vaccineBox") (getVaccineBoxController)
router.get("/vaccineBox/{id}") (getVaccineBoxByIdController)
router.put("/vaccineBox/{id}") (editVaccineBoxController)
router.delete("/vaccineBox/{id}") (deleteVaccineBoxController)