from ..presentation import ServiciosEstado
from dms2021client.data.rest import AuthService, SensorService

class GestionarSensoresEstado(ServiciosEstado):
    
    __session_id : str
    __username : str
    __auth_service : AuthService
    __sensor_service : SensorService

    def __init__(self, session_id : str, username: str, auth_service: AuthService, sensor_service: SensorService):
        self.__session_id = session_id
        self.__username  =username
        self.__auth_service = auth_service
        self.__sensor_service = sensor_service

    def ejecutarPagina(self) -> int:
        #Comprobar si el usuario tiene los permisos de gestion de sensores
        if self.__auth_service.hasRigth(self.__username, 'AdminSensors'):
            print('Tienes los permisos necesarios para gestionar los sensores')
        else:
            print('No tienes los permisos necesarios para gestionar los sensores')
        return 0