"""1)Desarrollar un programa que por medio de una función
agregar productos y su cantidaden stock en un diccionario
2) Otra función que permita mostrar los productos y cantidades
3)Otra que permita vender producto ingresando nombre y cantidad
4)Otra que permita mostrar los más vendidos"""


productos={}
masVendido={}
def agregarProducto():
    while True:
      nombre=input("Ingrese el artículo: ")
      precio=float(input("Ingrese precio: ")) 
      cantidad=int(input("Ingrese la cantidad en stock: "))
      productos[nombre]=cantidad
      op=input("Presione s para continar ingresando productos: ")
      if op=="s" or op=="S":
        continue
      else:
        break

def mostrarProducto():
    for n,c in productos.items():
        print(n, "|" ,c)

def venderProducto():
    nombre=input("Ingrese el nombre del producto a vender: ")
    for p,c in productos.items():
      if nombre==p:
        cantidadVender=int(input("Ingrese la cantidad vendida: "))
        productos[p]=c-cantidadVender
        masVendido[p]=cantidadVender
      else:
        productos[p]=c


def mostrarmasVendido():
    mv=max(masVendido)
    print("El producto más vendido es: ",mv)


"""agregarProducto()
print("Nombre producto | cantidad")
mostrarProducto()
venderProducto()
mostrarmasVendido() """