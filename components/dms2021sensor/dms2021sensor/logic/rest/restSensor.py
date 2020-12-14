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

    def obtenerValoresTodosSensores(self) -> RestResponse:
        devuelto : str = "Sensores:\n"
        for sensor in self.__sensores:
            devuelto = devuelto + str(sensor) + ":\n"
            devuelto = devuelto + "\t" + str(self.__sensores[sensor].monitorizar()) + "\n"

        if devuelto == "Sensores:\n":
            return RestResponse('No se han encontrado sensores', 404, 'text/plain')
        return RestResponse(devuelto, 200, 'text/plain')

    def obtenerTodosSensores(self) -> RestResponse:
        devuelto: str = self.__sensores.keys()
        if devuelto == '[]':
            return RestResponse('No sensors', 404, 'text/plain')
        else:
            return RestResponse(devuelto, 200, 'text/plain')

