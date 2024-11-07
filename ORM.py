
class Persona:
    def __init__(self, nombre, edad, id):
        self.id = id
        self.nombre = nombre
        self.edad = edad
class Empleado(Persona):
    def __init__(self, nombre, edad, id, salario):
        super().__init__(nombre, edad, id)
        self.salario = salario
        self.proyectos = []
    def asignar_proyecto(self, proyecto):
        if isinstance(proyecto, Proyecto):
            self.proyectos.append(proyecto)
        else:
            print("El proyecto no es válido")
class Proyecto:
    def __init__(self, nombre, id):
        self.id = id
        self.nombre = nombre

