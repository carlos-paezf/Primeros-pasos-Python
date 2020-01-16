def suma(num1, num2):
	return num1+num2
def resta(num1, num2):
	return num1-num2
def multiplicacion(num1,num2):
	return num1*num2
def division(num1, num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print("Sintax Error ..... No se puede dividir por 0")
		return "Operacion erronea"

while True:
	try:
		op1=(int(input("Introduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))
		break
	except ValueError:
		print("Valor ingresado INCORRECTO")

operacion=input("Ingrese la operacion a realizar: (suma, resta, multiplicacion, division)")

if operacion.lower()=="suma":
	print(suma(op1,op2))
elif operacion.lower()=="resta":
	print(resta(op1,op2))
elif operacion.lower()=="multiplicacion":
	print(multiplicacion(op1,op2))
elif operacion.lower()=="division":
	print(division(op1,op2))
else:
	print("Operacion no contemplada")

print("Operacion ejecutada...")