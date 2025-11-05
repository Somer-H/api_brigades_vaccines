from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from src.Vaccines.Presentation.Routes.vaccineBoxRouter import router as VaccineBoxRouter
from src.Vaccines.Presentation.Routes.sensorsVaccine import router as SensorsVaccineRouter
from src.Vaccines.Presentation.Routes.userRouter import router as User
from src.Vaccines.Presentation.Routes.groupRoutes import router as GroupsRouter
from src.Vaccines.Presentation.Routes.vaccineRoutes import router as VaccineRouter
from src.Vaccines.Presentation.Routes.brigadeRoutes import router as BrigadeRouter
from src.Shared.create_users import create_demo_users

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


@app.on_event("startup")
async def startup_event():
    """Se ejecuta al iniciar la aplicación crea 3 usuarios con cada uno de los roles"""
    print("Iniciando aplicación...")
    create_demo_users()
    print("Aplicación lista")

app.include_router(User, prefix="/api", tags=["Users"])
app.include_router(VaccineBoxRouter, prefix="/api", tags=["VaccineBoxes"])
app.include_router(SensorsVaccineRouter, prefix="/api", tags=["SensorsVaccine"])
app.include_router(GroupsRouter, prefix="/api", tags=["Groups"])
app.include_router(VaccineRouter, prefix="/api", tags=["Vaccines"])
app.include_router(BrigadeRouter, prefix="/api", tags=["Brigades"])