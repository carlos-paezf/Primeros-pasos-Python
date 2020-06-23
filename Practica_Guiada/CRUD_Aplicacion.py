from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.resizable(False, False)
root.config(bg="#DEDECB")


#----------------------------FUNCIONES--------------
def conexionBBDD():
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	try:
		miCursor.execute('''
			CREATE TABLE INFOUSER (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			user_name VARCHAR(50),
			surname VARCHAR(50),
			password VARCHAR(50),
			address VARCHAR(50),
			comments VARCHAR(100)
			)
			''')
		messagebox.showinfo("BBDD", "La BBDD ha sido creada con exito")
	except:
		messagebox.showwarning("Atencion", "La BBDD ya existe en el directorio")

def salirAplicacion():
	valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
	if valor == "yes":
		root.destroy()

def limpiarRegistros():
	miId.set("")
	miNombre.set("")
	miApellido.set("")
	miContrasena.set("")
	miDireccion.set("")
	campoComentario.delete(1.0, END)

def crear():
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	"""miCursor.execute("INSERT INTO INFOUSER VALUES(NULL, '" + miNombre.get() + 
		"','" + miApellido.get() + 
		"','" + miContrasena.get() +
		"','" + miDireccion.get() + 
		"','" + campoComentario.get(1.0, END) + 
		"')") """
	datos = miNombre.get(), miApellido.get(), miContrasena.get(), miDireccion.get(), campoComentario.get(1.0, END)
	miCursor.execute("INSERT INTO INFOUSER VALUES(NULL,?,?,?,?,?)",(datos))
	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro creado con exito")

def listar():
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	miCursor.execute("SELECT * FROM INFOUSER WHERE id="+miId.get())
	infoUsuario = miCursor.fetchall()
	for usuario in infoUsuario:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miApellido.set(usuario[2])
		miContrasena.set(usuario[3])
		miDireccion.set(usuario[4])
		campoComentario.insert(1.0, usuario[5])
	miConexion.commit()
	messagebox.showinfo("Usuario Listado", "Se ha listado el usuario con ID="+miId.get())

def actualizar():
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	"""miCursor.execute("UPDATE INFOUSER SET user_name='" + miNombre.get() +
		"', surname='" + miApellido.get() + 
		"', password='" + miContrasena.get() +
		"', address='" + miDireccion.get() +
		"', comments='" + campoComentario.get(1.0, END) +
		"' WHERE id=" + miId.get())"""
	datos = miNombre.get(), miApellido.get(), miContrasena.get(), miDireccion.get(), campoComentario.get(1.0, END)
	miCursor.execute('''
		UPDATE INFOUSER SET 
			user_name=?, 
			surname=?, 
			password=?, 
			address=?, 
			comments=? 
		WHERE id=''' + miId.get(), (datos))
	valor = messagebox.askokcancel("Actualizar Usuario", "¿Desea actualizar el usuario "+miId.get()+"?")
	if valor==True:
		messagebox.showinfo("Actualizar Usuario", "El usuario ha sido actualizado con exito")
	miConexion.commit()

def eliminar():
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	miCursor.execute("DELETE FROM INFOUSER WHERE id=" + miId.get())
	valor = messagebox.askokcancel("Eliminar Usuario", "¿Desea eliminar el usuario "+miId.get()+"?")
	if valor==True:
		messagebox.showinfo("Eliminar Usuario", "El usuario ha sido eliminado con exito")
	miConexion.commit()


#-----------------------------MENU-------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, width=500, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
bbddMenu.add_command(label="Conectar a BBDD", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Limpiar Registros", menu=borrarMenu)
borrarMenu.add_command(label="Limpiar Registros", command=limpiarRegistros)

crudMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Listar", command=listar)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Eliminar", command=eliminar)

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
miId = StringVar()
miNombre= StringVar()
miApellido = StringVar()
miContrasena = StringVar()
miDireccion = StringVar()

campoID = Entry(frame1, textvariable=miId)
campoID.grid(row=0, column=1, padx=10, pady=10)
campoID.config(fg="BLUE", justify="center")

campoNombre = Entry(frame1, textvariable=miNombre)
campoNombre.grid(row=1, column=1, padx=10, pady=10)

campoApellido = Entry(frame1, textvariable=miApellido)
campoApellido.grid(row=2, column=1, padx=10, pady=10)

campoContrasena = Entry(frame1, textvariable=miContrasena)
campoContrasena.grid(row=3, column=1, padx=10, pady=10)
campoContrasena.config(show="*")

campoDireccion = Entry(frame1, textvariable=miDireccion)
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


botonCrear = Button(frame2, text="Crear", command=crear)
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)
botonCrear.config(bg="#3CC72E", width=10, cursor="plus")

botonListar = Button(frame2, text="Listar", command=listar)
botonListar.grid(row=0, column=1, sticky="e", padx=10, pady=10)
botonListar.config(width=10, cursor="heart")

botonActualizar = Button(frame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)
botonActualizar.config(bg="#D7E146", width=10, cursor="exchange")

botonBorrar = Button(frame2, text="Eliminar", command=eliminar)
botonBorrar.grid(row=1, column=1, sticky="e", padx=10, pady=10)
botonBorrar.config(bg="#F64B48", width=10, cursor="pirate")


root.mainloop()