from ..presentation import ServiciosEstado
from dms2021client.data.rest import AuthService

class CrearUsuariosEstado(ServiciosEstado):
    
    __session_id : str
    __auth_service : AuthService

    def __init__(self, session_id : str, auth_service: AuthService):
        self.__session_id = session_id
        self.__auth_service = auth_service

    def ejecutarPagina(self) -> int:
        '''
        Falta comprobar si el usuario tiene los permisos de creacion
        '''
        print('Creación de Usuarios')
        newSession = input('\tNombre de la nueva cuenta:\n')
        newPassword = input('\tContraseña de la nueva cuenta:\n')
        print('FALTA CODIGO')
        return 0