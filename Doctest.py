import doctest
import math

def areaTriangulo(base, altura):
	'''
	Calcula el area de un triangulo dado
	El siguiente es la aplicacion del test 
	con espectativas incorrectas

	>>> areaTriangulo(2,4)
	'El area del triangulo es: 5.0'

	>>> areaTriangulo(3,6)
	'El area del triangulo es: 8.0'

	>>> areaTriangulo(4,4)
	'El area del triangulo es: 8.0'
	'''
	return "El area del triangulo es: " + str((base*altura)/2)

def compruebaEmail(email):
	'''
	Comprobacion de email recibido en busca de la @
	si tiene un @ es correcto, si tiene mas de 1 @ es incorrecto
	si el @ esta al final es incorrecto

	>>> compruebaEmail('curso@es')
	True

	>>> compruebaEmail('curso.es@')
	False

	>>> compruebaEmail('curso.es')
	True

	>>> compruebaEmail('cu@rso@es')
	False
	'''	
	if (email.count('@')!=1 or email.rfind('@')==(len(email)-1) or email.find('@')==0):
		return False
	else:
		return True

def raizCuadrada(listaNum):
	'''
	La funcion devuelve una lista con la raiz cuadrada de 
	los elementos numericos pasados por parametros en otra lista
	Codigo de prueba complejo para explicar un codigo anidado

	
	>>> lista=[]
	>>> for i in [4, 9, 16]:
	... 	lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]

	>>> lista=[]
	>>> for i in [4, -9, -16]:
	... 	lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
		...
  	ValueError: math domain error
	'''
	return [math.sqrt(n) for n in listaNum]


doctest.testmod()