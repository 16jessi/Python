class Vehiculo:
    def __init__(self,marca,ruedas):
        self.marca=marca
        self.ruedas=ruedas
    def mostrar(self,marca,ruedas):
        print("Datos del vehículo: ",self.marca,self.ruedas)


m=input("Introduzca la marca del vehículo: ")
r=int(input("Introduce la cantidad de ruedas: "))
v1=Vehiculo(m,r)
v1.mostrar(m,r)