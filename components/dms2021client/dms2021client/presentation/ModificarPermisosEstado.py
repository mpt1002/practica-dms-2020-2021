from ..presentation import ServiciosEstado
from dms2021client.data.rest import AuthService

class ModificarPermisosEstado(ServiciosEstado):
    __session_id : str
    __username : str
    __auth_service : AuthService


    def __init__(self, session_id : str, username: str, auth_service: AuthService):
        self.__session_id = session_id
        self.__username = username
        self.__auth_service = auth_service

    def ejecutarPagina(self) -> int:
        #Comprobar si el usuario tiene los permisos de modificacion
        if self.__auth_service.hasRigth(self.__username , 'AdminRights'):
            print('Modificación de permisos')
            print('¿A què usuario desea modificarle los permisos?')
            user : str = input('Introduzca el nombre del usuario:\n')
            decision = 0
            while True:
                print('1. Añadir permisos')
                print('2. Revocar permisos')
                decision = input()
                if decision == '1' or decision == '2':
                    print('ENTRO')
                    break
            if decision == 1:
                self.annadirPermiso(user)
            else:
                self.revocarPermiso(user)

        else:
            print('No tienes los permisos necesarios para modificar permisos')
        return 0

    def annadirPermiso(self, user : str):
        print('¿Qué permiso desea añadir?')
        permiso: str = input()
        self.__auth_service.giveRight(user, permiso, self.__session_id)

    def revocarPermiso(self, user: str):
        print('¿Qué permiso desea añadir?')
        permiso: str = input()
        self.__auth_service.revokeRight(user, permiso, self.__session_id)