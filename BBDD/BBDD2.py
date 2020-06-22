import sqlite3

miConexion=sqlite3.connect("BBDD2")
miCursor=miConexion.cursor()

#Crear tabla producto con una llave primaria
miCursor.execute('''
	CREATE TABLE PRODUCTS (
	item_code VARCHAR(4) PRIMARY KEY,
	item_name VARCHAR(50),
	price INTEGER,
	section VARCHAR(20)
	)
''') 
productos=[
	("AR01", "Balon", 1000, "Juguetes"),
	("AR02", "Caña de Pesca", 1001, "Pasatiempos"),
	("AR03", "Jarron", 9000, "Ceramica"),
	("AR--", "-----", 0000, "-----")
]
#Insertar varios elementos por medio de una tupla
miCursor.executemany("INSERT INTO PRODUCTS VALUES(?,?,?,?)", productos)
for producto in productos:
	print(producto)
print("-----------------------------------")

#Eliminar elementos de la tabla
miCursor.execute("DELETE FROM PRODUCTS WHERE item_code='AR--'")
miCursor.execute("SELECT * FROM PRODUCTS")
verProductos=miCursor.fetchall()
for producto in verProductos:
	print(producto)
print("-----------------------------------------")

#Crear tabla con una llave autoincremental y un elemento de valor unico y agregar elementos
miCursor.execute('''
	CREATE TABLE CLIENTS (
	id_client INTEGER PRIMARY kEY AUTOINCREMENT,
	document INTEGER UNIQUE,
	name_client VARCHAR(50), 
	address VARCHAR(50)
	)
''')
clientes=[
	(1234, "Carlos Paez", "Calle falsa 123"),
	(4321, "David Ferrer", "Calle Falsa 321"),
	(4132, "Arturo Marin", "Calle Falsa 132")
]
miCursor.executemany("INSERT INTO CLIENTS VALUES(NULL,?,?,?)", clientes)
for cliente in clientes:
	print(cliente)
print("------------------------------------------")

#Mostrar elementos segun la caracteristica comun
miCursor.execute("SELECT * FROM CLIENTS WHERE address='Calle falsa 123'")
verClientes=miCursor.fetchall()
print(verClientes)
print("------------------------------------------")

#Modificar un elemento
miCursor.execute("UPDATE CLIENTS SET address='Calle Falsa 123, Correccion' WHERE id_client=1")
miCursor.execute("SELECT * FROM CLIENTS")
verClientes=miCursor.fetchall()
for cliente in verClientes:
	print(cliente)
print("---------------------------------")


miConexion.commit()

miCursor.close()
miConexion.close()