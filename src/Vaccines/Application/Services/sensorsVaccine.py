from sqlalchemy.orm import Session
from fastapi import HTTPException
from ...Infraestructure.Repositories.sensorsVaccine import createSensorsVaccineRepository, getSensorsVaccineRepository, getTemperatureSensorRepository
from ...Domain.Scheme.sensorsVaccine import SensorsVaccine, SensorsVaccineBase, GaussPoint, GraficResponse
from math import sqrt, pi, exp
import numpy as np
import statistics
def createSensorsVaccineService(sensorsVaccine: SensorsVaccineBase, db: Session) -> SensorsVaccine:
    try: 
        return createSensorsVaccineRepository(sensorsVaccine, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def getSensorsVaccineService(db: Session) -> list[SensorsVaccine]:
    try: 
        sensorsGet = getSensorsVaccineRepository(db)
        if not sensorsGet:
            raise HTTPException(status_code=404, detail="No se encontraron Sensores de vacunas")
        return sensorsGet
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def sendToGuassCurveService(db: Session) -> GraficResponse:
    try: 
        sensors = getTemperatureSensorRepository(db)
        if not sensors: 
            raise HTTPException(status_code=400, detail="No se ha encontrado nada")
        
        temperatures = [sensor.information for sensor in sensors]
        if not temperatures:
           raise HTTPException(status_code=400, detail="No hay datos de temperatura")

        # Calcular media y desviación estándar, además de otras medidas
        mean = np.mean(temperatures)
        standarDeviation = np.std(temperatures)
        median = statistics.median(temperatures)
        mode = statistics.mode(temperatures)
        range = max(temperatures) - min(temperatures)
        variance = statistics.variance(temperatures)
        # Puntos para la curva de Gauss
        steps = 150  # cantidad de puntos en la curva
        x_min = mean - 3 * standarDeviation
        x_max = mean + 3 * standarDeviation
        x_vals = np.linspace(x_min, x_max, steps)
    
        points = []
        for x in x_vals:
          y = (1 / (standarDeviation * sqrt(2 * pi))) * exp(-0.5 * ((x - mean) / standarDeviation) ** 2)
          points.append(GaussPoint(x=round(x, 2), y=round(y, 6)))
        graficResponse = GraficResponse(
            mean= mean, 
            standarDeviation=standarDeviation,
            median=median,
            mode=mode, 
            range=range, 
            variance=variance,
            points=points
        )
        return graficResponse
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))