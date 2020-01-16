myDictionary = {"Alemania" : "Berlin", "Francia" : "Paris", 
"Colombia" : "Bogota"}

#Diccionario entero
print (myDictionary)

#Elemento especifico del elemento, usanso su clave
print (myDictionary["Colombia"])

#Agregar elemento (Error voluntario)
myDictionary["Italia"] = "Cali"
print (myDictionary)

#Modificar valor erroneo en una clave
myDictionary["Italia"] = "Roma"
print (myDictionary)

#Eliminar elemento
del myDictionary["Italia"]
print (myDictionary)

dictionary2 = {"PC":"HP", 1:"Michel Jordan", "Mosqueteros":3}
print (dictionary2)

#Asociar una tupla con un diccionario, asignandoles a las claves valores
myTupla = ["Colombia", "Francia", "Italia", "Alemania"]
dicc = {myTupla[0]:"Bogota", myTupla[1]:"Paris", myTupla[2]:"Roma", myTupla[3]:"Berlin"}
print (dicc)

#Diccionario que almacene una tupla de valores dentro de otro diccionario
dictionary3 = {1:"Michel Jordan", "Nombre":"Michel", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print (dictionary3["Anillos"])

#Mirar las claves
print (myDictionary.keys())

#Mirar los valores dentro de las claves
print (dictionary2.values())

#Longitud del diccionario
print (len(dictionary3))