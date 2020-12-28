from .serviciosEstado import ServiciosEstado
from dms2021client.data.rest import AuthService, SensorService

class GestionarSensoresEstado(ServiciosEstado):
    
    __session_id : str
    __username : str
    __auth_service : AuthService
    __sensor_service : SensorService

    def __init__(self, session_id : str, username: str, auth_service: AuthService, sensor_service: SensorService):
        print('\033[1;33m'+'OPCIÓN 3: Añadir y eliminar sensores')
        self.__session_id = session_id
        self.__username  =username
        self.__auth_service = auth_service
        self.__sensor_service = sensor_service

    def ejecutarPagina(self) -> int:
        #Comprobar si el usuario tiene los permisos de gestion de sensores
        if self.__auth_service.hasRigth(self.__username, 'AdminSensors'):
            print('\033[1;32m'+'\tTienes los permisos necesarios para modificar las reglas de monitorización de los sensores'+'\033[0m')
            eleccion: int = 0
            while True:
                print('\033[1;33m')
                print('\tGestionar sensores')
                print('\t\t1. Añadir sensor')
                print('\t\t2. Eliminar sensor')
                eleccion = int(input('\tIntroduzca su elección: '))
                print('\033[0m')
                if eleccion == 1 or eleccion == 2:
                    break
            
            if eleccion == 1:
                self.__annadir_sensor()
            elif eleccion == 2:
                self.__eliminar_sensor()
        else:
            print('\033[1;31m' + 'No tienes los permisos necesarios para gestionar los sensores' + '\033[1;31m')
        return 0

    def __annadir_sensor(self):
        print('\033[1;33m')
        sensor_nuevo = input('\tIntroduca el nombre del nuevo sensor que desea crear: ')
        print('\033[0m')
        self.__crear_sensor(sensor_nuevo)

    def __eliminar_sensor(self):
        sensores = self.__sensor_service.get_all_values()
        print('\033[1;33m')
        print('\t¿Qué sensor desea eliminar?')
        for sensor in sensores:
            print('\t\t-> ' + str(sensor))
        sensor_eliminar: str = input('\t- Introduzca el nombre del sensor: ')
        print('\033[0m')
        self.__sensor_service.remove_sensor(sensor_eliminar)

    def __crear_sensor(self, sensorname: str):
        eleccion = 0
        tipo_sensores = self.__sensor_service.get_tipos_posibles()
        if tipo_sensores != {}:
            while True:
                print('\033[1;33m')
                print('\t¿Qué tipo de sensor quieres crear?')
                for tipo in tipo_sensores:
                    print('\t\t'+str(tipo_sensores[tipo]) + '. ' + str(tipo))
                eleccion = int(input('\tElija su opción: '))
                if eleccion > 0 and eleccion <= len(tipo_sensores):
                    break
                print('\033[0m')
            if eleccion == tipo_sensores['sensorFile']:
                self.__crear_sensor_de_ficheros(sensorname)
            elif eleccion == tipo_sensores['sensorSystem']:
                self.__crear_sensor_de_sistema(sensorname)
            else:
                print('\033[1;31m'+'\tOpción elegida no válida. Vuelve a intentarlo.'+'\033[0m')
                self.__crear_sensor(sensorname)
        else:
            print('\033[1;31m'+'Error obteniendo los tipos de los sensores del servicio sensor'+'\033[0m')

    def __crear_sensor_de_ficheros(self, sensor: str):
        print('\033[1;33m')
        print('\t¿Qué fichero desea monitorizar?')
        nombre_fichero = input('\t- Introduzca el nombre del fichero que desea buscar: ')
        self.__sensor_service.add_sensor(sensor, 'sensorFile', nombre_fichero)
        print('\033[0m')

    def __crear_sensor_de_sistema(self, sensor: str):
        print('\033[1;33m')
        while True:
            print('\t¿Qué desea monitorizar?')
            print('\t-> Mem')
            print('\t-> Swap')
            tipo_monitorización = input('\t- Introduzca su elección: ')
            if tipo_monitorización == 'Mem' or tipo_monitorización == 'Swap':
                break
        self.__sensor_service.add_sensor(sensor, 'sensorSystem', tipo_monitorización)
        print('\033[0m')