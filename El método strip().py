# El método Strip() lo que hace es eliminar del principio y el final de la cadena los caracteres que vayan dentro de los paréntesis.
# Pero solo los del inicio y el final; el centro permanecerá igual.
cadena = "\tHola Ernesto \n"
print(cadena)

cadena = cadena.strip("s tHo\t\n")
print(cadena)