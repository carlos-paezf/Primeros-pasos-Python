class Areas:
	'''
	Esta clase calcula el area de diversas
	figuras geometricas
	'''
	def areaCuadrado(lado):
		'''
		Calcula el area de un cuadrado elevando al cuadrado el
		dato pasado por parametro
		'''
		return "El area del cudrado es: " + str(pow(lado,2))

	def areaTriangulo(base, altura):
		'''
		Calcula el area de un triangulo teniendo en cuenta la
		base y la altura
		'''
		return "El area del triangulo es: " + str((base*altura)/2)

print(Areas.areaCuadrado(5)) #<--------Imprimir la funcion
print(Areas.areaCuadrado.__doc__) #<-----Imprimir la documentacion en consola
help(Areas.areaCuadrado)

help(Areas.areaTriangulo)

help(Areas)