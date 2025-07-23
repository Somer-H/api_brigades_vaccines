from pydantic import BaseModel
from typing import Optional, List

class VaccineBoxBase(BaseModel):
  amountVaccines : int

class VaccineBox(VaccineBoxBase):
    idVaccineBox: int
    class Config:
        orm_mode = True

class EditVaccineBox(BaseModel):
    amountVaccines: Optional[int] = None

    class Config:
        orm_mode = True

class VaccineBoxVaccinesScheme(BaseModel): 
    idVaccineBox : int
    idVaccines: List[int]

class VaccineBoxVaccineScheme(BaseModel): 
    idVaccineBox: int
    idVaccines: int