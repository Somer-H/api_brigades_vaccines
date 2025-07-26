from fastapi import APIRouter
from ..Controllers.sensorsVaccineController import createSensorsVaccineController, getSensorsVaccineController, sendToGaussController
router = APIRouter()

router.post("/sensorsVaccine") (createSensorsVaccineController)
router.get("/sensorsVaccine") (getSensorsVaccineController)
router.get("/gaussCurve") (sendToGaussController)