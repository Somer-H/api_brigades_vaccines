from fastapi import APIRouter
from ..Controllers.sensorsVaccineController import createSensorsVaccineController
router = APIRouter()

router.post("/sensorsVaccine") (createSensorsVaccineController)