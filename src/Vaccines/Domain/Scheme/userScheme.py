from pydantic import BaseModel
from typing import Optional

class UserSchemeBase(BaseModel):
    username: str
    password: str
    role: str
    groupIdGroup: Optional[int] = None
    name: str
    lastname: str
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

    class Config:
        orm_mode = True
class Login(BaseModel): 
    username: str
    password: str

    class Config: 
        orm_mode = True
class UserResponse(BaseModel): 
    username: str
    role: str
    groupIdGroup: int
    name: str 
    lastname: str
    class Config:
        orm_mode: True