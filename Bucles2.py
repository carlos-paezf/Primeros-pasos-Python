#Bucle while
i=1
while i<=10:
	print("Ejecucion: "+str(i))
	i=i+1
print("Fin de Ejecucion")

print("##################")

#ejercicio
age=int(input("Introduce tu edad: "))
while age<5 or age>100:
	print("Has introducido una edad no valida. Vuelve a intentarlo")
	age=int(input("Introduce tu edad: "))
print("Puedes pasar.")
print("Edad del aspirante-> "+str(age))

print("##################")

#Raiz Cuadrada
import math
print("Raiz Cuadrada")
numero=int(input("Introduce un numero: "))
intentos=0
while numero<0:
	print("No se puede halla la raiz cuadrada de un numero negativo")
	if intentos==2:
		print("Fin de intentos")
		break;
	numero=int(input("Introduce un numero: "))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de "+str(numero)+" es "+str(solucion))

print("##################")

#ignorar y continuar
letra=input("Ingrese una frase: ")
aux=0
for i in letra:
	print("Viendo la letra: "+i)
	if i==" ":
		continue
	aux+=1
print("Cantidad de caracteres sin espacio: "+str(aux))

print("##################")

#email
email=input("Introduce tu email: ")
for i in email:
	if i=="@":
		arroba=True
		break;
else:
	arroba=False
print(arroba)