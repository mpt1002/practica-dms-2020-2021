#!/usr/bin/env python3
import os
from abc import ABC, abstractmethod
from ....dms2021client.bin.dms2021client import ManejadorPagina


class ServiciosEstado(ABC):
    #@staticmethod
    @abstractmethod
    def ejecutarPagina(self):
        pass

    @abstractmethod
    def logout(self):
        pass
