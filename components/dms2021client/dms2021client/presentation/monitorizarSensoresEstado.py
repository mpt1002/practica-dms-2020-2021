from .serviciosEstado import ServiciosEstado
from dms2021client.data.rest import SensorService, AuthService

class MonitorizarSensoresEstado(ServiciosEstado):

    def __init__(self, username : str, auth_service: AuthService, sensorservice : SensorService):
        self.__username : str = username
        self.__sensor_service :SensorService = sensorservice
        self.__auth_service : AuthService = auth_service

    def ejecutarPagina(self) -> int:
        print('Valores de monitorizacion de cada sensor')
        if self.__auth_service.hasRigth(self.__username, 'ViewReports'):
            if self.__sensor_service.is_running():
                devuelto : str = "Sensores:\n"
                response_data = self.__sensor_service.get_all_values()
                for sensor in response_data:
                    devuelto = devuelto + '\t'+str(sensor) + ":\n"
                    devuelto = devuelto + "\t" + str(response_data[sensor]) + "\n"
                print(devuelto)
            else:
                print("ERROR: No se ha podido establecer contacto con el servicio sensor")
        else:
            print('No tienes los permisos para obtener los valores de monitorización')
        return 0