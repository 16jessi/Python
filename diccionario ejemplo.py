pelicula={
    "Nombre": "Harry Potter",
    "Protagonistas": ["Harry","Ron"],
    "Estreno": 2001,
    "Género": "Fantasía",
}
print(pelicula)
for key in pelicula:
    print(key,":",pelicula[key])
keys=pelicula.keys()
print("Claves :",keys) # me muestra la clave
valor=pelicula.get("Protagonistas")
print("Valores obtenidos: ",valor)
values=pelicula.values()
print("Valores :",values)
pelicula2=pelicula.copy()#me copia todo el contenido de la lista
print("2° lista :",pelicula2)
pelicula.pop("Género")
print(pelicula.pop("Protagonistas"))
pelicula2.clear()#borra el contenido de toda la lista
print("Elemento borrado: ",pelicula2)