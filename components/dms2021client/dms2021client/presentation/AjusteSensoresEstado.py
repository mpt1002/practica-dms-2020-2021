from ..presentation import ServiciosEstado
from dms2021client.data.rest import AuthService

class AjusteSensoresEstado():
    
    __session_id : str
    __username : str
    __auth_service : AuthService

    def __init__(self, session_id : str, username : str, auth_service: AuthService):
        self.__session_id = session_id
        self.__auth_service = auth_service
        self.__username = username

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