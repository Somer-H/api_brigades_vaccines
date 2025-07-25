from fastapi import APIRouter
from ..Controllers.brigadeController import createBrigadeController

router = APIRouter()

router.post("/brigades") (createBrigadeController)