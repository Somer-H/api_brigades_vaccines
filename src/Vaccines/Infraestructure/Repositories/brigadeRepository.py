from ...Infraestructure.Models.brigadeModel import BrigadeModel, LocationModel
from ...Domain.Scheme.brigadeScheme import BrigateScheme, BrigateResponseScheme, LocationScheme, LocationSchemeBase, BrigadeAndLocationsScheme
from sqlalchemy.orm import Session
from fastapi import HTTPException
def createBrigadeRepository(brigate: BrigateScheme, db: Session) -> BrigateResponseScheme: 
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