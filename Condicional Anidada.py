nu= "Jessica"
c= "2314"
nomUsu=input("Ingrese su nombre de usuario")
if nomUsu==nu:
    contras=input("Ingrese su contraseña")
    if contras==c:
        print("Bienvenido al sistema")
    else:
        print("Su contraeña es incorrecta")
else:
    print("Su nombre de ususario es incorrecto")