class Person():

	def __init__(self, name, age, resident):
		self.name=name
		self.age=age
		self.resident=resident

	def description(self):
		print(
			"Nombre: ",self.name,
			"\nEdad: ",self.age,
			"\nLugar de residencia: ",self.resident)


class Employee(Person):

	def __init__(self, salary, antiquity, name_employee, age_employee, resident_employee):
		super().__init__(name_employee, age_employee, resident_employee)
		self.salary=salary
		self.antiquity=antiquity

	def description(self):
		super().description()
		print(
			"Salario: ", self.salary,
			"\nAntigüedad: ",self.antiquity)


Charles=Employee(1500,20,"Charles",20,"Colombia")
Charles.description()
print("Es instancia Charles de empleado? ",isinstance(Charles,Employee))
print("Es instancia Charles de persona? ",isinstance(Charles,Person),"\n")

David=Person("David",20,"Colombia")
David.description()
print("Es instancia David de empleado? ",isinstance(David,Employee))
print("Es instancia David de persona? ",isinstance(David,Person),"\n")