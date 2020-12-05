from dms2021client.data.rest.exc import InvalidCredentialsError, UnauthorizedError
from dms2021client.data.rest import AuthService
from ..presentation import ServiciosEstado

class ExitEstado(ServiciosEstado):

    __session_id : str
    __auth_service : AuthService

    def __init__(self, session_id : str, auth_service: AuthService):
        self.__session_id = session_id
        self.__auth_service = auth_service

    def ejecutarPagina(self) -> int:
        try:
            self.__auth_service.logout(self.__session_id)
            print('Logged out successfully.')
            return 7
        except UnauthorizedError:
            print('Wrong session id.')
        except Exception as ex:
            print(ex)
        return 0
