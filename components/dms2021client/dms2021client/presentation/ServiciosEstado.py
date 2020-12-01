#!/usr/bin/env python3
import os
from abc import ABC, abstractmethod


class ServiciosEstado(ABC):
    @staticmethod
    @abstractmethod
    def ejecutarPagina(session_id:str):
        pass
