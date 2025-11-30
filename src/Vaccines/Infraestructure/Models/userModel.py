from ....Shared.mysql import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = "User"

    idUser = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(200), nullable=True)
    role = Column(String(20), nullable=False)
    groupIdGroup = Column(Integer, ForeignKey("Group.idGroup"), nullable=True)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    idHospital = Column(String(50), nullable=True)
    idUserCivil = Column(Integer, nullable=True)