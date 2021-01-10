import json
from dms2021core.data.rest import RestResponse
from dms2021sensor.data import Sensor, SensorFile, SensorSystem
from dms2021sensor.data.db.tables import Sensors
from dms2021sensor.logic.db import SensorManager, SensorTypeManager
from dms2021sensor.data.db import Schema
from dms2021sensor.data.config import SensorConfiguration

class RestSensor():

    def __init__(self):
        cfg: SensorConfiguration = SensorConfiguration()
        cfg.load_from_file(cfg.default_config_file())
        self.__schema = Schema(cfg)
        self.__sensor_manager = SensorManager(self.__schema)
        self.__sensores: dict = self.__obtener_sensores()
        self.__sensor_type_manager = SensorTypeManager(self.__schema)
        self.__tipo_sensores: dict = self.__obtener_tipo_sensores()

    def __obtener_sensores(self) -> dict:
        '''Debido a que en el resto de servicios se trabaja con diccionarios para los sensores
         se van a convertir ahora a diccionario'''

        sensores = self.__sensor_manager.get_all_sensor()
        dict_sensores: dict = {}

        for sensor in sensores:
            if sensor.sensor_type == 'sensorFile':
                dict_sensores[sensor.sensor_name] = SensorFile(sensor.parameters)
            elif sensor.sensor_type == 'sensorSystem':
                dict_sensores[sensor.sensor_name] = SensorSystem(sensor.parameters)
        return dict_sensores

    def __obtener_tipo_sensores(self)-> dict:
        '''Debido a que en el resto de servicios se trabaja con diccionarios para los tipos
        de sensores se van a convertir ahora a diccionario'''
        
        tipo_sensores = self.__sensor_type_manager.get_all_sensortypes()
        dict_tipo_sensores: dict = {}

        i: int = 1
        for tipo in tipo_sensores:
            dict_tipo_sensores[tipo.sensor_type] = i
            i+=1
        return dict_tipo_sensores

    def obtenerRespuestaSensor(self, nombreSensor:str) -> RestResponse:
        keys = self.__sensores.keys()
        flag = False
        for s in keys:
            if nombreSensor == s:
                flag = True
                break

        if flag:
            valor_sensor = str(self.__sensores[nombreSensor].monitorizar())
            return RestResponse(valor_sensor, 200, 'text/plain')
        else:
            #Si no existe el sensor ERROR 404
            return RestResponse(code = 404, mime_type = 'text/plain')

    def obtenerValoresTodosSensores(self) -> RestResponse:
        res_sensors = {}
        for sensor in self.__sensores:
            res_sensors[sensor] = self.__sensores[sensor].monitorizar()
        res_content_json = json.dumps(res_sensors)
        return RestResponse(res_content_json, 200, mime_type='application/json')

    def obtenerTodosSensores(self) -> RestResponse:
        devuelto = self.__sensores.keys()
        if devuelto == []:
            return RestResponse('No sensors', 404, 'text/plain')
        else:
            res_content_json = json.dumps(devuelto)
            return RestResponse(res_content_json, 200, 'text/plain')

    def get_posibles_tipos(self)->RestResponse:
        print(self.__tipo_sensores)
        res_content_json = json.dumps(self.__tipo_sensores)
        return RestResponse(res_content_json, 200, mime_type='application/json')

    def set_sensor(self, sensorName: str, sensorType : str, parameters = "")-> RestResponse:
        '''Devido a las caracteristicas de los doccionarios de python sirve tanto para crear como para modificar sensores'''
        if sensorType not in self.__tipo_sensores or sensorName not in self.__sensores:
            return RestResponse('Not found', 404, 'text/plain')
        else:
            if sensorType == 'sensorFile':
                self.__sensores[sensorName] = SensorFile(parameters)
                return RestResponse('OK', 200, 'text/plain')
            elif sensorType == 'sensorSystem':
                self.__sensores[sensorName] = SensorSystem(parameters)
                return RestResponse('OK', 200, 'text/plain')
            else:
                return RestResponse('BAD ARGUMENTS', 400, 'text/plain')

    def remove_sensor(self, sensorName: str) -> RestResponse:
        self.__sensores.pop(sensorName)
        return RestResponse('OK', 200, 'text/plain')

    def add_sensor(self, sensorName: str, sensorType: str, parameters = "") -> RestResponse:
        if sensorType not in self.__tipo_sensores or sensorName in self.__sensores:
            return RestResponse('Not found', 404, 'text/plain')
        else:
            if sensorType == 'sensorFile':
                self.__sensores[sensorName] = SensorFile(parameters)
                return RestResponse('OK', 200, 'text/plain')
            elif sensorType == 'sensorSystem':
                self.__sensores[sensorName] = SensorSystem(parameters)
                return RestResponse('OK', 200, 'text/plain')
            else:
                return RestResponse('BAD ARGUMENTS', 400, 'text/plain')

