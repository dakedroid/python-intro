# CLASES Y OBJETOS

# CREANDO LA CLASE
class Alumno:
    def __init__(self, numControl, nombre, edad):
        self.numControl = numControl
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.numControl}: {self.nombre}, edad: {self.edad}"


# CLEANDO EL OBJETO
alumnoEmir = Alumno("20232245", "emir", 20)
alumnoROXEL = Alumno("22230979", "ROXEL", 21)
alumnoVictor = Alumno("20230221", "VICTOR", 20)

print(alumnoEmir)
print(alumnoROXEL)
print(alumnoVictor)
