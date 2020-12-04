#!/usr/bin/env python3
#import os
from abc import ABC, abstractmethod
#from . import ManejadorPagina

class ServiciosEstado(ABC):
    #@staticmethod
    @abstractmethod
    def ejecutarPagina(self):
        pass

    @abstractmethod
    def logout(self):
        pass
