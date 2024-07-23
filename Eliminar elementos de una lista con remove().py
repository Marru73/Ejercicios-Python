# En Python, al trabajar con listas, es polible eliminar un elemento, especificando el elemto a eliminar, a diferencia del método pop(), donde tenemos que especificar la posición exacta dentro de la lista, para poder eliminar dicho elemento.
# Su sintaxis es la siguiente: nombre_lista.remove(elemento a eliminar).

vocales = ["a", "e", "i", "o", "u"]
vocales.remove("i")
print(vocales) 

# El método remove() solo eliminaría un elemento de la lista. Para eliminar más elementos iguales, tendría que estar incluído en un bucle for o while.

character = ""
contador = 0

vocales = ["a", "e", "i", "i", "u"]

while contador != len(vocales):
    contador += 1
    for character in vocales:
        if character == "i":
            vocales.remove("i")
print(vocales, end="")