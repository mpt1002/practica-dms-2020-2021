from ..presentation import ServiciosEstado
from dms2021client.data.rest import AuthService, SensorService

class AjusteSensoresEstado():
    
    __session_id : str
    __username : str
    __auth_service : AuthService
    __sensor_service : SensorService

    def __init__(self, session_id : str, username : str, auth_service: AuthService, sensor_service : SensorService):
        self.__session_id = session_id
        self.__auth_service = auth_service
        self.__username = username
        self.__sensor_service = sensor_service

    def ejecutarPagina(self) -> int:
        '''Asegurarse de que el usuario tiene permisos de ajuste de los sensores
        '''
        print('Modificar las reglas de monitorización de los sensores')
        print('FALTA CODIGO')
        #Comprobar si el usuario tiene los permisos de gestion de sensores
        if self.__auth_service.hasRigth(self.__username, 'AdminRules'):
            print('Tienes los permisos necesarios para modificar las reglas de monitorización de los sensores')
        else:
            print('No tienes los permisos necesarios para modificar las reglas de monitorización de los sensores')
        return 0