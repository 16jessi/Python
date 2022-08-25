class Alumno:
    def __init__(self):
        self.nombre=input("Apellido y nombre del alumno: ")
        self.edad=input("Edad del alumno: ")
        self.dni=input("D.N.I del alumno: ")
        self.nota=input("Nota del alumno: ")
    def mostrar(self):
        print(self.nombre,self.edad,self.dni,self.nota) 
    def situacion(self):
        if self.nota>="7":
            print(self.nombre," Aprobo la materia con: ",self.nota)
        else:
            print(self.nombre," Desaprobo la materia con: ",self.nota)

c1=Alumno()
c1.mostrar()
c1.situacion()