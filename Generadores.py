#Funcion tradicional -> genera la lista inmediata
def pares(lim):
	num=1
	myList=[]
	while num<lim:
		myList.append(num*2)
		num+=1
	return myList
print(pares(10))

print("###############")

#Generador -> genera un objeto iterable almacenando de uno en uno
def par(lim):
	num=1
	while num<lim:
		yield num*2
		num+=1
pares=par(10)
for i in pares:
	print(i)

print("###############")

#Devolver valor a valor
#Entre llamada y llamada se ahorran recursos
def par2(lim):
	num=1
	while num<lim:
		yield num*2
		num+=1
pares=par2(10)
print(next(pares))
print("Aqui puede ir mas codigo")
print(next(pares))
print("Aqui puede ir mas codigo")
print(next(pares))

print("###############")

#yield from
#(*argumento_de_la_funcion)->recibe un numero indeterminado de elementos
##->los recibe en tupla
print("Elementos generales")
def ciudad(*ciudad):
	for elem in ciudad:
		yield elem
ciudades_devueltas=ciudad("Bogota","Cali","Manizales","Bucaramanga")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

print("###############")

print("""Semejanda a blucles anidados
	acceso a sub-elementos""")
def ciudades(*ciudades):
	for elem in ciudades:
		for subElem in elem:
			yield subElem
ciudades_devueltas=ciudades("Bogota","Cali","Manizales","Bucaramanga")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

print("###############")

print("""Uso de yield from
	acceso a sub-elementos""")
def citys(*citys):
	for elem in citys:
		yield from elem
ciudades_devueltas=citys("Bogota","Cali","Manizales","Bucaramanga")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))