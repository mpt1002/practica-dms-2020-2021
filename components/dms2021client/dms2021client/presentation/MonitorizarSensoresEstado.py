from ..presentation import ServiciosEstado
from dms2021client.data.rest import sensorService

class MonitorizarSensoresEstado(ServiciosEstado):
    
    def __init__(self, session_id : str, sensorservice : sensorService):
        pass

    def ejecutarPagina(self) -> int:
        print('Valores de monitorizacion de cada sensor')
        print('FALTA CODIGO')
        return 0