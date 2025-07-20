from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from src.Vaccines.Presentation.Routes.vaccineBoxRouter import router as VaccineBoxRouter
from src.Vaccines.Presentation.Routes.sensorsVaccine import router as SensorsVaccineRouter
from src.Vaccines.Presentation.Routes.userMedicPersonaRouter import router as UserMedicPersonaRouter
from src.Vaccines.Presentation.Routes.groupRoutes import router as GroupsRouter
security = HTTPBearer()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)
app.include_router(VaccineBoxRouter, prefix="/api", tags=["VaccineBoxes"])
app.include_router(SensorsVaccineRouter, prefix="/api", tags=["SensorsVaccine"])
app.include_router(GroupsRouter, prefix="/api", tags=["Groups"])
app.include_router(UserMedicPersonaRouter, prefix="/api", tags=["UserMedicPersona"])