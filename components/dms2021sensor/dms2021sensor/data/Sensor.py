from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def monitorizar(self):
        pass