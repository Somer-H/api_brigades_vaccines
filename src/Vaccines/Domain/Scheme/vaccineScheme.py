from pydantic import BaseModel
from typing import Optional
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