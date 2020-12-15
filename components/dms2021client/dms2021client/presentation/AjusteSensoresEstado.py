from ..presentation import ServiciosEstado
from dms2021client.data.rest import AuthService, SensorService

class AjusteSensoresEstado():
    
    __session_id : str
    __username : str
    __auth_service : AuthService
    __sensor_service : SensorService

    def __init__(self, session_id : str, username : str, auth_service: AuthService, sensor_service : SensorService):
        self.__session_id = session_id
        self.__auth_service = auth_service
        self.__username = username
        self.__sensor_service = sensor_service

    def ejecutarPagina(self) -> int:
        '''Asegurarse de que el usuario tiene permisos de ajuste de los sensores
        '''
        print('Modificar las reglas de monitorización de los sensores')
        print('FALTA CODIGO')
        #Comprobar si el usuario tiene los permisos de gestion de sensores
        if self.__auth_service.hasRigth(self.__username, 'AdminRules'):
            print('Tienes los permisos necesarios para modificar las reglas de monitorización de los sensores')
            sensores = self.__sensor_service.get_all_values()
            print('¿A que sensor desea cambiarle los ajustes?')
            for sensor in sensores:
                print('\t->' + str(sensor))
            sensor_cambio: str = input('Introduzca el nombre del sensor\n')
            if sensor_cambio in sensores:
                self.__cambiar_ajustes_sensor(sensor_cambio)
            else:
                print('Ese sensor no existe')
        else:
            print('No tienes los permisos necesarios para modificar las reglas de monitorización de los sensores')
        return 0

    def __cambiar_ajustes_sensor(self, sensor : str):
        eleccion = 0
        tipo_sensores = self.__sensor_service.get_tipos_posibles()
        if tipo_sensores != {}:
            while True:
                print('¿Qué tipo de sensor quieres que sea ahora ' + str(sensor))
                for tipo in tipo_sensores:
                    print(str(tipo_sensores[tipo]) + '. ' + str(tipo))
                eleccion = int(input('Elija su opción\n'))
                if eleccion > 0 and eleccion <= len(tipo_sensores):
                    break
            if eleccion ==1:
                self.ajustar_sensor_de_ficheros(sensor)
            else:
                print('Un error inesperado ha ocurrido, vuelva a intentarlo')
        else:
            print('Error obteniendo los tipos de los sensores del servicio sensor')

    def ajustar_sensor_de_ficheros(self, sensor):
        print('¿Què fichero desea monitorizar?')
        nombre_fichero = input('Introduzca la ruta absoluta')
        