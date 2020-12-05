from ..presentation import ServiciosEstado
from dms2021client.data.rest import AuthService

class GestionPermisosEstado(ServiciosEstado):
    
    __session_id : str
    __auth_service : AuthService

    def __init__(self, session_id : str, auth_service: AuthService):
        self.__session_id = session_id
        self.__auth_service = auth_service

    def ejecutarPagina(self) -> int:
        print('Gestion de Permisos')
        print('FALTA CODIGO')
        return 0