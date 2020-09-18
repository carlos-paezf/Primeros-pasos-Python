from tkinter import *
from tkinter import filedialog

root=Tk()

def abrirArchivo():
	archivo=filedialog.askopenfilename(title="Abrir", initialdir="D:", filetypes=(
		("Archivos Comprimidos", "*.zip"), 
		("Archivo de Texto", "*.txt"), 
		("Todos los archivos", "*.*")))
	print(archivo)

Button(root, text="Abrir Archivo", command=abrirArchivo).pack()


root.mainloop()