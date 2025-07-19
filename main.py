from fastapi import FastAPI
from src.Vaccines.Presentation.Routes.vaccineBoxRouter import router as VaccineBoxRouter
from src.Vaccines.Presentation.Routes.sensorsVaccine import router as SensorsVaccineRouter
from src.Vaccines.Presentation.Routes.userMedicPersonaController import router as UserMedicPersonaRouter
app = FastAPI()
app.include_router(VaccineBoxRouter, prefix="/api", tags=["VaccineBoxes"])
app.include_router(SensorsVaccineRouter, prefix="/api", tags=["SensorsVaccine"])
app.include_router(UserMedicPersonaRouter, prefix="/api", tags=["UserMedicPersona"])