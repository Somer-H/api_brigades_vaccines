from sqlalchemy import Column, Integer, String, ForeignKey, Float
from ....Shared.mysql import Base

class SensorsVaccineModel(Base): 
    __tablename__ = "SensorsVaccine"
    
    idSensorsVaccine = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    measurementUnit = Column(String, nullable=False)
    nameSensor = Column(String, nullable=False)
    information = Column(Float, nullable=False)
    idVaccineBox = Column(Integer, ForeignKey("VaccineBox.idVaccineBox"), nullable=False)