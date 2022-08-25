class Persona:
    def __init__(self):
        self.nombre=input("Nombre: ")
        self.edad=input("Edad: ")
        self.dni=input("D.N.I: ")
    def mostrar(self):
        print(self.nombre,self.edad,self.dni) 

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Suledo: "))
        self.antiguedad=int(input("Antiguedad :"))
    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)
        print("Antigüedad: ",self.antiguedad)
    def pagaImpuestos(self):
        if self.sueldo>300000:
            i=self.sueldo*0.30
            print(self.nombre,"Debe pagar impuestos",i)
        else:
            print(self.nombre,"No debe pagar impuestos")
    def aumento(self):
        if self.antiguedad>5:
            a=self.sueldo*0.30
            print("El empleado: ",self.nombre)
            print("Tiene un aumento de: ",a)

class Cliente(Persona):
    def __init__(self):
        super().__init__()
        self.zona=input("Ingrese zona: ")
        self.direccion=input("Ingrese dirección: ")
        self.bonificacion=int(input("Ingrese bonificación: "))
    def mostrar(self):
        return super().mostrar()
        print("El cliente ",self.nombre," zona: ",self.zona," dirección: ",self.direccion," bonificación: ",self.bonificacion)
        if self.bonificacion>0:
            print("Tiene una bonificación del: ",self.bonificacion)


p1=Persona()
p1.mostrar()
e1=Empleado()
e1.mostrar()
e1.pagaImpuestos()
e1.aumento()
b1=Cliente()
b1.mostrar()