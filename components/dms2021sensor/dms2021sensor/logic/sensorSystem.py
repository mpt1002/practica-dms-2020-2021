from dms2021sensor.data.Sensor import Sensor
import os

class SensorSystem(Sensor):
    __parametros:str
    __porcentaje:int

    def __init__(self, parametros:str = 'Mem', porcentaje:int = 50):
        # parametros, que caracteristicas del sistema se quiere monitorizar
        self.__parametros = parametros
        self.__porcentaje = porcentaje

    def monitorizar(self):
        # Monitorizar solo Mem y Swap
        proceso = os.popen('cat /proc/meminfo|grep "'+self.__parametros+'"').read()
        memTotal:str = os.popen('cat /proc/meminfo|grep "'+self.__parametros+'Total"|tr -s " " ":"|cut -d ":" -f 2 ').read()
        memFree:str = os.popen('cat /proc/meminfo|grep "'+self.__parametros+'Free"|tr -s " " ":"|cut -d ":" -f 2 ').read()
        dif:float = float(memTotal) - float(memFree)
        
        if dif > float(memTotal)*(self.__porcentaje/100):
            return "--> " + str(proceso) + "La "+self.__parametros+" usada supera el "+str(self.__porcentaje)+"%\n"
        else:
            return "--> " + str(proceso) + "La "+self.__parametros+" usada NO supera el "+str(+self.__porcentaje)+"%\n"