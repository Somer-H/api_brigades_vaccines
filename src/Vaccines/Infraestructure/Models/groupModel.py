from ....Shared.mysql import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class GroupModel(Base):
    __tablename__ = "Group"
    
    idGroup = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    nameGroup = Column(String(50), nullable=False)
    dateGroup = Column(String(50), nullable=False)
    idVaccineBox = Column(Integer, ForeignKey("VaccineBox.idVaccineBox"), nullable=False)