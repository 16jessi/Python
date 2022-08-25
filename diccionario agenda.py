clientes={}
opcion=""
while opcion!="5":
    if opcion=="1":
        nombre=input("Ingrese el nombre del cliente: ")
        direccion=input("Ingrese dirección del cliente: ")
        telefono=input("Ingrese el telefono del cliente: ")
        email=input("Ingresa email del cliente: ")
        cliente=("Nombre: ",nombre,"Dirección: ,",direccion,"Telefono: ",telefono,"Email: ",email)
        clientes[id]=cliente
        print("Cliente",cliente)
        print("Clientes",clientes)
    if opcion=="2":
        id=input("Ingrese el id del cliente que desea eliminar: ")
        if id in clientes:
            del clientes[id]
        else:
            print("No existe el id ingresado",id)
    if opcion =="3":
        id=input("Ingrese el id del cliente que desea consultar: ")
        if id in clientes:
            print("id: ",id)
            for clave,valor in clientes[id].items():
                print(clave,":",valor)
        else:
            print("El id ingresado no existe")
    if opcion =="4":
        print("Lista de clientes: " )
        print("___________________")
        for clave,valor in clientes.items():
            print(clave,valor["nombre"],valor["telefono"],valor["email"])  
    opcion=input("Menu de opciones \n (1)Ingresar un cliente \n (2)Eliminar un cliete \n (3)Mostrar un determinado cliente \n (4)Listar todos los clientes \n (5)Salir \n Ingrese una opción:")
