from Sensor import Sensor
import os

class SensorFile (Sensor):
    __file:str

    def __init__(self, file:str):
        self.__file = '../dms2021sensor/data/'+file

    def monitorizar(self):
        devuelto = os.system('find '+ self.file)
        if devuelto == self.file:
            return 'Fichreo en el sistema'
        else:
            return 'El fichero buscado no esta en el sistema'