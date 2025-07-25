from fastapi import APIRouter
from ..Controllers.brigadeController import createBrigadeController, getBrigadesController

router = APIRouter()

router.post("/brigades") (createBrigadeController)
router.get("/brigades") (getBrigadesController)