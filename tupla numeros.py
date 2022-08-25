numeros=(23,34,54,67)
lista_pares=[]
lista_impares=[]
for numero in numeros:
    if numero %2==0:
        print("numero ",numero,"es par")
        lista_pares.append(numero)
    else:
        print("numero",numero,"es impar")
        lista_impares.append(numero)
print("lista de pares :",lista_pares)
print("suma de pares: ",sum(lista_pares))
print("lista de impares :",lista_impares)
print("suma de impares :",sum(lista_impares))