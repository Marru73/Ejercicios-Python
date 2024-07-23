# Su sintaxis será: nombre_diccionario = {key: elemento, key: elemento} 
# Existen dos tipos de diccionarios: Homogéneo y Heterogéneo.
# En el Homogéneo todos sus datos son de mismo tipo de dato. 
# En el Heterogéneo sus datos son de distintos  tipos de datos.

# Diccionario vació:
dictionary_empty = {}

print (f"Diccionario vacío: {dictionary_empty}")

print()

# Diccionario homogéneo:
dictionary_age = { "Juan": 32,
                "Gerardo": 21,
                "Luis": 25
                }

print(f"Diccionario de edades: {dictionary_age}")

print()

# Diccionario heterogéneo:
dictionary_dates = {"name": "Brenda",
                    "Last_name": "Flores",
                    "age": 22
                    }

print(f"Diccionario de edades: {dictionary_dates}")

print()

# Diccionario para almacenar listas y diccionarios:
dictionary_list = { "a": {"a": 1},
                    "b": [0, 1, 2]
                    }

print(f"Diccionario con lista y diccionario: {dictionary_list}")

print()

# Un diccionario puede tener claves numéricas
dictionary_keys_num = { 4: 1,
                        5: 2,
                        6: 3
                        }

print(f"Diccionario con claves numéricas {dictionary_keys_num}")

print()

# Un diccionario no puede tener claves repetidas
dictionary_repeated_keys = {"Juan": 20,
                            "Gerardo": 30,
                            "Juan": 15
                            }

print(f"Diccionario con claves repetidas: {dictionary_repeated_keys}")

print()

# Un diccionario puede tener claves numéricas o de tipo texto
dictionary = {  1: 23,
                "Juan": 5,
                -2: "hola"
                }

print(f"Diccionario con claves de distintos tipos de dato: {dictionary}")
