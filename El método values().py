# Este método devuelve todos los valores dentro de un diccionario.
# Su sintaxis es: nombre_diccionario.values()

dictionary = {   "a": 1,
                "b": 2,
                "c": 3
            }

print(dictionary)

print(f"\nLos valores del diccionario son: \n{dictionary.values()} ")

print("\nConvirtiendo los valores a lista usando el constructor list()")
list_values = list(dictionary.values())

print(f"La lista es: {list_values}")
print(f"Posición 1 de la lista values: {list_values[1]}")