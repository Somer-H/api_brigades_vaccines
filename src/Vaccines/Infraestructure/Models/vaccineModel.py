from ....Shared.mysql import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class VaccineModel(Base):
    __tablename__ = "Vaccine"
    
    idVaccines = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    nameVaccine = Column(String(50), nullable=False)