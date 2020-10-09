import pafy

url = ''
video = pafy.new(url)

# Obteniendo todos los streams viables
streams = video.streams
# Imprimir todas os streams viables
for i in streams:
	print(i)

# Obtener las los formatos de mejores resolucion
best = video.getbest()

print(best.resolution, best.extension)

# Descargar el video
best.download()
print('Descarga de video exitosa')