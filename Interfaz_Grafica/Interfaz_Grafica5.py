from tkinter import *

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=500, height=500)

archivoMenu=Menu(barraMenu, tearoff=0) ##tearoff=0, elimina la lagrima de seleccion vacia
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como...")
archivoMenu.add_separator()
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir")

archivoEdicion=Menu(barraMenu)
archivoEdicion.add_command(label="<-- Regresar")
archivoEdicion.add_command(label="Avanzar -->")
archivoEdicion.add_separator()
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu)
archivoHerramientas.add_command(label="Ir a GitHub")

archivoAyudas=Menu(barraMenu, tearoff=0)
archivoAyudas.add_command(label="Documentación")
archivoAyudas.add_separator()
archivoAyudas.add_command(label="Licencia")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyudas)


root.mainloop()