
from abc import ABC, abstractmethod

class Archivo(ABC):

    def __init__(self, nombre, ruta):
        self._nombre = nombre
        self._ruta = ruta

    def escribir(self):
        pass

    def leer(self):
        pass