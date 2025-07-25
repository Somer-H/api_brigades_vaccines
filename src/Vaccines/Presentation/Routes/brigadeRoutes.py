from fastapi import APIRouter
from ..Controllers.brigadeController import createBrigadeController, getBrigadesController, getBrigadeWithLocationsByIdController, editBrigadeController

router = APIRouter()

router.post("/brigades") (createBrigadeController)
router.get("/brigades") (getBrigadesController)
router.get("/brigades/{id}") (getBrigadeWithLocationsByIdController)
router.put("/brigades/{id}") (editBrigadeController)