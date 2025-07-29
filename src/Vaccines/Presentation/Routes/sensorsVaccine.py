from fastapi import APIRouter
from ..Controllers.sensorsVaccineController import createSensorsVaccineController, getSensorsVaccineController, sendToGaussController, inputGaussController
router = APIRouter()

router.post("/sensorsVaccine") (createSensorsVaccineController)
router.post("/pointInGauss") (inputGaussController)
router.get("/sensorsVaccine") (getSensorsVaccineController)
router.get("/gaussCurve") (sendToGaussController)