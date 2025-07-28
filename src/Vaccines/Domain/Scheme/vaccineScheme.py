from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class VaccineBaseScheme(BaseModel):
    nameVaccine: str

    class Config:
        orm_mode = True
class VaccineScheme(VaccineBaseScheme):
    idVaccines: int

    class Config:
        orm_mode = True
class VaccineEditScheme(BaseModel):
    nameVaccine: Optional[str] = None

    class Config:
        orm_mode = True

class VaccineVaccineBoxScheme(BaseModel):
    idVaccines: int
    nameVaccine: str
    batch: int 
    availableDoses: int 
    
    class Config:
        from_attributes = True

class UserVaccinatedScheme(BaseModel):
    idUserCivil: int
    fol: str
    corporalTemperature: float
    alcoholBreat: float
    name: Optional[str] = None
    firstLastname: Optional[str] = None
    secondLastname: Optional[str] = None
    CURP: Optional[str] = None
    dayBirthday: Optional[int] = None
    monthBirthday: Optional[str] = None
    yearBirthday: Optional[str] = None
    yearsOld: Optional[int] = None
    school: Optional[int] = None
    schoolGrade: Optional[str] = None
    
    UserCivil_idUserCivil: int
    UserCivil_UserMedicVaccined: int
    Vaccine_idVaccines: Optional[int] = None
    date: datetime
    
    idVaccines: Optional[int] = None
    nameVaccine: str
    
    idUser: int
    username: str
    role: str
    groupIdGroup: Optional[int] = None
    medicName: str
    medicLastname: str
    idHospital: Optional[str] = None
    idUserCivil_User: Optional[str] = None
    
    class Config:
        from_attributes = True