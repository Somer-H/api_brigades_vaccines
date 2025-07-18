from pydantic import BaseModel
from typing import Optional

class UserMedicPersonalSchemeBase(BaseModel):
    username: str
    password: str
    role: str
    groupIdGroup: int
    name: str
    lastName: str
    class Config:
        orm_mode = True
class UserMedicPersonalScheme(UserMedicPersonalSchemeBase):
    idUserMedicPersonal: int

    class Config:
        orm_mode = True
class UserMedicPersonalEditScheme(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
    groupIdGroup: Optional[int] = None
    name: Optional[str] = None
    lastName: Optional[str] = None

    class Config:
        orm_mode = True