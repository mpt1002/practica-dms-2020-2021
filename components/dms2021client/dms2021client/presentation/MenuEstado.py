
from ..presentation import ServiciosEstado

class MenuEstado(ServiciosEstado):

    __session_id : str

    
    def __init__(self, session_id: str):
        print("ESTOY EN MENU ESTADO")
        self.__session_id = session_id

    #@staticmethod
    def ejecutarPagina(self) -> int:
        opcion : int = 0
        print('MENU')
        print('\t1. Crear usuarios')
        print('\t2. Modificar Permisos')
        print('\t3. Acceder a gestionar sensores')
        print('\t4. Modificar las reglas de monitorizacion de cada sensor')
        print('\t5. Obtener los valores de monitorizacion de cada sensor')
        print('\t6. Salir')
        print("\tIntroduce una opcion (1-6): ")
        opcion = int(input())
        return opcion
