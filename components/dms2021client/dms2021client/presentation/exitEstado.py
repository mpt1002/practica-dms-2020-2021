from dms2021client.data.rest.exc import InvalidCredentialsError, UnauthorizedError
from dms2021client.data.rest import AuthService
from .serviciosEstado import ServiciosEstado

class ExitEstado(ServiciosEstado):

    __session_id : str
    __auth_service : AuthService

    def __init__(self, session_id : str, auth_service: AuthService):
        self.__session_id = session_id
        self.__auth_service = auth_service

    def ejecutarPagina(self) -> int:
        print('\033[1;33m'+'OPCIÓN 6: Saliendo ...'+'\033[0m')
        try:
            self.__auth_service.logout(self.__session_id)
            print('\033[1;32m')
            print('Logged out successfully.')
            print('\033[0m')
            return 7
        except UnauthorizedError:
            print('\033[1;31m')
            print('Wrong session id.')
            print('\033[0m')
        except Exception as ex:
            print(ex)
        return 0
