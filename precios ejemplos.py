ventas={}
cantidad=[]
continuar=True
#continuar=input("Desea continuar? Si/No: ")
while continuar: #=="si":
    articulo=input("Ingrese un antículo: ")
    precio=float(input("Ingrese precio: "))
    cantidad=int(input("Ingrese la cantidad: "))
    precios={"precio":precio,"cantidad":cantidad}
    ventas[articulo]=precios
    continuar=input("Desea continuar? si/no. ")=="si"
costo=0
for articulo,precios in ventas.items():
    precioitems=precios["precio"]*precios["cantidad"]
    print(articulo,"\t",precioitems)
    costo+=precioitems
print("Total venta: ",costo)