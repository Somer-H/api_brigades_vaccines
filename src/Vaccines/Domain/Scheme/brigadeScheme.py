from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
class LocationSchemeBase(BaseModel): 
    idBrigade : int
    location: str
    class Config:
        orm_mode = True

class LocationScheme(LocationSchemeBase): 
    idLocation: int
    
class BrigateRequestScheme(BaseModel): 
    referenceBrigade: str
    startDate: datetime
    endDate: datetime
    locations: List[str]

    class Config: 
        orm_mode = True

class BrigateResponseWithLocationsScheme(BrigateRequestScheme): 
    idBrigade: int

class BrigateScheme(BaseModel):
    referenceBrigade: str
    startDate: datetime
    endDate: datetime
    class Config: 
        orm_mode = True
class BrigateResponseScheme(BrigateScheme): 
    idBrigade: int
    class Config: 
        orm_mode = True
class BrigateUpdateScheme(BaseModel): 
    referenceBrigade: Optional[str] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    class Config: 
        orm_mode = True