from dms2021core.data.rest import RestResponse
from dms2021sensor.data import Sensor, SensorFile

class RestSensor():
    __sensores : {}

    def __init__(self):
        self.__sensores['sensor1'] = SensorFile('FicheroABuscar.txt')

    def obtenerRespuestaSensor(self, nombreSensor:str) -> RestResponse:
        if nombreSensor in self.__sensores:
            valorSensor = str(self.__sensores[nombreSensor].monitorizar())
            RestResponse(valorSensor, 200, 'text/plain')
            return RestResponse
        else:
            #Si no existe el sensor ERROR 404
            return RestResponse(code = 404, mime_type = 'text/plain')

