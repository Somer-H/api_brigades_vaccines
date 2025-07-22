from pydantic import BaseModel
from typing import Optional

class UserSchemeBase(BaseModel):
    username: str
    password: str
    role: str
    groupIdGroup: int
    name: str
    lastname: str
    class Config:
        orm_mode = True
class UserMedicPersonalScheme(UserSchemeBase):
    idUserMedicPersonal: int

    class Config:
        orm_mode = True
class UserMedicPersonalEditScheme(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
    groupIdGroup: Optional[int] = None
    name: Optional[str] = None
    lastname: Optional[str] = None

    class Config:
        orm_mode = True
class LoginMedicPersonal(BaseModel): 
    username: str
    password: str

    class Config: 
        orm_mode = True
class UserMedicPersonalResponse(BaseModel): 
    username: str
    role: str
    groupIdGroup: int
    name: str 
    lastname: str
    class Config:
        orm_mode: True