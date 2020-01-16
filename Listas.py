myList = ["wssp", "fb", "inst", "pint", "youtube", "gmail"]

#Imprimir toda la lista
print (myList[:])

#Imprimir la posicion solicitada
print (myList[2]) 

#Imprimir la posicion solitada, haciendo el conteo en reversa
print (myList[-2])

#Acceder a una porcion de la lista con punto de inicio a punto final
print (myList[2:4])
#Acceder a una porcion de la lista desde el inicio de la lista hasta un punto determinado
print (myList[:3])
#Acceder a una porcion de la lista desde un punto determinado hasta el final
print (myList[2:])

#Agregar elemento al final de la lista
myList.append("Twitter")
print (myList[:])
#Agregar elemento en una posicion especifica
myList.insert(2,"Hi5")
print (myList[:])
#Agregar varios elementos -> similar a concatenar
myList.extend(["Boostrap", "Laravel", "Fonts"])
print (myList[:])

#Retornar el indice
print (myList.index("Boostrap"))

#Comprobar si un elemento se encuentra o no
print ("wssp" in myList)
print ("mail" in myList)

#Las listas puedes guardar varios tipos de elementos
list2 = ["wssp", 5, True, 33.33]
print (list2[2])

#Remover elemento
myList.remove("Hi5")
print (myList[:])
list2.remove(True)
print (list2[:])

#Remover el ultimo elemento de una lista
myList.pop()
print (myList[:])

#Concatenar las listas
list3 = myList+list2
print(list3[:])