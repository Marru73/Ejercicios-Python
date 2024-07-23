# A diferencia del método strip(), lo que hace rstrip() y lstrip() es eliminar los caracteres solo de la derecha de la cadena si es rstrip() o de la izquierda si es lstrip().

# Método rstrip()

cadena = "\tHola Ernesto\n"
print(cadena)

cadena = cadena.rstrip("s tHo\t\n")
print(cadena)

# Método lstrip()

cadena = "\tHola Ernesto\n"
print(cadena)

cadena = cadena.lstrip("s tHo\t\n")
print(cadena)
