materias=["Geografía","Matemáteticas","Historia","Fisica","Química","Lengua"]
notas=[]
for materia in materias:
    nota=input("Ingresa nota de "+materia+ " :")
    notas.append(nota)
for i in range(len(materias)):
    print(materias[i],":",notas[i])