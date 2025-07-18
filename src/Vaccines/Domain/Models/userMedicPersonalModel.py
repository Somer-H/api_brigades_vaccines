from ....Shared.mysql import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class UserMedicPersonalModel(Base):
    __tablename__ = "UserMedicPersonal"

    idUserMedicPersonal = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(String(20), nullable=False)
    groupIdGroup = Column(Integer, ForeignKey("Group.idGroup"), nullable=False)
    name = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
