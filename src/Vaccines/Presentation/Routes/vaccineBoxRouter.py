from fastapi import APIRouter, Depends
from ..Controllers.vaccineBoxController import createVaccineBoxController, getVaccineBoxByIdController, editVaccineBoxController, deleteVaccineBoxController, getVaccineBoxController

router = APIRouter()

router.post("/vaccineBox") (createVaccineBoxController)
router.get("/vaccineBox") (getVaccineBoxController)
router.get("/vaccineBox/{id}") (getVaccineBoxByIdController)
router.put("/vaccineBox/{id}") (editVaccineBoxController)
router.delete("/vaccineBox/{id}") (deleteVaccineBoxController)