from sqlalchemy import Column, Integer, String, ForeignKey
from ....Shared.mysql import Base

class VaccineBoxModel(Base):
    __tablename__ = "VaccineBox"
    
    idVaccineBox = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    amountVaccines = Column(Integer, nullable=False)