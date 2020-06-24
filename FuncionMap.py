class Persona:
	def __init__(self, nombre, edad, salario):
		self.nombre=nombre
		self.edad=edad
		self.salario=salario
	def __str__(self):
		return "La persona {} tiene {} años de edad y tiene un salario de ${}".format(self.nombre, self.edad, self.salario)
listaPersonas=[
Persona("Carlos", 19, 1000),
Persona("Arturo", 66, 5000),
Persona("Laura", 18, 900),
Persona("Silvia", 56, 3500)
]

def comision_salario(persona):
	if(persona.edad>=50):
		persona.salario=persona.salario*1.19
	return persona

listaPersonasSalario=map(comision_salario, listaPersonas)
for persona in listaPersonasSalario:
	print(persona)