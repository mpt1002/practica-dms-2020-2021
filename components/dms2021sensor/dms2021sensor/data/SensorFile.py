from .Sensor import Sensor
import os

class SensorFile (Sensor):
    __file:str

    def __init__(self, file:str):
        self.__file = file

    def monitorizar(self):
        encontrado : bool =  False
        for root, _, files in os.walk('/'):
            if self.__file in files:
                encontrado = True
                break

        if encontrado:
            return '\t--> Fichero '+str(self.__file)+' se ha encontrado.\n'
        else:
            return '\t--> Fichero '+str(self.__file)+' NO se ha encontrado.\n'