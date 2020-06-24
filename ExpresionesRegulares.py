#------------https://docs.python.org/3/howto/regex.html

import re

cadena="Expresiones REGULARES en python. Primeros pasos en python"

print(re.search("Expresiones", cadena))

textoBuscar="python"
if re.search(textoBuscar, cadena) is not None:
	print("Se ha encontrado 1 coincidencia")
else:
	print("No existen coincidencias")

textoEncontrado=re.search(textoBuscar, cadena)
print(textoEncontrado.start()) #<--- Numero de caracter donde inicia la coincidencia
print(textoEncontrado.end()) #<----Caracter donde finaliza
print(textoEncontrado.span()) #<---Tupla del caracter donde inicia y finaliza
print(re.findall(textoBuscar, cadena))
print(len(re.findall(textoBuscar, cadena)))



#----------------Filtrado y rango---------------
lista_nombre=["Carlos", 
				"Paez", 
				"David", 
				"Ferrer", 
				"Laura", 
				"Dayana",
				"Juan", 
				"Villamizar",
				"David", 
				"Traslaviña"]
for elemento in lista_nombre:
	if re.findall('^Ju', elemento): #<---- Busca lo que inician por ...
		print(elemento)
print()
for elemento in lista_nombre:
	if re.findall('er$', elemento): #<----- Busca los que finalizan por ...
		print(elemento)
print()
for elemento in lista_nombre:
	if re.findall('[yñ]', elemento):
		print(elemento)
print()
for elemento in lista_nombre:
	if re.findall('[D-G]', elemento): #<---- rango establecio en [], tambien se puede usar los comodines ^ y $
		print(elemento)
print()

lista_codigos=["Ma1", "Se1", 
				"Ma.2", "Ba1", 
				"Ma3", "Va1", 
				"Va:2", "Ma,4", 
				"Ma:A", "MaC"]
for elemento in lista_codigos:
	if re.findall('Ma[0-3]', elemento):
		print(elemento)
print()
for elemento in lista_codigos:
	if re.findall('Ma[^0-3]', elemento): #<---- Negacion del rango
		print(elemento)
print()
for elemento in lista_codigos:
	if re.findall('Ma[0-3A-C]', elemento):
		print(elemento)
print()
for elemento in lista_codigos:
	if re.findall('Ma[.,:]', elemento):
		print(elemento)
print()



#----------------Match y search
cadena1="Carlos Paez"
cadena2="123456"
cadena3="s45fw4b5"
cadena4="David Ferrer Arturo Marin"

if re.match(".arlos", cadena1, re.IGNORECASE):
	print("Hemos encontrado el nombre")
else:
	print("No se han encontrado coincidencias")

if re.match("\d", cadena2):
	print("Se han encontrado coincidencias")
else:
	print("No hay coincidencias")

if re.search("Ferrer", cadena4, re.IGNORECASE):
	print("Si hay un resultado")
else:
	print("No hay resultado")