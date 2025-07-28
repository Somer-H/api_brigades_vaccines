from sqlalchemy import Column, Integer, String, ForeignKey, Float
from ....Shared.mysql import Base

class UserCivilModel(Base): 
    __tablename__ = "UserCivil"

    idUserCivil = Column(Integer, primary_key=True, nullable=False, autoincrement= True)
    fol = Column(String, nullable=False)
    corporalTemperature = Column(Float, nullable=False)
    alcoholBreat = Column(Float, nullable=False)
    