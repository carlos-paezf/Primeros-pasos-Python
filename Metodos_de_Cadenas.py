age=input("Introduce tu edad: ")
while (age.isdigit()==False):
	print ("Por favor introduce un valor numerico")
	age=input("Introduce tu edad: ")
if (int(age)<18):
	print("No tiene acceso")
else:
	print("Tiene acceso")


email=input("Introduce una direccion de correo electronico: ")
arroba=email.count("@")
if (arroba!=1 or email.rfind('@')==(len(email)-1 or email.find('@')==0)):
	print("Mail incorrecto")
else:
	print("Mail correcto")


miemail=input("Introduzca por favor su correo electronico: ")
#if email cuenta con 1 @ y la encuentra en una posicion diferente a 0 y diferente a la ultima posicion
if miemail.count("@")==1 and miemail.find("@")!=0 and miemail.find("@")!=len(miemail)-1:
 print("Su dirección de email es correcta")
else:
 print("Su dirección de email no es correcta")


email=input ("Digite su dirección de correo: ")
#if email cuenta con mas 1 @ o email empieza o termina con @ o el email no contiene ningun punto
if email.count("@")!=1 or email.startswith("@") or email.endswith("@") or email.count(".")==0:
    print ("Correo invalido")
else:
    print ("Correo Valido")