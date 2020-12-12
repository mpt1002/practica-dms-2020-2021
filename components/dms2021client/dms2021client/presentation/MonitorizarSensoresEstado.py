from ..presentation import ServiciosEstado
from dms2021client.data.rest import SensorService

class MonitorizarSensoresEstado(ServiciosEstado):
    __sensor_service : SensorService
    __session_id : str

    def __init__(self, session_id : str, sensorservice : SensorService):
        self.__session_id = session_id
        self.__sensor_service = sensorservice

    def ejecutarPagina(self) -> int:
        print('Valores de monitorizacion de cada sensor')
        if self.__sensor_service.is_running():
            print(str(self.__sensor_service.get_all_values()))
        else:
            print("ERROR: No se ha podido establecer contacto con el servicio sensor")
        return 0