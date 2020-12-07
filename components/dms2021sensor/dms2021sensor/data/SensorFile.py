from Sensor import Sensor
import os

class SensorFile (Sensor):
    file:str
    def __init__(self, file):
        self.file = '../dms2021sensor/data/'+file

    def monitorizar(self):
        devuelto = os.system('find '+ self.file)
        return devuelto == self.file