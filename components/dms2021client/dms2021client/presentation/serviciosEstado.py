from abc import ABC, abstractmethod

class ServiciosEstado(ABC):

    @abstractmethod
    def ejecutarPagina(self) -> int:
        pass
