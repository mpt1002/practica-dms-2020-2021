from .Sensor import Sensor
import os

class SensorFile (Sensor):
    __file:str

    def __init__(self, file:str):
        self.__file = file

    def monitorizar(self):
        #devuelto : str = os.system("find "+ self.__file)
        pwd : str = os.system("pwd")
        print(pwd)
        devuelto : str = os.system("find . -name "+self.__file)
        if devuelto != "":
            return '\t--> Fichero '+str(self.__file)+' se ha encontrado.\n'
        else:
            return '\t--> Fichero '+str(self.__file)+' NO se ha encontrado.\n'