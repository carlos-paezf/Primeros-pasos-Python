class Car():
	#Constructor->estado inicial
	def __init__(self):
		#Propiedades
		#Encapsulamiento
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__rodamiento=False

	# 2 Comportamientos
	def arrancar(self, arrancar):
		self.__rodamiento=arrancar
		if(self.__rodamiento):
			chequeo=self.__chequeo_interno()
		if(self.__rodamiento and chequeo):
			return "El coche esta en marcha"
		elif(self.__rodamiento and chequeo==False):
			return "Algo va mal... No se puede arrancar"
		else:
			return "El coche esta detenido"
		self.__rodamiento=True

	def estado(self):
		print("El coche tiene ",self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

	def __chequeo_interno(self):
		print("Realizando chequeo interno...")
		self.gasolina="OK"
		self.aceite="OK"
		self.puertas="OK"
		if(self.gasolina=="OK" and self.aceite=="OK" and self.puertas=="OK"):
			return True
		else:
			return False

#instanciamiento de un objeto 
myCar=Car()
print(myCar.arrancar(True))
myCar.estado()

print("#########################")

#instanciamiento de segundo objeto
myCar2=Car()
print(myCar2.arrancar(False))
#Intento fallido de romper el encapsulamiento
myCar2.__ruedas=2
myCar2.estado()