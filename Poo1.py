class Car():
	#Propiedades
	largoChasis=250
	anchoChasis=120
	ruedas=4
	rodamiento=False
	# 2 Comportamientos
	def arrancar(self):
		self.rodamiento=True
	def estado(self):
		if(self.rodamiento):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"
#instanciamiento de un objeto 
myCar=Car() 	
#pruebas
print("Ancho del chasis: ",myCar.anchoChasis)
print("Largo del chasis: ",myCar.largoChasis)
print("Ruedas: ",myCar.ruedas)
print("Rodamiento: ",myCar.rodamiento)
print(myCar.estado())
myCar.arrancar()
print("Rodamiento luego de arrancar: ",myCar.rodamiento)
print(myCar.estado())