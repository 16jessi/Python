from funcionDiccionario import*
while True:
    menu=input("Seleccione la acción que desea realizar:\n 1)-Agregar productos. \n 2)-Vender productos. \n 3)-Mostrar los productos. \n 4)-Mostrar el producto más vendido. \n 5)-Fin. \n Ingrese opción: ")
    if menu=="1":
        agregarProducto()
    if menu=="2":
        venderProducto()
    if menu=="3":
        mostrarProducto()
    if menu=="4":
        mostrarmasVendido()
    if menu=="5":
        print("Fin")
        break
    else:
        print("La opción ingresada no es correcta.")