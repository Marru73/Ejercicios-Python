# Con del podemos eliminar una lista completa como también podemos eliminar solo elementos de la misma.
# La sintaxis es: del nombre_lista [posición]

# Eliminar solo un elemento de la lista:

vocales = ["a", "e", "i", "o", "u"]
del vocales [3]
print(vocales)

# Eliminar varios elementos incluídos en un rango:

vocales = ["a", "e", "i", "o", "u"]
del vocales [0:2]
print(vocales)

# Para borrar toda la lista hay dos formas:

vocales = ["a", "e", "i", "o", "u"]
del vocales [:]
print(vocales)

vocales = ["a", "e", "i", "o", "u"]
del vocales

# Con esta opción podemos borrar los elementos de una lista con un rango de 2, es decir, eliminará los elementos saltando de dos en dos.

vocales = ["a", "e", "i", "o", "u"]
del vocales [: : 2]
print(vocales)