from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from ....Shared.mysql import Base

class UserCivilModel(Base): 
    __tablename__ = "UserCivil"

    idUserCivil = Column(Integer, primary_key=True, nullable=False, autoincrement= True)
    fol = Column(String, nullable=False)
    corporalTemperature = Column(Float, nullable=False)
    alcoholBreat = Column(Float, nullable=False)
    name = Column(String, nullable=True)
    firstLastname = Column(String, nullable=True)
    CURP = Column(String, nullable=True)
    secondLastname = Column(String, nullable=True)
    dayBirthday = Column(Integer, nullable=True)
    monthBirthday = Column(String, nullable=True)
    yearBirthday = Column(String, nullable=True)
    yearsOld = Column(Integer, nullable=True)
    school = Column(Integer, nullable=True)
    schoolGrade = Column(String, nullable= True)

class UserCivilVaccinatedModel(Base): 
    __tablename__ = "UserCivilVaccinated" 

    UserCivil_idUserCivil = Column(Integer, ForeignKey("UserCivil.idUserCivil"), primary_key= True, nullable=True)
    UserCivil_UserMedicVaccined = Column(Integer, ForeignKey("User.idUser"),primary_key=True, nullable=True)
    Vaccine_idVaccines = Column(Integer, ForeignKey("Vaccine.idVaccine"), nullable=True)
    date = Column(DateTime, nullable=False)