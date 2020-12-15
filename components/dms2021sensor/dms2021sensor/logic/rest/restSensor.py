import json
from dms2021core.data.rest import RestResponse
from dms2021sensor.data import Sensor, SensorFile

class RestSensor():
    __sensores : dict
    __tipo_sensores:dict

    def __init__(self, tipoSensores: dict):
        self.__sensores['sensor1'] = SensorFile('ficheroABuscar.txt')
        self.__tipo_sensores = tipoSensores

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
        res_content_json = json.dumps(self.__sensores)
        return RestResponse(res_content_json, 200, mime_type='application/json')

    def obtenerTodosSensores(self) -> RestResponse:
        devuelto: str = self.__sensores.keys()
        if devuelto == '[]':
            return RestResponse('No sensors', 404, 'text/plain')
        else:
            return RestResponse(devuelto, 200, 'text/plain')

    def get_posibles_tipos(self)->RestResponse:
        res_content_json = json.dumps(self.__tipo_sensores)
        return RestResponse(res_content_json, 200, mime_type='application/json')

