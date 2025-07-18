from pydantic import BaseModel
from typing import Optional

class GroupSchemeBase(BaseModel):
    nameGroup: str
    dateGroup: str
    idVaccineBox: int

    class Config:
        orm_mode = True
class GroupScheme(GroupSchemeBase):
    idGroup: int

    class Config:
        orm_mode = True
class GroupEditScheme(BaseModel):
    nameGroup: Optional[str] = None
    dateGroup: Optional[str] = None
    idVaccineBox: Optional[int] = None

    class Config:
        orm_mode = True