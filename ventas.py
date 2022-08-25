ventas={}
continuar=True
continuar=input("Desea continuar? si/no:")
while continuar=="SI" or continuar=="si":
    articulo=input("Ingrese articulo: ")
    precio=float(input("Ingrese precio: ")) 
    cantidad=int(input("Ingrese la cantidad: "))
    precios={"precio": precio,"cantidad":cantidad}
    ventas[articulo]=precios
    continuar=input("Desea continuar? si/no: ")#=="si"
costo=0
for a,p in ventas.items():
        precioitems=p["precio"]*p["cantidad"]
        print(a,"\t",precioitems)
        costo+=precioitems
print("Total venta: ",costo)