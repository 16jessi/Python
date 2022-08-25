"""def fun():
    print("Hola desde una función")
fun()



def nombre_funcion(nombre,apellido):#recibe la funcion como parametros
    print("Hola",nombre,apellido,"desde una función")

tu_nombre=input("¿Cual es tu nombre?: ")#llama a la función
tu_apellido=input("¿Cual es tu apellido?: ")#"" " " ""
nombre_funcion(tu_nombre,tu_apellido) #paso de argumentos

#pass se utiliza cuando no tenemos bloque de código
#desarollado en una función para que no arroge error 

def mifuncion(*hijos):
    print("Mis hijos menores son",hijos[1],hijos[2])
mifuncion("Ana","Pedro","Laura")
mifuncion("Ana","Pedro","Laura")


def funcion_claveValor(niño3,niño2,niño1):
    print("El menor de los tres niños es: ",niño1)
funcion_claveValor(niño1="Caro",niño2="Lautaro",niño3="Ana")



def funcionPalabrasClave(**niños):
    print("El apellido de: ", niños["nombre"],"es: ",niños["apellido"])
funcionPalabrasClave(nombre="Elena", apellido="Arias")


def funcion_paises(pais="Argetina"):
    print(pais)
funcion_paises()
funcion_paises(pais="China")
funcion_paises()#se escribe el valor predeterminado
funcion_paises(pais="Perú")


def alimentos(lista):
    for i in lista:
        print("Lista de alimentos: ",i)
lista=["leche","queso","jamon"]
alimentos(lista)

#funciones que devuelven un valor utilizando la declaración
#"return"

def funcionCalcularElPorcentaje(n):
    return n*0.10
print(funcionCalcularElPorcentaje(100))"""


def esPar(n):
    
    if n%2==0:
        return True
        print("El número ingresado es par")
    else:
        return False
        print("El número ingresado es impar")
num=int(input("Ingrese un número: "))

esPar(num)

