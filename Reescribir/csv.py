from Reescribir.archivo import Archivo
import csv
from Reescribir.estudiante import Estudiante


class CSV(Archivo):

    def __init__(self, nombre, ruta):
        super().__init__(nombre, ruta)



    """
    Método lee el archivo CSV y retorna los datos

    """
    def leer(self):
        estudiantes = []
        with open(self._ruta, 'r', newline='', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                id, nombre, apellido = fila 
                estudiantes.append(Estudiante(id, nombre, apellido))

        return estudiantes