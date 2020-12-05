from ..presentation import ServiciosEstado
from dms2021client.data.rest import AuthService

class ModificarPermisosEstado(ServiciosEstado):
    __session_id : str
    __auth_service : AuthService

    def __init__(self, session_id : str, auth_service: AuthService):
        self.__session_id = session_id
        self.__auth_service = auth_service

    def ejecutarPagina(self) -> int:
        '''
        Falta comprobar si el usuario tiene los permisos de modificacion
        '''
        print('Modificación de permisos')
        print('¿A què usuario desea modificarle los permisos?')
        user = input('Introduzca el nombre del usuario:\n')
        print('FALTA CODIGO')
        return 0