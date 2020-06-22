from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.resizable(False, False)
root.config(bg="#DEDECB")

#-----------------------------MENU-------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, width=500, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
bbddMenu.add_command(label="Conectar a BBDD")
bbddMenu.add_command(label="Salir")

borrarMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Borrar Registros", menu=borrarMenu)
borrarMenu.add_command(label="Limpiar Registros")

crudMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Listar")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Eliminar")

acercaMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=acercaMenu)
acercaMenu.add_command(label="Acerca de ...")
acercaMenu.add_command(label="Ir a GitHub")


#----------------------------FRAME DE CAMPOS---------
frame1 = Frame(root)
frame1.pack(fill="both", expand="True")
frame1.config(relief="groove", bd=5, bg="#EDEDDA")

			#----------------Labels
labelID = Label(frame1, text="Id:")
labelID.grid(row=0, column=0, sticky="e", padx=10, pady=10)

labelNombre = Label(frame1, text="Nombre:")
labelNombre.grid(row=1, column=0, sticky="e", padx=10, pady=10)

labelApellido = Label(frame1, text="Apellido:")
labelApellido.grid(row=2, column=0, sticky="e", padx=10, pady=10)

labelContrasena = Label(frame1, text="Contraseña:")
labelContrasena.grid(row=3, column=0, sticky="e", padx=10, pady=10)

labelDireccion = Label(frame1, text="Direccion:")
labelDireccion.grid(row=4, column=0, sticky="e", padx=10, pady=10)

labelComentarios = Label(frame1, text="Comentarios:")
labelComentarios.grid(row=5, column=0, sticky="e", padx=10, pady=10)

			#----------------Campos de textos
campoID = Entry(frame1)
campoID.grid(row=0, column=1, padx=10, pady=10)
campoID.config(fg="BLUE", justify="center")

campoNombre = Entry(frame1)
campoNombre.grid(row=1, column=1, padx=10, pady=10)

campoApellido = Entry(frame1)
campoApellido.grid(row=2, column=1, padx=10, pady=10)

campoContrasena = Entry(frame1)
campoContrasena.grid(row=3, column=1, padx=10, pady=10)
campoContrasena.config(show="*")

campoDireccion = Entry(frame1)
campoDireccion.grid(row=4, column=1, padx=10, pady=10)

campoComentario = Text(frame1, width=20, height=5)
campoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(frame1, command=campoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
campoComentario.config(yscrollcommand=scrollVert.set)


#----------------------------FRAME DE BOTONES
frame2 = Frame(root)
frame2.pack(fill="both", expand="True")
frame2.config(relief="ridge", bd=5, bg="#E3E3D9")


botonCrear = Button(frame2, text="Crear")
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)
botonCrear.config(bg="#3CC72E", width=10, cursor="plus")

botonListar = Button(frame2, text="Listar")
botonListar.grid(row=0, column=1, sticky="e", padx=10, pady=10)
botonListar.config(width=10, cursor="heart")

botonActualizar = Button(frame2, text="Actualizar")
botonActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)
botonActualizar.config(bg="#D7E146", width=10, cursor="exchange")

botonBorrar = Button(frame2, text="Eliminar")
botonBorrar.grid(row=1, column=1, sticky="e", padx=10, pady=10)
botonBorrar.config(bg="#F64B48", width=10, cursor="pirate")


root.mainloop()