venta={}
continuar=True
continuar=input("Desea ingresar productos? s/n: ")
continuar=continuar.upper()
while continuar=="s":
    producto=input("Ingrese el producto: ")
    producto=producto.upper()
    precio=float(input("Ingrese su precio: "))
    producto[producto]=precio
    continuar=input("Desea ingresar productos? s/n: ")
    continuar=continuar.upper()
for p,v in producto.items():
    if v < 100:
        valor_con_incremento=v*0.10+v
        print("Para el producto: ",p,"su valor con incremento es: $",valor_con_incremento)
    elif v >= 100:
        print("El producto: ",p,"tiene u valor de: $",v)
    else:
        valor_con_descuento=v*-0.10+v
        print("Para el producto: ",p,"su valor con descuentoes: $",valor_con_descuento)