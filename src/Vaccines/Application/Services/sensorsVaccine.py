from sqlalchemy.orm import Session
from fastapi import HTTPException
from ...Infraestructure.Repositories.sensorsVaccine import createSensorsVaccineRepository, getSensorsVaccineRepository, getTemperatureSensorRepository
from ...Domain.Scheme.sensorsVaccine import SensorsVaccine, SensorsVaccineBase, GaussPoint, GraficResponse, TemperatureInput
from math import sqrt, pi, exp
import numpy as np
import statistics
from concurrent.futures import ThreadPoolExecutor
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


def pointInGaussCurveService(point: TemperatureInput, db: Session) -> GraficResponse: 
    try:
        sensors = getTemperatureSensorRepository(db)
        if not sensors:
            raise HTTPException(status_code=400, detail="No se ha encontrado nada")
        temperatures = [sensor.information for sensor in sensors]
        if not temperatures:
            raise HTTPException(status_code=400, detail="No hay datos de temperatura")

        def compute_stats():
            mean = np.mean(temperatures)
            standarDeviation = np.std(temperatures)
            median = statistics.median(temperatures)
            mode = statistics.mode(temperatures)
            range_ = max(temperatures) - min(temperatures)
            variance = statistics.variance(temperatures)
            steps = 150
            x_min = mean - 3 * standarDeviation
            x_max = mean + 3 * standarDeviation
            x_vals = np.linspace(x_min, x_max, steps)
            points = []
            for x in x_vals:
                y = (1 / (standarDeviation * sqrt(2 * pi))) * exp(-0.5 * ((x - mean) / standarDeviation) ** 2)
                points.append(GaussPoint(x=round(x, 2), y=round(y, 6)))
            x = point.value
            y = (1 / (standarDeviation * sqrt(2 * pi))) * exp(-0.5 * ((x - mean) / standarDeviation) ** 2)
            input_point = GaussPoint(x=round(x, 2), y=round(y, 6))
            return GraficResponse(
                mean=mean,
                standarDeviation=standarDeviation,
                median=median,
                mode=mode,
                range=range_,
                variance=variance,
                points=points,
                inputPoint=input_point
            )

        with ThreadPoolExecutor() as executor:
            future = executor.submit(compute_stats)
            return future.result()
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

        def compute_stats():
            mean = np.mean(temperatures)
            standarDeviation = np.std(temperatures)
            median = statistics.median(temperatures)
            mode = statistics.mode(temperatures)
            range_ = max(temperatures) - min(temperatures)
            variance = statistics.variance(temperatures)
            steps = 150
            x_min = mean - 3 * standarDeviation
            x_max = mean + 3 * standarDeviation
            x_vals = np.linspace(x_min, x_max, steps)
            points = []
            for x in x_vals:
                y = (1 / (standarDeviation * sqrt(2 * pi))) * exp(-0.5 * ((x - mean) / standarDeviation) ** 2)
                points.append(GaussPoint(x=round(x, 2), y=round(y, 6)))
            graficResponse = GraficResponse(
                mean=mean,
                standarDeviation=standarDeviation,
                median=median,
                mode=mode,
                range=range_,
                variance=variance,
                points=points
            )
            return graficResponse

        with ThreadPoolExecutor() as executor:
            future = executor.submit(compute_stats)
            return future.result()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))