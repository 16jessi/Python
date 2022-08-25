from cProfile import label
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from tkinter.tix import COLUMN
from turtle import width

root=Tk()
root.title("GESTIÓN EMPLEADOS")
root.geometry("650x350")
Id=StringVar()
Nombre=StringVar()
Cargo=StringVar()
Salario=StringVar()

def conexion():
    miconexion=sqlite3.connect("base")
    micursor=miconexion.cursor()
    try:
        micursor.execute('''CREATE TABLE empleado (Id INTEGER PRIMARY KEY AUTOINCREMENTAL,
        Nombre TEXT(50) NOT NULL, Cargo TEXT(50) NOT NULL, Salario INT NOT NULL)''' )
        messagebox.showinfo("conexion", "conexión creada de manera  exitosa con base de datos")

    except:
        messagebox.showinfo("conexion", "conexion exitosa a base de datos")

def crear():
    miconexion=sqlite3.connect("base")
    micursor=miconexion.cursor()
    try:
        datos=Nombre.get(),Cargo.get(),Salario.get()
        micursor.execute("INSERT INTO empleado vALUES(NULL, ?,?,?)",(datos))
        messagebox.showinfo("conexion", "El registro del empleado se registro con exito")
        miconexion.commit()

    except:
        messagebox.showwarning("ADVERTENCIA", "Algo salio mak")
    limpiarCampos()    
    mostrar()

def limpiarCampos():
    Id.set("")
    Nombre.set("")
    Cargo.set("")
    Salario.set("")
def mostrar():
    miconexion=sqlite3.connect("base")
    micursor=miconexion.cursor()
    registro=tree.get_children()
    for elemento in registro:
        tree.delete(elemento)
    try:
        micursor.execute("SELECT * FROM empleado" )
        for row in micursor:
            tree.insert("",0,text=row[0], values=(row[1],row[2],row[3]))
        
    except:
        messagebox.showinfo("conexion", "algo salio mal")    
  

tree=ttk.Treeview(height=10, columns=('#0',"#1",'#3'))
tree.place(x=10, y=150)
tree.column('#0',width=100)
tree.heading('#0',text="ID",anchor=CENTER)
tree.heading('#1',text="Nombre",anchor=CENTER)
tree.heading('#2',text="CARGO",anchor=CENTER)
tree.heading('#3',text="SALARIO",anchor=CENTER)

def actualizar():
    miconexion=sqlite3.connect("base")
    micursor=miconexion.cursor()
    try:
        datos=Nombre.get(),Cargo.get(),Salario.get()
        micursor.execute("UPDATE empleado SET Nombre=?, Cargo=?,Salario=? WHERE Id=" +Id.get(),(datos))
        messagebox.showinfo("conexion", "El registro del empleado se actualizo con exito")
        miconexion.commit()

    except:
        messagebox.showwarning("ADVERTENCIA", "Algo salio mak")
    limpiarCampos()    
    mostrar()
def seleccionConClick(event):
    item=tree.identify('item',event.x,event.y)
    Id.set(tree.item(item,"text"))
    Nombre.set(tree.item(item,"values")[0])
    Cargo.set(tree.item(item,"values")[1])
    Salario.set(tree.item(item,"values")[2])
def ayudamenu():
    pass
def mensaje():
    pass
def eliminar():
    pass
def salir():
    root.destroy()

tree.bind("<Double-1>",seleccionConClick)    
menubar=Menu(root)
menubasedato=Menu(menubar, tearoff=0)
menubasedato.add_command(label="Crear/Conectar BASE DE DATOS", command=crear)
menubasedato.add_command(label="Eliminar Base de Datos", command=crear)
menubasedato.add_command(label="Salir", command=crear)
menubar.add_cascade(label="INIICIO", menu=menubasedato)
menuayuda=Menu(menubar,tearoff=0)
menuayuda.add_command(label="Resetear",command=limpiarCampos)
menuayuda.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Ayuda", command=ayudamenu)

labelId=label(root,text="Id")
labelId.place(x=50,y=5)
EntryId=Entry(root,textvariable=Id,bg="yelow")
EntryId.place(x=100,y=5)

labelNombre=label(root,text="Nombre")
labelNombre.place(x=50,y=30)
EntryNombre=Entry(root,textvariable=Nombre,width=50,bg="green")
EntryNombre.place(x=100,y=30)

labelCargo=label(root,text="Cargo")
labelCargo.place(x=50,y=60)
EntryCargo=Entry(root,textvariable=Cargo,width=50,bg="blue")
EntryCargo.place(x=100,y=60)

labelSalario=label(root,text="Salario")
labelSalario.place(x=50,y=90)
EntrySalario=Entry(root,textvariable=Salario,width=50,bg="purple")
EntrySalario.place(x=100,y=90)




root.config(menu=menubar)


root.mainloop()
