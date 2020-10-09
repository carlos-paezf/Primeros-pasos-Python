import phonenumbers

# Parseando el String a número de telefono
phone_number = phonenumbers.parse("+573112221234")

# Validando el numero de telefono
valid = phonenumbers.is_valid_number(phone_number)

# Comprobando la posibilidad de un numero
possible = phonenumbers.is_possible_number(phone_number)

# Imprimir la salida
print(valid)
print(possible)