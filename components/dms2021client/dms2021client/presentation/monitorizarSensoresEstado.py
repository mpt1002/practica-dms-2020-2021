from .serviciosEstado import ServiciosEstado
from dms2021client.data.rest import SensorService, AuthService

class MonitorizarSensoresEstado(ServiciosEstado):

    def __init__(self, username : str, auth_service: AuthService, sensorservice : SensorService):
        self.__username : str = username
        self.__sensor_service :SensorService = sensorservice
        self.__auth_service : AuthService = auth_service

    def ejecutarPagina(self) -> int:
        print('\033[1;33m'+'OPCIÓN 5: Obtener los valores de monitorización del sensor')
        if self.__auth_service.hasRigth(self.__username, 'ViewReports'):
            if self.__sensor_service.is_running():
                devuelto : str = "\t- Sensores:\n"
                response_data = self.__sensor_service.get_all_values()
                for sensor in response_data:
                    devuelto = devuelto + '\t\t- '+str(sensor) + ":\n"
                    devuelto = devuelto + "\t\t" + str(response_data[sensor]) + "\n"
                print(devuelto)
                print('\033[0m')
            else:
                print('\033[1;31m')
                print("ERROR: No se ha podido establecer contacto con el servicio sensor")
                print('\033[0m')
        else:
            print('\033[1;31m')
            print('No tienes los permisos para obtener los valores de monitorización')
            print('\033[0m')
        return 0