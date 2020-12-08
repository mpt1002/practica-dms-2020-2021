from dms2021core.data.rest import RestResponse
from dms2021sensor.data import Sensor, SensorFile

class RestSensor():
    __sensores = {}

    def __init__(self):
        self.__sensores['sensor1'] = SensorFile('ficheroABuscar.txt')

    def obtenerRespuestaSensor(self, nombreSensor:str) -> RestResponse:
        keys = self.__sensores.keys()
        flag = False
        for s in keys:
            if nombreSensor == s:
                flag = True
                break

        if flag:
            valorSensor = str(self.__sensores[nombreSensor].monitorizar())
            return RestResponse(valorSensor, 200, 'text/plain')
        else:
            #Si no existe el sensor ERROR 404
            return RestResponse(code = 404, mime_type = 'text/plain')

