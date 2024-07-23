# Este métdo devuelve todos los items dentro de un diccionario.
# Su sintaxis es: nombre_diccionario.items()

dictionary = {  "a": 1,
                "b": 2,
                "c": 3
            }

print(dictionary)
print(f"\nLos items del diccionario son:\n{dictionary.items()}")

print("\nConvirtiendo items a lista utilizando el constructor list()")

list_items = list(dictionary.items())

print(f"La lista es: {list_items}")
print(f"Posición 1 de la lista items: {list_items [1]}")