from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from ....Shared.mysql import Base

class UserCivilModel(Base): 
    __tablename__ = "UserCivil"

    idUserCivil = Column(Integer, primary_key=True, nullable=False, autoincrement= True)
    fol = Column(String(100), nullable=False)
    corporalTemperature = Column(Float, nullable=False)
    alcoholBreat = Column(Float, nullable=False)
    name = Column(String(100), nullable=True)
    firstLastname = Column(String(100), nullable=True)
    CURP = Column(String(18), nullable=True)
    secondLastname = Column(String(100), nullable=True)
    dayBirthday = Column(Integer, nullable=True)
    monthBirthday = Column(String(20), nullable=True)
    yearBirthday = Column(String(4), nullable=True)
    yearsOld = Column(Integer, nullable=True)
    school = Column(Integer, nullable=True)
    schoolGrade = Column(String(50), nullable= True)

class UserCivilVaccinatedModel(Base): 
    __tablename__ = "UserCivilVaccinated" 

    UserCivil_idUserCivil = Column(Integer, ForeignKey("UserCivil.idUserCivil"), primary_key= True, nullable=True)
    UserCivil_UserMedicVaccined = Column(Integer, ForeignKey("User.idUser"),primary_key=True, nullable=True)
    Vaccine_idVaccines = Column(Integer, ForeignKey("Vaccine.idVaccines"), nullable=True)
    date = Column(DateTime, nullable=False)