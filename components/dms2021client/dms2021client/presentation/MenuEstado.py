


class MenuEstado:

    def __init__(self, session_id: str):
        pass

    @staticmethod
    def ejecutarPagina(session_id: str) -> int:
        opcion = 0
        while(opcion >= 0 and opcion < 6):
            print('MENU')
            print('\t1. Crear usuarios')
            print('\t2. Modificar Permisos')
            print('\t3. Acceder a gestionar sensores')
            print('\t4. Modificar las reglas de monitorizacion de cada sensor')
            print('\t5. Obtener los valores de monitorizacion de cada sensor')
            print('\t6. Salir')
            print("\tIntroduce una opcion (1-6): ")
            opcion = input()
        return opcion