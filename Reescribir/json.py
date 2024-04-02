from Reescribir.archivo import Archivo
from Reescribir.csv import CSV
import json

class JSON(Archivo):

    def __init__(self, nombre, ruta):
        super().__init__(nombre, ruta)


    """
    Metodo que crea el archivo JSON con los datos especificados
    
    """
    def escribir(self, datos):
        with open(self._ruta, 'w', encoding='utf-8') as archivo_json:
            json.dump(datos, archivo_json,ensure_ascii=False, indent=4)
    