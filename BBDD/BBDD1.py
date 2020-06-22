import sqlite3

miConexion=sqlite3.connect("BBDD1")	#Para observar la base de datos SQLite, usar un visor
miCursor=miConexion.cursor()

miCursor.execute("CREATE TABLE PRODUCTS (item_name VARCHAR(50), price INTEGER, section VARCHAR(20))")
		#Luego de crear la tabla, se debe documentar la linea anterior
miCursor.execute("INSERT INTO PRODUCTS VALUES('Balon', '12345', 'Deportes')")
variosProductos=[
	("Camiseta", 1000, "Deportes"),
	("Jarron", 90000, "Ceramica"),
	("Celular", 2000, "Tecnologia")
]
miCursor.executemany("INSERT INTO PRODUCTS VALUES(?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTS")
verProductos=miCursor.fetchall()
for producto in verProductos:
	print("Nombre Articulo: ", producto[0], 
		" Precio: ", producto[1], 
		" Seccion: ", producto[2])

miConexion.commit()


miCursor.close()
miConexion.close()