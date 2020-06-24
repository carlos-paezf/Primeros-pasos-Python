'''			Funciones simples
def area_triangulo(base, altura):
	return (base*altura)/2

triangulo1 = area_triangulo(5,7)
triangulo2 = area_triangulo(9,6)
print(triangulo1)
print(triangulo2)
'''

 	#Las funciones lambda permite simplificar funciones simples
 	#como por ejemplo el calculo de la funcion anterior
area_triangulo=lambda base,altura:(base*altura)/2
print(area_triangulo(5,6))


exponente_cubo = lambda num:pow(num, 3)
print(exponente_cubo(3))


destacar_valor = lambda comision:"¡${}!".format(comision)
comision_Juan=12345
print(destacar_valor(comision_Juan))