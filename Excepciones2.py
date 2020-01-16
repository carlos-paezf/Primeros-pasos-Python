def division():
	while True:
		try:
			op1=(float(input("Introduce el primer numero: ")))
			op2=(float(input("Introduce el segundo numero: ")))
			print("La division es: "+str(op1/op2))
			break;
		except ValueError:
			print("Valor introducido INCORRECTO")
		except ZeroDivisionError:
			print("No se puede dividir entre 0")
		finally:
			print("Calculo finalizado")
division()
print()
print("######################3")

#Lanzar nuestas propias excepciones personalizadas
def edad(edad):
	if edad<0:
		raise TypeError("Edad negativa -> ERROR")

	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return "Eres maduro"
	elif edad<100:
		return "Cuidate..."
print(edad(20))
print()
print("######################3")

#Ejercicio
import math
def raiz(num1):
	if num1<0:
		raise ValueError("Numero negativo -> ERROR")
	else:
		return math.sqrt(num1)
op1=(int(input("Introduce un numero: ")))
try:
	print(raiz(op1))
except ValueError as NumNegativo:
	print(NumNegativo)
print()
print("#######################")