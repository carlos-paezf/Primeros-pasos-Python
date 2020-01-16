salario_presidente=int(input("Introduce salario de presidente: "))
print("Salario de presidente: " + str(salario_presidente))

salario_director=int(input("Introduce salario de director: "))
print("Salario de director: " + str(salario_director))

salario_jefe_area=int(input("Introduce salario de jefe de area: "))
print("Salario de jefe de area: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario de administrativo: "))
print("Salario de administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo correcto")
else:
	print("Revisa los salarios")

print()
print("####################################")
print("Funcion de AND y OR")

print("Programa de becas 2020")
dist_esc=int(input("Intruduce la distancia a tu escuela en km: "))
print(dist_esc)
num_her=int(input("Introduce la cantidad de hermanos: "))
print(num_her)
sal_fam=int(input("Intruduce el salario anual bruto: "))
print(sal_fam)

if dist_esc>40 and num_her>2 or sal_fam<=20000:
	print("Derecho a beca")
else:
	print("Sin derecho a beca")

print()
print("####################################")
print("Funcion de IN")

print("Carreras 2020")
print("Derecho-Sistemas-Medicina")
opcion=input("Escribe la carrera elegida: ")
asig=opcion.lower()

if asig in ("derecho", "sistemas", "medicina"):
	print("Carrera elegida "+asig)
else:
	print("Error")