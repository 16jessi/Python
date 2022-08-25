compra={}
continuar= True
while continuar: #para no colocar el cartel dos veces.
     articulo=input("Ingrese artículo: ") #ingreso de claves
     precio=float(input("Precio $")) #ingreso de valores
     compra[articulo]=precio #se carga todo en el diccionario compra
     continuar=input("¿Desea ingresar otro artículo?: si/no ")=="si" #la condicion del while
print("Lista de compras: ",compra)
costo=0
for articulo,precio in compra.items(): #hace la lista, al recorrer cada articulo y precio ingresados.
    print(articulo,"\t:",precio) # "\t" crea un espacio en el cartel
    costo+=precio #es lo mismo que "costo=costo+precio"
print("Total de compra: ",costo)