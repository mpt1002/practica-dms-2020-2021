
from .ServiciosEstado import ServiciosEstado
from ...bin.dms2021client import ManejadorPagina

class MenuEstado(ServiciosEstado):

    # Referncia a la clase contexto
    __manejador : ManejadorPagina

    
    def __init__(self, manejador: ManejadorPagina):
        self.__manejador = manejador

    #@staticmethod
    def ejecutarPagina(self) -> int:
        opcion : int = 0
        self.__manejador.set_opcion(opcion)
        while(opcion >= 0 and opcion < 6):
            print('MENU')
            print('\t1. Crear usuarios')
            print('\t2. Modificar Permisos')
            print('\t3. Acceder a gestionar sensores')
            print('\t4. Modificar las reglas de monitorizacion de cada sensor')
            print('\t5. Obtener los valores de monitorizacion de cada sensor')
            print('\t6. Salir')
            print("\tIntroduce una opcion (1-6): ")
            opcion = int(input())
        self.__manejador.set_opcion(opcion)
        return opcion

    def logout(self):
        pass