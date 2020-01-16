print ("Evaluacion de notas")

noteStudent=input("Introduce una nota: ")

def test(note):
	value = "Approved"
	if note<3:
		value="Suspended"
	value = "Approved"

print(test(int(noteStudent)))

print()

#################
print ("Verificar acceso")

ageUser= int(input("Introduce tu edad: "))

if ageUser<18:
	print ("No ingresar")
elif ageUser>100:
	print ('Error')
else:
	print ("Bienvenido")

#################
print()

print ("Devuelve el Maximo")

num1= int(input("Introduce el primer numero: "))
num2= int(input("Introduce el segundo numero: "))

def devMax(n1,n2):
	if num1 < num2 :
		print (n2)
	elif num2 < num1 :
		print (n1)
	else :
		print ("Son iguales")
print("El numero mas alto es: "); devMax(num1, num2)

#################
print()

print ("Guardar datos")

name=input("Ingrese su nombre: ")
address=input("Ingrese su direccion: ")
numPho=int(input("Ingrese su numero de telefono: "))

tupla = ['Nombre', "Direccion", "Numero Telefono"]
dictionary = {tupla[0]:name, tupla[1]:address, tupla[2]:numPho}

print (dictionary)

#################
print()

print ("Media aritmetica")

num1= int(input("Introduce el primer numero: "))
num2= int(input("Introduce el segundo numero: "))
num3= int(input("Introduce el tercer numero: "))

media = (num1+num2+num3)/3

print ("El promedio es : "); print (media)