from pydantic import BaseModel
from typing import Optional

class UserSchemeBase(BaseModel):
    username: str
    password: str
    role: str
    groupIdGroup: Optional[int] = None
    name: str
    lastname: str
    idHospital: Optional[int] = None
    idUserCivil: Optional[int] = None
    class Config:
        orm_mode = True
class UserScheme(UserSchemeBase):
    idUser: int

    class Config:
        orm_mode = True
class UserEditScheme(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
    groupIdGroup: Optional[int] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    idHospital: Optional[int] = None
    idUserCivil : Optional[int] = None
    class Config:
        orm_mode = True
class Login(BaseModel): 
    username: str
    password: str

    class Config: 
        orm_mode = True
class UserResponse(BaseModel):
    idUser: int
    username: str
    role: str
    groupIdGroup: Optional[int] = None
    name: str 
    lastname: str
    idHospital: Optional[int] = None
    idUserCivil: Optional[int] = None
    class Config:
        orm_mode: True