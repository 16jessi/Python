num_loteria=[]
for i in range (1,7):
    print("Ingrese el ",i,"°: ")
    nro_ganador=int(input("Número ganador de la loteria:"))
    num_loteria.append(nro_ganador)
num_loteria.sort()#ordena la lista de menor a mayor
print("Los números ganadores de la loteria son: ",num_loteria)