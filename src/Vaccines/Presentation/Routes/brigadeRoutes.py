from fastapi import APIRouter
from ..Controllers.brigadeController import createBrigadeController, getBrigadesController, getBrigadeWithLocationsByIdController, editBrigadeController, editLocationController, deleteBrigadeController, deleteLocationController

router = APIRouter()

router.post("/brigades") (createBrigadeController)
router.get("/brigades") (getBrigadesController)
router.get("/brigades/{id}") (getBrigadeWithLocationsByIdController)
router.put("/brigades/{id}") (editBrigadeController)
router.put("/brigades/location/{id}") (editLocationController)
router.delete("/brigade/{id}") (deleteBrigadeController)
router.delete("/brigate/locationY/{id}") (deleteLocationController)