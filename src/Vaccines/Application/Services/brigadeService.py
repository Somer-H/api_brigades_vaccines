from sqlalchemy.orm import Session
from fastapi import HTTPException
from ...Domain.Scheme.brigadeScheme import BrigateRequestScheme, BrigateScheme, BrigateResponseWithLocationsScheme, LocationScheme, LocationSchemeBase
from ...Infraestructure.Repositories.brigadeRepository import createBrigadeRepository, createLocationRepository

def createBrigadeService(brigade: BrigateRequestScheme, db: Session) -> BrigateResponseWithLocationsScheme:
    try: 
        brigadeToPost = BrigateScheme(
            referenceBrigade = brigade.referenceBrigade, 
            startDate= brigade.startDate, 
            endDate= brigade.endDate
        )
        brigateResponse=createBrigadeRepository(brigadeToPost, db)
        
        for locationIn in brigade.locations:
            locationToPost = LocationSchemeBase(
                idBrigade=brigateResponse.idBrigade, 
                location=locationIn
            )
            createLocationRepository(locationToPost, db)
        brigateAndLocationsResponse = BrigateResponseWithLocationsScheme(
            idBrigade=brigateResponse.idBrigade, 
            referenceBrigade=brigateResponse.referenceBrigade, 
            startDate=brigateResponse.startDate, 
            endDate=brigateResponse.endDate, 
            locations=brigade.locations
        )
        print(brigateAndLocationsResponse)
        return brigateAndLocationsResponse
    except Exception as e: 
       raise HTTPException(status_code=500, detail=str(e))