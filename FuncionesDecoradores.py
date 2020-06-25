def funcion_decoradora(funcion_parametro):
	def funcion_interna(*args, **kwargs):
		#Acciones adicionales que decoran
		print("Vamos a realizar un calculo: ")
		funcion_parametro(*args, **kwargs)
		print("Se ha terminado el proceso")
		print()
	return funcion_interna

@funcion_decoradora
def suma(num1, num2, num3, num4):
	print(num1+num2+num3+num4)

def resta(num1, num2):
	print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
	print(pow(base,exponente))


resta(10,3) #<------------Funcion sin decorar
suma(7,5,3,4) #<-------------Funcion decorada
potencia(base=5,exponente=3) #<--------Funcion decorada con argumentos claves