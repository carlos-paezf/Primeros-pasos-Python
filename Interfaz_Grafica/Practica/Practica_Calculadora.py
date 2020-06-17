from tkinter import *

root = Tk()
miFrame=Frame(root)
miFrame.pack()

#Variables globales
operacion=""
numeroPantalla=StringVar()
resultado=0
resetearPantalla=False
numero1=0
contadorResta=0
contadorMultiplicacion=0
contadorDivision=0

#Pantalla de salida
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=0, column=0, padx=5, pady=5, columnspan=4)
pantalla.config(background="#221F1F", fg="#FFFFFF", justify="right")

#Pulsaciones del teclado
def numeroPulsado(num):
	global operacion
	global resetearPantalla
	if resetearPantalla != False:
		numeroPantalla.set(num)
		resetearPantalla=False
	else:
		numeroPantalla.set(numeroPantalla.get()+num)

#Funcion Suma
def suma(num):
	global operacion
	global resultado
	global resetearPantalla
	resultado+=float(num)
	operacion="suma"
	resetearPantalla=True
	numeroPantalla.set(resultado)

#Funcion Resta
def resta(num):
	global operacion
	global resultado
	global numero1
	global contadorResta
	global resetearPantalla
	if contadorResta==0:
		numero1=float(num)
		resultado=numero1
	else:
		if contadorResta==1:
			resultado=numero1-float(num)
		else:
			resultado=float(resultado)-float(num)
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contadorResta=contadorResta+1
	operacion="resta"
	resetearPantalla=True

#Funcion Multiplicacion
def multiplicacion(num):
	global operacion
	global resultado
	global numero1
	global contadorMultiplicacion
	global resetearPantalla
	if contadorMultiplicacion==0:
		numero1=float(num)
		resultado=numero1
	else:
		if contadorMultiplicacion==1:
			resultado=numero1*float(num)
		else:
			resultado=float(resultado)*int(num)
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contadorMultiplicacion=contadorMultiplicacion+1
	operacion="multiplicacion"
	resetearPantalla=True

#Funcion Division
def division(num):
	global operacion
	global resultado
	global numero1
	global contadorDivision
	global resetearPantalla
	if contadorDivision==0:
		numero1=float(num)
		resultado=numero1
	else:
		if contadorDivision==1:
			resultado=numero1/float(num)
		else:
			resultado=float(resultado)/float(num)
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contadorDivision=contadorDivision+1
	operacion="division"
	resetearPantalla=True

#Funcion igual
def igual():
	global resultado
	global operacion
	global contadorResta
	global contadorMultiplicacion
	global contadorDivision
	if operacion=="suma":
		numeroPantalla.set(resultado+float(numeroPantalla.get()))
		resultado=0
	elif operacion=="resta":
		numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))
		resultado=0
		contadorResta=0
	elif operacion=="multiplicacion":
		numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))
		resultado=0
		contadorMultiplicacion=0
	elif operacion=="division":
		numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))
		resultado=0
		contadorDivision=0

#Botones Fila 1
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=1, column=0)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=1, column=1)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=1, column=2)
botonDiv=Button(miFrame, text="/", width=3, command=lambda:division(numeroPantalla.get()))
botonDiv.grid(row=1, column=3)

#Botones Fila 2
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=2, column=0)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=2, column=1)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=2, column=2)
botonMul=Button(miFrame, text="X", width=3, command=lambda:multiplicacion(numeroPantalla.get()))
botonMul.grid(row=2, column=3)

#Botones Fila 3
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=3, column=0)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=3, column=1)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=3, column=2)
botonRes=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRes.grid(row=3, column=3)

#Botones Fila 4
botonDec=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonDec.grid(row=4, column=0)
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=4, column=1)
botonSum=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=4, column=2)
botonIgu=Button(miFrame, text="=", width=3, command=lambda:igual())
botonIgu.grid(row=4, column=3)



root.mainloop()