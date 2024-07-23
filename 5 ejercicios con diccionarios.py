# Ejercicio 1: Según el diccionario dado, imprime el número de manzanas que tienes en el mismo:
fruits = {  "manzanas": 5,
            "peras": 2,
            "naranjas": 4
            }

print(fruits)
print(f"El número de manzanas es: {fruits['manzanas']}")

# Ejercicio 2: El programa deberá agregar tres nuevos ítems al diccionario con las siguientes especificaciones: "bananas": 5, "mangos": 6, "uvas": 3

fruits.update({"bananas" : 5, "mangos" : 6, "uvas" : 3})
print(f"El nuevo diccionario es: {fruits}")

# Ejercicio 3: El programa deberá eliminar el par clave-valor correspondiente a la clave "peras".

fruits = {  "manzanas": 5,
            "peras": 2,
            "naranjas": 4
            }
print(fruits)

fruits.pop("peras")
print(f"El diccionario queda ahora de la sigiente forma: {fruits}")


# Ejercicio 4: El programa deberá retornar dos listas: la primera lista deberá contener todas las claves del diccionario y la segunda deberá contener todos los valores del diccionario.

fruits = {  "manzanas": 5,
            "peras": 2,
            "naranjas": 4
            }
print(fruits)

keys_list = list(fruits.keys())
print (f"Lista de claves: {keys_list}")

values_list = list(fruits.values())
print (f"Lista de valores: {values_list}")


# Ejercicio 5: El programa deberá retornar True si la clave "manzanas" existe en el diccionario y False si la clave no existe.

fruits = {  "manzanas": 5,
            "peras": 2,
            "naranjas": 4
            }
print(fruits)

if "manzanas" in fruits:
    print(True)
else:
    print(False)