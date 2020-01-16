MORSE = {' ':'_', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 
'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 
'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 
'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 
'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',}

def convertirAMorse(frase):
	frase = frase.upper()
	fraseCodificada = ""
	for caracter in frase :
		fraseCodificada += MORSE[caracter]+" "
	return fraseCodificada

print("Frase inscrita en el codigo->")
frase = "hi world"
print(convertirAMorse(frase) + " Traduccion -> " +frase)

print()
print("Solicitar la frase->")
frase = input("Frase a Convertir: ")
print(convertirAMorse(frase) + " Traduccion -> " +frase)
