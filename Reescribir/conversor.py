from Reescribir.archivo import Archivo
from Reescribir.csv import CSV
from Reescribir.json import JSON
import os
from Reescribir.estudiante import Estudiante

class Conversor:

    def __init__(self, nombre, ruta):
        self.archivo_csv = CSV(nombre, ruta)
        self.archivo_json = JSON(nombre.replace('.csv', '.json'), ruta.replace('.csv', '.json'))


    """
    Método que convierte un archivo CSV a JSON
    
    """
    def convertir(self):
        #verificar si el archivo CSV existe
        if not os.path.exists(self.archivo_csv._ruta):
            print("El archivo CSV especificado no existe.")
            return
        
        #verificar si el archivo ya existe      
        if os.path.exists(self.archivo_json._ruta):
            print("El archivo JSON ya existe, cambia su nombre")
            return
        
        #leer el archivo CSV y convertirlo a JSON
        datos_csv = self.archivo_csv.leer()
        datos_json = []
        for estudiante in datos_csv:
            datos_json.append(estudiante.diccionario())
        self.archivo_json.escribir(datos_json)
        print("La conversión ha sido exitosa. Se ha creado el archivo JSON.")