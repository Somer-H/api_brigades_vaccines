from sqlalchemy.orm import Session
from fastapi import HTTPException
from ...Domain.Scheme.brigadeScheme import BrigateRequestScheme, BrigateScheme, BrigateResponseWithLocationsScheme, LocationSchemeBase, BrigadeAndLocationsScheme, BrigadeUpdateScheme, BrigadeFullScheme, LocationScheme
from ...Infraestructure.Repositories.brigadeRepository import createBrigadeRepository, createLocationRepository, getBrigadesRepository, getBrigadeWithLocationsByIdRepository, editBrigadeRepository, getBrigadeByIdRepository, getLocationByIdRepository, editLocationRepository, deleteBrigadeRepository, deleteLocationRepository

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

def getBrigadesService(db: Session) -> list[BrigadeAndLocationsScheme]: 
    try: 
        brigades = getBrigadesRepository(db)
        if not brigades: 
            raise HTTPException(status_code=400, detail="No se ha encontrado nada")
        return brigades
    except Exception  as e:
        raise HTTPException(status_code=500, detail=str(e))

def getBrigadeWithLocationsByIdService(id: int, db: Session) -> list[BrigadeAndLocationsScheme]: 
    try: 
        brigade = getBrigadeWithLocationsByIdRepository(id, db)
        if not brigade: 
            raise HTTPException(status_code=400, detail="No se ha encontrado nada")
        return brigade
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))

def getBrigadeByIdService(id: int, db: Session) -> BrigadeFullScheme: 
    try: 
        brigade = getBrigadeByIdRepository(id, db)
        if not brigade: 
            raise HTTPException(status_code=400, detail="Brigada no encontrada")
        return brigade
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getLocationByIdService(id: int, db: Session) -> LocationScheme: 
    try: 
        location = getLocationByIdRepository(id, db)
        if not location: 
            raise HTTPException(status_code=400, detail="No se encontró la localización")
        return location
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
    
def editBrigadeService(id: int, brigade : BrigadeUpdateScheme, db: Session) -> BrigadeFullScheme: 
    try:
        brigadeToUpdate = getBrigadeByIdService(id, db)
        if brigade.referenceBrigade is not None: 
            brigadeToUpdate.referenceBrigade = brigade.referenceBrigade
        if brigade.startDate is not None:
            brigadeToUpdate.startDate = brigade.startDate
        if brigade.endDate is not None: 
            brigadeToUpdate.endDate = brigade.endDate
        updatedBrigade = editBrigadeRepository(brigadeToUpdate, db)
        if updatedBrigade:
            return updatedBrigade
        else: 
            raise HTTPException(status_code=400, detail="Vaya, ha ocurrido un error, intente de nuevo más tarde")
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))

def editLocationService(id: int, location: LocationSchemeBase, db: Session) -> LocationScheme: 
    try: 
        locationToEdit = getLocationByIdService(id, db)
        if location.location is not None: 
            locationToEdit.location = location.location
        updatadedLocation = editLocationRepository(locationToEdit, db)
        if updatadedLocation: 
            return updatadedLocation
        else: 
            raise HTTPException(status_code=400, detail="Ocurrió un error, por favor intentelo más tarde")
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))

def deleteBrigadeService(id: int, db: Session) -> str: 
    try: 
        if deleteBrigadeRepository(id, db) == False:
            raise HTTPException(status_code=500, detail="No se ha encontrado la brigada")
        return "Eliminado con éxito"
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))

def deleteLocationService(id: int, db: Session) -> str: 
    try: 
        if deleteLocationRepository(id, db) == False:
            raise HTTPException(status_code=500, detail="No se ha encontrado la localización")
        return "Eliminado con éxito"
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
    