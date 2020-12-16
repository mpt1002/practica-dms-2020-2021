
from .serviciosEstado import ServiciosEstado

class MenuEstado(ServiciosEstado):

    __session_id : str

    def __init__(self, session_id: str):
        self.__session_id = session_id

    def ejecutarPagina(self) -> int:
        opcion : int = 0
        print('\n\t\033[1;36m'+'+------------------------------------------------------------------+')
        print('\t|\t\t\t\tMENU                               |')
        print('\t+------------------------------------------------------------------+')
        print('\t| 1. Crear usuarios                                                |')
        print('\t| 2. Modificar Permisos                                            |')
        print('\t| 3. Acceder a gestionar sensores                                  |')
        print('\t| 4. Modificar las reglas de monitorizacion de cada sensor         |')
        print('\t| 5. Obtener los valores de monitorizacion de cada sensor          |')
        print('\t| 6. Salir                                                         |')
        print('\t+------------------------------------------------------------------+')
        opcion = int(input("\t| Introduce una opcion (1-6): "))
        print('\t+------------------------------------------------------------------+\n'+'\033[0m')
        return opcion
