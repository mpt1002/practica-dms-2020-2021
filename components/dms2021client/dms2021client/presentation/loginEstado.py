import time
from getpass import getpass
from .serviciosEstado import ServiciosEstado
from dms2021client.data.rest import AuthService
from dms2021client.data.rest.exc import InvalidCredentialsError

class LoginEstado(ServiciosEstado):

    def __init__(self, auth_service: AuthService):
        self.__auth_service = auth_service
        self.__session_id: str = ''
        self.__username: str = ''

    def ejecutarPagina(self) -> int:
        print('Estableciendo contacto con el servidor, por favor espere...')
        while not self.__auth_service.is_running():
            time.sleep(1)
        print('Contacto establecido')

        try:
            self.__pedir_credenciales()
            return 0
        except InvalidCredentialsError:
            print('\033[1;31m')
            print('\tWrong username and/or password. Try again.')
            print('\033[0m')
            self.__pedir_credenciales()
        except Exception as ex:
            print(ex)
        return 0

    def get_session_id(self):
        return self.__session_id

    def get_username(self):
        return self.__username

    def __pedir_credenciales(self):
        print('\033[1;33m'+'LOGIN')
        username: str = input('\t- Username: ')
        password: str = getpass('\t- Password: ')
        print('\033[0m')

        self.__session_id = self.__auth_service.login(username, password)
        self.__username = username
        print('\033[1;32m')
        print('\tLogged in successfully as ' + username + ' . Session id: ' + self.__session_id)
        print('\033[0m')
