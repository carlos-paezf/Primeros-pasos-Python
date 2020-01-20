class Vehicle():

	def __init__(self, typeVehicle, trademark, model):
		self.typeVehicle=typeVehicle
		self.trademark=trademark
		self.model=model
		self.movement=False
		self.accelerate=False
		self.brake=False

	def star(self):
		self.movement=True
	def accelerate(self):
		self.accelerate=True
	def brake(self):
		self.brake=True
	def status(self):
		print(
			"\nTipo: ",self.typeVehicle,
			"\nMarca: ",self.trademark, 
			"\nModelo: ",self.model,
			"\nMovimiento: ",self.movement,
			"\nAcelerar: ",self.accelerate,
			"\nFrenar: ",self.brake)


class Motorcycle(Vehicle):

	maneuver=""
	def maneuver(self):
		self.maneuver="Maniobra -> Caballito"
	#Sobreescritura de metodos
	def status(self):
		print(
			"\nTipo: ",self.typeVehicle,
			"\nMarca: ",self.trademark, 
			"\nModelo: ",self.model,
			"\nMovimiento: ",self.movement,
			"\nAcelerar: ",self.accelerate,
			"\nFrenar: ",self.brake,
			"\n",self.maneuver)


class Van(Vehicle):

	def load(self, load):
		self.load=load
		if(self.load):
			return "La Furgoneta esta cargada"
		else:
			return "La Furgoneta no esta cargada"


class VehElectrics(Vehicle):

	def __init__(self, typeVehicle, trademark, model):
		super().__init__(typeVehicle, trademark, model)
		self.autonomy=100

	def chargeEnergy(self):
		self.charge=True

	def status(self):
		print(
			"\nTipo: ",self.typeVehicle,
			"\nMarca: ",self.trademark, 
			"\nModelo: ",self.model,
			"\nMovimiento: ",self.movement,
			"\nAcelerar: ",self.accelerate,
			"\nFrenar: ",self.brake,
			"\nAutonomia",self.autonomy)


class BicycleElectrics(VehElectrics,Vehicle):
	pass
