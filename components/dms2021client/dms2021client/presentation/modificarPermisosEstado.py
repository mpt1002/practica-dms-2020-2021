from .serviciosEstado import ServiciosEstado
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
            print('\033[1;33m'+'OPCIÓN 2: Modificar Permisos')
            print('\t- ¿A qué usuario desea modificarle los permisos?')
            user : str = input('\t- Introduzca el nombre del usuario: ')
            decision = 0
            while True:
                print('\t¿Qué acción desea realizar?')
                print('\t\t1. Añadir permisos')
                print('\t\t2. Revocar permisos')
                decision = int(input('\t\t- Introduzca una opción: '))
                if decision == 1 or decision == 2:
                    break
                else: 
                    print('\033[1;31m')
                    print('\tOpción elegida no disponible. Vuelve a intentarlo.')
                    print('\033[0m')
            print('\033[0m')
            if decision == 1:
                self.annadirPermiso(user)
            elif decision == 2:
                self.revocarPermiso(user)

        else:
            print('\033[1;31m')
            print('No tienes los permisos necesarios para modificar permisos')
            print('\033[0m')
        return 0

    def annadirPermiso(self, user : str):
        print('\033[1;33m')
        print('\t\t¿Qué permiso desea añadir?')
        print('\t\t\t- Posibles permisos: AdminUsers, AdminRights, AdminSensors, AdminRules, ViewReports')
        permiso: str = input('\t\t\t- Introduce el permiso: ')
        print('\033[0m')
        self.__auth_service.giveRight(user, permiso, self.__session_id)

    def revocarPermiso(self, user: str):
        print('\033[1;33m')
        print('\t\t¿Qué permiso desea revocar?')
        print('\t\t\t- Posibles permisos: AdminUsers, AdminRights, AdminSensors, AdminRules, ViewReports')
        permiso: str = input('\t\t\t- Introduce el permiso: ')
        print('\033[0m')
        self.__auth_service.revokeRight(user, permiso, self.__session_id)