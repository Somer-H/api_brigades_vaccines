from ...Infraestructure.Models.brigadeModel import BrigadeModel, LocationModel
from ...Domain.Scheme.brigadeScheme import BrigateScheme, BrigadeFullScheme, LocationScheme, LocationSchemeBase, BrigadeAndLocationsScheme
from sqlalchemy.orm import Session
from fastapi import HTTPException
def createBrigadeRepository(brigate: BrigateScheme, db: Session) -> BrigadeFullScheme: 
    try: 
        brigateToPost = BrigadeModel(**brigate.dict())
        db.add(brigateToPost)
        db.commit()
        db.refresh(brigateToPost)
        return brigateToPost
    except Exception as e: 
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def createLocationRepository(location: LocationSchemeBase, db: Session) -> LocationScheme: 
    try:
        locationPost = LocationModel(**location.dict())
        db.add(locationPost)
        db.commit()
        db.refresh(locationPost)
        return locationPost
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    

def getBrigadesRepository(db: Session) -> list[BrigadeAndLocationsScheme]: 
    try: 
        brigades = db.query(BrigadeModel.idBrigade, BrigadeModel.referenceBrigade, BrigadeModel.startDate, BrigadeModel.endDate, LocationModel.idLocation, LocationModel.location).join(LocationModel, BrigadeModel.idBrigade == LocationModel.idBrigade).all()
        return brigades
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
    
def getBrigadeWithLocationsByIdRepository(id: int, db:Session) -> list[BrigadeAndLocationsScheme]: 
    try: 
        brigades = db.query(BrigadeModel.idBrigade, BrigadeModel.referenceBrigade, BrigadeModel.startDate, BrigadeModel.endDate, LocationModel.idLocation, LocationModel.location).join(LocationModel, BrigadeModel.idBrigade == LocationModel.idBrigade).filter(BrigadeModel.idBrigade==id).all()
        return brigades
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getBrigadeByIdRepository(id: int, db: Session) -> BrigadeFullScheme: 
    try: 
        brigade = db.query(BrigadeModel).filter(BrigadeModel.idBrigade == id).first()
        return brigade
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
def getLocationByIdRepository(id: int, db: Session) -> LocationScheme:
    try: 
        location = db.query(LocationModel).filter(LocationModel.idLocation == id).first()
        return location
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
def editBrigadeRepository(brigade: BrigadeFullScheme, db: Session) -> BrigadeFullScheme: 
    try: 
        db.commit()
        db.refresh(brigade)
        return brigade
    except Exception as e: 
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def editLocationRepository(location: LocationScheme, db: Session) -> LocationScheme: 
    try: 
        db.commit()
        db.refresh(location)
        return location
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))

def deleteBrigadeRepository(id: int, db: Session) -> bool: 
    try:
        brigadeToDelete = db.query(BrigadeModel).filter(BrigadeModel.idBrigade == id).first()
        if not brigadeToDelete:
            # No la encontró
            return False
        db.delete(brigadeToDelete)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise e

def deleteLocationRepository(id: int, db: Session) -> bool: 
    try: 
        locationToDelete = db.query(LocationModel).filter(LocationModel.idLocation).first()
        if not locationToDelete: 
            #No la encontró
            return False
        db.delete(locationToDelete)
        db.commit()
        return True
    except Exception as e: 
        db.rollback()
        raise e