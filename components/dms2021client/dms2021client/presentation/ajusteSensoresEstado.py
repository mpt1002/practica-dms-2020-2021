from .serviciosEstado import ServiciosEstado
from dms2021client.data.rest import AuthService, SensorService

class AjusteSensoresEstado(ServiciosEstado):
    
    def __init__(self, session_id : str, username : str, auth_service: AuthService, sensor_service : SensorService):
        self.__session_id: str = session_id
        self.__auth_service: AuthService = auth_service
        self.__username:str = username
        self.__sensor_service:SensorService = sensor_service

    def ejecutarPagina(self) -> int:
        '''Asegurarse de que el usuario tiene permisos de ajuste de los sensores
        '''
        print('\033[1;33m'+'OPCIÓN 4: Modificar las reglas de monitorización de cada sensor')
        print('\033[0m')
        #Comprobar si el usuario tiene los permisos de gestion de sensores
        if self.__auth_service.hasRigth(self.__username, 'AdminRules'):
            print('\033[1;32m'+'\tTienes los permisos necesarios para modificar las reglas de monitorización de los sensores'+'\033[0m')
            sensores = self.__sensor_service.get_all_values()
            print('\033[1;33m')
            print('\t¿A que sensor desea cambiarle los ajustes?')
            for sensor in sensores:
                print('\t\t-> ' + str(sensor))
            sensor_cambio: str = input('\t\t- Introduzca el nombre del sensor: ')
            print('\033[0m')
            if sensor_cambio in sensores:
                self.__cambiar_ajustes_sensor(sensor_cambio)
            else:
                print('\033[1;31m'+'Ese sensor no existe'+'\033[0m')
        else:
            print('\033[1;31m'+'No tienes los permisos necesarios para modificar las reglas de monitorización de los sensores'+'\033[0m')
        return 0

    def __cambiar_ajustes_sensor(self, sensor : str):
        eleccion = 0
        tipo_sensores = self.__sensor_service.get_tipos_posibles()
        if tipo_sensores != {}:
            while True:
                print('\033[1;33m')
                print('\t¿Qué tipo de sensor quieres que sea ahora ' + str(sensor)+' ?')
                for tipo in tipo_sensores:
                    print('\t\t'+str(tipo_sensores[tipo]) + '. ' + str(tipo))
                eleccion = int(input('\t\tElija su opción: '))
                if eleccion > 0 and eleccion <= len(tipo_sensores):
                    break
                print('\033[0m')
            if eleccion == tipo_sensores['sensorFile']:
                self.__ajustar_sensor_de_ficheros(sensor)
            elif eleccion == tipo_sensores['sensorSystem']:
                self.__ajustar_sensor_de_sistema(sensor)
            else:
                print('\033[1;31m'+'\tOpción elegida no válida. Vuelve a intentarlo.'+'\033[0m')
                self.__cambiar_ajustes_sensor(sensor)
        else:
            print('\033[1;31m'+'Error obteniendo los tipos de los sensores del servicio sensor'+'\033[0m')

    def __ajustar_sensor_de_ficheros(self, sensor: str):
        print('\033[1;33m')
        print('\t¿Qué fichero desea monitorizar?')
        nombre_fichero = input('\t\t- Introduzca el nombre del fichero que desea buscar: ')
        self.__sensor_service.set_sensor(sensor, 'sensorFile', nombre_fichero)
        print('\033[0m')

    def __ajustar_sensor_de_sistema(self, sensor: str):
        print('\033[1;33m')
        while True:
            print('\t¿Qué desea monitorizar?')
            print('\t-> Mem')
            print('\t-> Swap')
            tipo_monitorización = input('\t\t- Introduzca su elección: ')
            if tipo_monitorización == 'Mem' or tipo_monitorización == 'Swap':
                break
        self.__sensor_service.set_sensor(sensor, 'sensorSystem', tipo_monitorización)
        print('\033[0m')
        