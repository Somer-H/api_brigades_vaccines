from fastapi import APIRouter
from ..Controllers.sensorsVaccineController import createSensorsVaccineController, getSensorsVaccineController
router = APIRouter()

router.post("/sensorsVaccine") (createSensorsVaccineController)
router.get("/sensorsVaccine") (getSensorsVaccineController)