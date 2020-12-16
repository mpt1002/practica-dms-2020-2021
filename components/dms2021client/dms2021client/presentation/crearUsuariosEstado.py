from .serviciosEstado import ServiciosEstado
from dms2021client.data.rest import AuthService
from dms2021core.data import UserRightName

class CrearUsuariosEstado(ServiciosEstado):
    
    __session_id : str
    __username : str
    __auth_service : AuthService
    
    def __init__(self, session_id : str, username: str, auth_service: AuthService):
        self.__session_id = session_id
        self.__username = username
        self.__auth_service = auth_service

    def ejecutarPagina(self) -> int:
        
        #Comprobar si el usuario tiene los permisos de creacion
        if self.__auth_service.hasRigth(self.__username, 'AdminUsers'):
            print('\033[1;33m'+'OPCIÓN 1: Crear usuarios')
            newSession: str = input('\t- Nombre del nuevo usuario: ')
            newPassword: str = input('\t- Contraseña para el nuevo usuario: ')
            print('\033[0m')
            self.__auth_service.createUser(newSession, newPassword, self.__session_id)
        else:
            print('\033[1;31m')
            print('No tienes los permisos necesarios para crear usuarios')
            print('\033[0m')
        return 0