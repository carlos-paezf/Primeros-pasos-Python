import phonenumbers
from phonenumbers import geocoder, carrier

# Parseando String a numero de telefono
phoneNumber = phonenumbers.parse("+573143282831")

# Obtener el proveedor del numero
Carrier = carrier.name_for_number(phoneNumber, 'en')

# Obteniendo informacion regional
Region = geocoder.description_for_number(phoneNumber, 'en')

# Imprimiendo el propietario y la region del numero
print(f"| Country | Supplier |\n|--------------------|\n| {Region} | {Carrier} |")