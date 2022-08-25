agenda={}
opcion=input("Menú de opciones: \n (1)-Añadir/modificar contacto.\n (2) Buscar contacto \n (3) Borrar contactos \n (4)Listar contacto \n (5) Salir \n Seleccione una opción: ")
while opcion!="5":
  if opcion=="1":
        nombre=input("Ingrese el nombre del contacto: ")
        if nombre in agenda:
           op=input("El contacto se encuentra en la agenda, desea editarlo: s/n")
           op=op.upper()
           if op=="s":
               telefono=input("Ingrese el número de teléfono: ")
               agenda[nombre]=telefono
        else:
          telefono=input("Ingrese el número de teléfono: ")
          agenda[nombre]=telefono
  if opcion=="2":
      buscar=input("Ingrese el nombre del contacto a buscar: ")
      buscar=buscar.upper()
      for nombre,telefono in agenda.items():
          if nombre.startswith(buscar):
             print("El número de teléfono es ",nombre, telefono)
  if opcion=="3":
      nombre=input("Ingrese contacto a eliminar: ")
      if nombre in agenda:
         del agenda[nombre]
      else:
         print("El contacto que desea eliminar no existe")
  if opcion=="4":
      print("Lista contactos agendados: ",agenda)
      for nombre,telefono in agenda.items():
          print(nombre," | ",telefono)
  opcion=input("Menú de opciones: \n (1)-Añadir/modificar contacto.\n (2) Buscar contacto \n (3) Borrar contactos \n (4)Listar contacto \n (5) Salir \n Seleccione una opción: ")        