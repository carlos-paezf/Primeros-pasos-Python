#Imprime hola, por cada elemento en la lista
for i in [1,2,3]:
	print("Hi")
#Imprime cada elemento de la lista
for i in [1,2,3]:
	print(i)
#Imprime cada elemento de la lista sin salto de linea, pero si con un espacio
for i in ["A","B"]:
	print(i, end=" ")
#Imprime algo por cada caracter del string recorrido
for i in "Hola":
	print("#$", end=" ")
#Veririficacion
print("###############")
email=False
mail=input("Introduce tu email: ")
for i in mail:
	if(i=="@"):
		email=True
if email:
	print("El email es correcto")
else:
	print("El email no es correcto")
#Veririficacion
print("###############")
email=False
mail=input("Introduce tu email: ")
aux=0
for i in mail:
	if(i=="@" or i=="."):
		aux=aux+1
if aux==2:
	print("El email es correcto")
else:
	print("El email no es correcto")
print("###############")

#bucle con tipo range -> Devuelve un tipo de array
for i in range(5):
	print(i, end=" ")
print("###############")

#unir textos con variables -> uso de f dentro del print
#range(inicio, final)
for i in range(4,8):
	print(f"Valor de la variable: {i}")
print("###############")

#range(inicio,final,intervalo)
for i in range(2,10,3):
	print(f"Valor de la variable: {i}")
print("###############")

#Validacion junto a len
val=False
email=input("Ingrese un email: ")
for i in range(len(email)):
	if email[i]=="@":
		val=True
if val:
	print("Email correcto")
else:
	print("Email incorrecto")