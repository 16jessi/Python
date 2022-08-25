from funcionesCalculadora import*
while True:
    n1=float(input("Ingrese el 1° número: "))
    n2=float(input("Ingrese el 2° número: "))
    
    calculo=input("Seleccione una opción: \n 1)Suma: \n 2)Resta: \n 3)Multiplicación: \n 4)División: \n 5)Potenciación: \n 6)Resto: \n 7)Fin: \n *Opción: ")
    if calculo=="1":
      print(suma(n1,n2))
    elif calculo=="2":
        print(resta(n1,n2))
    elif calculo=="3":
        print(multiplicacion(n1,n2))
    elif calculo=="4":
        print(division(n1,n2))
    elif calculo=="5":
        print(potenciacion(n1,n2))
    elif calculo=="6":
        print(resto(n1,n2))
    elif calculo=="7":
        print("Fin de los calculos")
        break
    else:
        print("La opción ingresada no es valida")