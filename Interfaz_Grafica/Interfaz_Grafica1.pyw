	#Para abrir el archivo desde el directorio, sin tener una
	#consola de comando atras, se cambia la extension del archivo
	#de .py a .pyw

from tkinter import *

#Crear una nueva ventana
raiz=Tk()
raiz.title("Ventana de Pruebas")
raiz.resizable(True, False)
raiz.iconbitmap("EscudoUsta.ico")
raiz.geometry("360x360")
raiz.config(bg="White")

#Crear el widget Frame
miFrame = Frame()
	#side permite ubicar en left, right, top, bottom
	#archor permite ubicar mediante puntos cardinales n, w, e, s
	#fill permite rellenar segun la redimension con x, y, both, none
		##miFrame.pack(fill="both", expand="True")
miFrame.pack(side="left", anchor="s")
miFrame.config(width="350", height="350")
miFrame.config(bg="Gray")
miFrame.config(bd=10)	#Tamaño del borde
miFrame.config(relief="groove")		#Tipo de Borde
miFrame.config(cursor="pirate")		#Tipo de cursor sobre el frame

raiz.mainloop()