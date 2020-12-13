#!/usr/bin/env python3

import time
from getpass import getpass
from dms2021client.data.config import ClientConfiguration
from dms2021client.data.rest import AuthService, SensorService
from dms2021client.data.rest.exc import InvalidCredentialsError, UnauthorizedError
from ..presentation import ServiciosEstado, MenuEstado, ExitEstado, CrearUsuariosEstado, ModificarPermisosEstado, GestionPermisosEstado, AjusteSensoresEstado, MonitorizarSensoresEstado

class ManejadorPagina:

    __estado : ServiciosEstado
    __opcion : int
    __session_id: str
    __username : str
    __cfg: ClientConfiguration
    __auth_service: AuthService
    __sensor_service : SensorService

    def __init__(self):
        print('ESTOY EN MANEJADOR PAGINA')
        self.__cfg = ClientConfiguration()
        self.__cfg.load_from_file(self.__cfg.default_config_file())
        self.__auth_service = AuthService(self.__cfg.get_auth_service_host(), self.__cfg.get_auth_service_port())
        self.__session_id, self.__username = self.login()
        print('HE VUELTO DEL LOGIN')
        
        # Ir al estado inicial
        self.__estado = MenuEstado(self.__session_id)
        
        opcion = 0
        while True:
            opcion = self.__estado.ejecutarPagina()
            if opcion == 0:
                self.__estado = MenuEstado(self.__session_id)
            elif opcion == 1:
                self.__estado = CrearUsuariosEstado(self.__session_id, self.__username, self.__auth_service)
            elif opcion == 2:
                self.__estado = ModificarPermisosEstado(self.__session_id, self.__username, self.__auth_service)
            elif opcion == 3:
                self.__estado = GestionPermisosEstado(self.__session_id, self.__auth_service)
            elif opcion == 4:
                self.__estado = AjusteSensoresEstado(self.__session_id, self.__auth_service)
            elif opcion == 5:
                self.__sensor_service = self.__get_sensor_service()
                self.__estado = MonitorizarSensoresEstado(self.__session_id, self.__sensor_service)
            elif opcion == 6:
                self.__estado = ExitEstado(self.__session_id, self.__auth_service)
            elif opcion == 7:
                #La opcion 7 solo saltara si se ha hecho el correcto logout
                break
                                
    # Obtener el estado actual
    def get_Estado(self) -> ServiciosEstado:
        return self.__estado
    
    # Asignar un nuevo estado
    def set_Estado(self, estado):
        self.__estado = estado
    
    # Obtener la session id
    def get_session_id(self) -> str:
        return self.__session_id
    
    # Obtener la opcion actual
    def get_opcion(self) -> int:
        return self.__opcion

    # Asignar una nueva opcion
    def set_opcion(self, opcion: int) -> int:
        self.__opcion = opcion

    # Obtener la configuracion del cliente actual
    def get_cfg(self) -> ClientConfiguration:
        return self.__cfg
    
    # Obtener la autentificacion del servicio actual
    def get_auth_service(self) -> AuthService:
        return self.__auth_service

    def login(self) -> str:
        print('ESTOY EN LOGIN')
        while not self.__auth_service.is_running():
            time.sleep(1)
        print('\nAuthentication service up!')
        
        
        print('Press Ctrl+C to end this process.')
        print('If run as a docker container, press Ctrl+P,Ctrl+Q to detach from the container.')
        username: str = input('Username: ')
        password: str = getpass('Password: ')
        try:
            self.__session_id = self.__auth_service.login(username, password)
            self.__username = username
            print('Logged in successfully as ' + username + ' . Session id: ' + self.__session_id)
        except InvalidCredentialsError:
            print('Wrong username and/or password. Try again.')
        except Exception as ex:
            print(ex)

        return self.__session_id, self.__username

    def __get_sensor_service(self) -> SensorService:
        opcion:int = 0
        while True:
            print('¿Qué sensor desea monitorizar?')
            print('\t1. Sensor 1')
            print('\t2. Sensor 2')
            opcion = int(input('Elija un sensor'))
            if opcion == 1:
                return SensorService(self.__cfg.get_sensor1_service_host(), self.__cfg.get_sensor1_service_port())
            elif opcion == 2:
                return SensorService(self.__cfg.get_sensor2_service_host(), self.__cfg.get_sensor2_service_port())