from ..presentation import ServiciosEstado
from dms2021client.data.rest import AuthService

class CrearUsuariosEstado(ServiciosEstado):
    
    __session_id : str
    __auth_service : AuthService

    def __init__(self, session_id : str, auth_service: AuthService):
        self.__session_id = session_id
        self.__auth_service = auth_service

    def ejecutarPagina(self) -> int:
        #Comprobar si el usuario tiene los permisos de creacion
        if self.__auth_service.hasRigth(self.__session_id, 'AdminUsers'):
            print('Creación de Usuarios')
            newSession: str = input('\tNombre de la nueva cuenta:\n')
            newPassword: str = input('\tContraseña de la nueva cuenta:\n')
            self.__auth_service.createUser(newSession, newPassword)
        else:
            print('No tienes los permisos necesarios para crear usuarios')
        return 0