class Car():

	def displacement(self):
		print("Comportamiento-> Desplazamiento en 4 ruedas")


class MotorCycle():

	def diplacement(self):
		print("Comportamiento-> Desplazamiento en 2 ruedas")


class Truck():

	def displacement(self):
		print("Comportamiento-> Desplazamiento en 6 ruedas")

#Funcion para el polimorfismo
def displacementVehicle(vehicle):
	vehicle.displacement()

myVehicle=Truck()
displacementVehicle(myVehicle)