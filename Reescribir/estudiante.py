
class Estudiante:

    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

    def diccionario(self):
        return {
            "id" : self.id,
            "nombre" : self.nombre,
            "apellido" : self.apellido
        }