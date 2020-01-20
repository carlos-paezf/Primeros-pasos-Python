from io import open

#Ingreso de texto
archivo_texto=open("archivo.txt","w")
frase="Manejo de archivos en Pyhton \n Hi world"
archivo_texto.write(frase)	
archivo_texto.close()

#Lectura del texto
archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read()
archivo_texto.close()
print(texto)

#Lectura del texto linea a linea y almacenarlo en una lista
archivo_texto=open("archivo.txt","r")
lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto)
print(lineas_texto[1])

#Metodo Append
archivo_texto=open("archivo.txt","a")
archivo_texto.write("\n 1234567890")
archivo_texto.close()
archivo_texto=open("archivo.txt","r")
lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto)


#Ubicacion del puntero
archivo_texto=open("archivo.txt","r")
print(archivo_texto.read())
archivo_texto.seek(11)
print(archivo_texto.read())
archivo_texto.seek(0) #leer desde n caracter
print(archivo_texto.read(11)) #Leer hasta n caracter
archivo_texto.close()

archivo_texto=open("archivo.txt","r+")
archivo_texto.write("\n 1234567890")
print(archivo_texto.read())