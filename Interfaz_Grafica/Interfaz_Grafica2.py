from tkinter import *

root=Tk()
miFrame=Frame(root, width=1205, height=500)
miFrame.pack()

#Creacion de un label de texto
Label(miFrame, text="Hello World", fg="Blue", 
	font=("Comic Sans MS", 18)).place(x=100, y=250)

	#Creacion de un label de imagen o gif
#miImagen=PhotoImage(file="loading.gif")
#Label(miFrame, image=miImagen).place(x=0, y=0)

#Creacion de un label de cuadro de texto
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=25, pady=10)
cuadroNombre.config(fg="red", justify="center")
nombreLabel=Label(miFrame, text="Nombre:")
		#grid permite cuadrar los datos en una tabla
		#sticky permite alinear basandose en puntos cardinales n, s, e, w
		#padx y pady permiten controlar el pading segun su eje, x o y
nombreLabel.grid(row=0, column=0, sticky="w", padx=25, pady=10)

cuadroEdad=Entry(miFrame)
cuadroEdad.grid(row=1, column=1, padx=25, pady=10)
cuadroEdad.config(fg="blue", justify="left")
EdadLabel=Label(miFrame, text="Edad:")
EdadLabel.grid(row=1, column=0, sticky="e", padx=25, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=25, pady=10)
cuadroDireccion.config(fg="green", justify="right")
direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=2, column=0, sticky="w", padx=25, pady=10)

cuadroContrasena=Entry(miFrame)
cuadroContrasena.grid(row=3, column=1, padx=25, pady=10)
cuadroContrasena.config(show="*", justify="center")
contrasenaLabel=Label(miFrame, text="Contraseña:")
contrasenaLabel.grid(row=3, column=0, sticky="e", padx=25, pady=10)

root.mainloop()