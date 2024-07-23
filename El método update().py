# La sintaxis es: dict_name.update(dictionary)

dict_name = {   "a": 1,
                "b": 2,
                "c": 3
            }

print(f"El diccionario original es: {dict_name}")

dict_name.update({"z": 4, "d": 5})
print(f"Agregando 'z' y 'd': {dict_name}")

dict_name.update({"a": 6, "b": 5})
print(f"Actualizando 'a' y 'b': {dict_name}")