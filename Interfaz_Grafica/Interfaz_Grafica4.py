from tkinter import *

root=Tk()
miFrame=Frame(root)
miFrame.pack()


##RadioButton
Label(miFrame, text="Genero", width=50).pack()

varOpcion=IntVar()

def imprimir():
	print(varOpcion.get())
	if varOpcion.get()==1:
		etiqueta.config(text="Has elegido masculino")
	if varOpcion.get()==2: 
		etiqueta.config(text="Has elegido femenino")
	if varOpcion.get()==3:
		etiqueta.config(text="Has elegido otros")

Radiobutton(miFrame, text="Maculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(miFrame, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()
Radiobutton(miFrame, text="Otros", variable=varOpcion, value=3, command=imprimir).pack()

etiqueta=Label(miFrame)
etiqueta.pack()


##Checkbutton
Label(miFrame, text="Destinos de viaje", width=50).pack()

playa=IntVar()
montana=IntVar()
turismorural=IntVar()

def opcionesViaje():
	opcionEscogida=""
	if(playa.get()==1):
		opcionEscogida+=" -Playa- "
	if(montana.get()==1):
		opcionEscogida+=" -Montaña- "
	if(turismorural.get()==1):
		opcionEscogida+=" -Turismo Rural- "
	mensaje.config(text=opcionEscogida)

Checkbutton(miFrame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(miFrame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(miFrame, text="Turismo Rural", variable=turismorural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

mensaje=Label(miFrame)
mensaje.pack()


root.mainloop()