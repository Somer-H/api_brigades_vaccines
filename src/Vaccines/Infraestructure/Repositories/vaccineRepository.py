from ...Infraestructure.Models.vaccineModel import VaccineModel
from ...Infraestructure.Models.userCivilModel import UserCivilModel, UserCivilVaccinatedModel
from ...Infraestructure.Models.userModel import User
from ...Domain.Scheme.vaccineScheme import VaccineScheme, VaccineBaseScheme, VaccineEditScheme, VaccineVaccineBoxScheme, UserVaccinatedScheme
from ...Infraestructure.Models.vaccineBoxModel import VaccineBoxVaccineModel, VaccineBoxModel
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import func
def createVaccineRepository (vaccine: VaccineBaseScheme, db: Session) -> VaccineScheme: 
    try: 
        vaccinePost = VaccineModel(**vaccine.dict())
        db.add(vaccinePost)
        db.commit()
        db.refresh(vaccinePost)
        return vaccinePost
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def getVaccinesRepository(db: Session) -> list[VaccineScheme]: 
    try: 
       vaccines = db.query(VaccineModel).all()
       return vaccines
    except Exception as e: 
        HTTPException(status_code=500, detail=str(e))

def getVaccineByIdRepository(id: int, db: Session) -> VaccineScheme:
    try:
        vaccine = db.query(VaccineModel).filter(VaccineModel.idVaccines == id).first()
        return vaccine
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))

def getUsersVaccinatedByIdHospitalRepository(id: int, db: Session) -> list[UserVaccinatedScheme]:
    usersVaccinated = db.query(
        UserCivilModel.idUserCivil,
        UserCivilModel.fol,
        UserCivilModel.name,
        UserCivilModel.firstLastname,
        UserCivilModel.secondLastname,
        UserCivilModel.CURP,
        UserCivilModel.yearsOld,
        UserCivilVaccinatedModel.date,
        VaccineModel.idVaccines,
        VaccineModel.nameVaccine,
        User.name.label('medic_name'),
        User.lastname.label('medic_lastname')
    ).select_from(
        UserCivilModel
    ).join(
        UserCivilVaccinatedModel, 
        UserCivilModel.idUserCivil == UserCivilVaccinatedModel.UserCivil_idUserCivil
    ).join(
        VaccineModel,
        UserCivilVaccinatedModel.Vaccine_idVaccines == VaccineModel.idVaccines
    ).join(
        User,
        UserCivilVaccinatedModel.UserCivil_UserMedicVaccined == User.idUser
    ).filter(
        User.idHospital == str(id)
    ).all()

    return usersVaccinated
def getVaccinesWithVaccinesBoxRepository(db: Session) -> list[VaccineVaccineBoxScheme]:
    try:
        vaccines = db.query(
            VaccineModel.idVaccines,
            VaccineModel.nameVaccine,
            func.count(VaccineBoxModel.idVaccineBox).label('batch'),  # Cuenta las cajas
            func.sum(VaccineBoxModel.amountVaccines).label('availableDoses')  # Suma las dosis
        ).join(
            VaccineBoxVaccineModel, VaccineModel.idVaccines == VaccineBoxVaccineModel.idVaccines
        ).join(
            VaccineBoxModel, VaccineBoxVaccineModel.idVaccineBox == VaccineBoxModel.idVaccineBox
        ).group_by(
            VaccineModel.idVaccines, VaccineModel.nameVaccine
        ).all()
        
        return vaccines
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def editVaccineRepository(vaccineToEdit: VaccineEditScheme, db: Session) -> VaccineScheme: 
    try: 
         db.commit()
         db.refresh(vaccineToEdit)
         return vaccineToEdit
    except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail = str(e))

def deleteVaccineRepository(id: int, db: Session) -> bool: 
    try:
        vaccineToDelete = db.query(VaccineModel).filter(VaccineModel.idVaccines == id).first()
        if not vaccineToDelete:
            #No la ha encontrado
            return False
        db.delete(vaccineToDelete)
        db.commit()
        return True
    except Exception as e: 
        return HTTPException(status_code=500, detail=str(e))