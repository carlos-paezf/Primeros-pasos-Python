def numero_par(num):
	if num % 2 == 0:
		return True

numeros={17,24,7,39,8,51,92}
print(list(filter(numero_par, numeros)))

print(list(filter(lambda num_par:num_par%2==0, numeros)))


class Empleados:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
	def __str__(self):
		return "{} que trabaja como {}, con un salario de ${}".format(self.nombre, self.cargo, self.salario)
listaEmpleados=[
Empleados("Juan", "Director", 12345),
Empleados("Pedro", "Presidente", 5432),
Empleados("Antonio", "Administrativo", 1234),
Empleados("Ana", "Secretaria", 432)
]
salarios_altos=filter(lambda empleado:empleado.salario>5000, listaEmpleados)
for emp_salario in salarios_altos:
	print(emp_salario)