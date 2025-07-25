from ....Shared.mysql import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class BrigadeModel(Base):
    __tablename__ = "Brigade"

    idBrigade = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    referenceBrigade = Column(String, nullable=False)
    startDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime, nullable=False)

class LocationModel(Base):
    __tablename__ = "Location"

    idLocation = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    idBrigade = Column(Integer, ForeignKey("Brigade.idBrigade"), primary_key=True, nullable=False)
    location = Column(String, nullable=False)