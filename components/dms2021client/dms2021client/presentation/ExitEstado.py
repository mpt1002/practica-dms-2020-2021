from dms2021client.data.rest.exc import InvalidCredentialsError, UnauthorizedError
from ..presentation import ServiciosEstado, ManejadorPagina

class ExitEstado(ServiciosEstado):

    # Referncia a la clase contexto
    __manejador : ManejadorPagina

    def __init__(self, manejador: ManejadorPagina):
        self.__manejador = manejador

    def ejecutarPagina(self):
        pass

    def logout(self):

        try:
            self.__manejador.get_auth_service().logout(self.__manejador.get_session_id())
            print('Logged out successfully.')
        except UnauthorizedError:
            print('Wrong session id.')
        except Exception as ex:
            print(ex)