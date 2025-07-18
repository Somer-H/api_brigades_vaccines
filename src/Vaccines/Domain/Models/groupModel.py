from ....Shared.mysql import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class GroupModel(Base):
    __tablename__ = "Vaccine"
    
    idGroup = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    nameGroup = Column(String(50), nullable=False)
    dateGroup = Column(String(50), nullable=False)
    VaccineBox = Column(Integer, ForeignKey("VaccineBox.idVaccineBox"), nullable=False)