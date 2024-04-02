
from Reescribir.conversor import Conversor

nombre = input("Ingrese el nombre del archivo CSV: ")
ruta = input("Ingrese la ruta del archivo CSV: ")

conversor = Conversor(nombre,ruta)
conversor.convertir()
