import pickle

lista_nombres=["Pedro", "Juan", "Maria", "Laura"]
fichero_binario=open("lista_nombres", "wb")
#volcado de la lista al archivo binario
pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close()
del (fichero_binario)

#recuperacion del los datos binarios
fichero=open("lista_nombres", "rb")
lista=pickle.load(fichero)
print(lista)


#serializar un objeto
class Vehiculo():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
	def arrancar(self):
		self.enmarcha=True
	def acelerar(self):
		self.acelera=True
	def frenar(self):
		self.frena=True
	def estado(self):
		print("Marca: ", self.marca, "\n Modelo: ", self.modelo, 
			"\n En marcha", self.enmarcha, "\n Acelerando: ", self.acelera,
			"\n Frenando: ", self.frena)
carro1=Vehiculo("Mazda","MX5")
carro2=Vehiculo("H%","mim")
carro3=Vehiculo("M&M","HAHAH")
coches=[carro1, carro2, carro3]
fichero=open("losCarros", "wb")
pickle.dump(coches, fichero)
fichero.close()
del (fichero)

ficheroApertura=open("losCarros", "rb")
misCarros=pickle.load(ficheroApertura)
ficheroApertura.close()
for c in misCarros:
	print(c.estado())