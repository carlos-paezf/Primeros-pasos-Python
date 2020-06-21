from tkinter import *
from tkinter import messagebox        #<--- Importar las ventanas emergentes

root=Tk()

def infoAdicional():
	messagebox.showinfo("Primeros Pasos en Python", "https://github.com/carlos-paezf/Primeros-pasos-Python.git")
def aviso():
	messagebox.showwarning("Licencia", "En proceso de obtención")
def salir():
	valor=messagebox.askquestion("Salir", "¿Deseas salir?")
	if valor=="yes":
		root.destroy()
def eliminar():
	valor=messagebox.askokcancel("Eliminar", "Vas a eliminar el archivo:")
	if valor==True:
		root.destroy()
def reintentar():
	valor=messagebox.askretrycancel("Reintentar", "Accion Prohibida")
	if valor==False:
		root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=500, height=500)

ayuda=Menu(barraMenu, tearoff=0)
ayuda.add_command(label="Ir a GitHub", command=infoAdicional)
ayuda.add_separator()
ayuda.add_command(label="Licencia", command=aviso)
ayuda.add_separator()
ayuda.add_command(label="Salir", command=salir)
ayuda.add_separator()
ayuda.add_command(label="Eliminar", command=eliminar)
ayuda.add_separator()
ayuda.add_command(label="Reintentar", command=reintentar)

barraMenu.add_cascade(label="Ayuda en ventanas emergentes", menu=ayuda)


root.mainloop()