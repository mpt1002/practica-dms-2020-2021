from ..presentation import ServiciosEstado
from dms2021client.data.rest import AuthService

class AjusteSensoresEstado():
    
    __session_id : str
    __auth_service : AuthService

    def __init__(self, session_id : str, auth_service: AuthService):
        self.__session_id = session_id
        self.__auth_service = auth_service

    def ejecutarPagina(self) -> int:
        '''Asegurarse de que el usuario tiene permisos de ajuste de los sensores
        '''
        print('Modificar las reglas de monitorización de los sensores')
        print('FALTA CODIGO')
        return 0