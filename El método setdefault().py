# La sintaxis es: dict_name.setdefault(key, value). Puede trabajar con un solo argumento, aunque se aconseja usar sus dos argumentos.

fruits = {  "manzana": 2,
            "banana": 3,
            "naranja": 1
            }

print(f"{fruits} \n")

# Intentamos agregar una clave que ya existe en el diccionario.
return_value = fruits.setdefault("banana", 4) # En este caso no retornaría el 4 ya que en el diccionario "banana" tiene el valor 3, por consiguiente, retornará el valor 3.
print(f"El valor retornado de ('banana', 4) es: {return_value}")
print(f"El diccionario actualizado es: {fruits} \n")


# Intentamos agregar una clave que no existe ene el diccionario sin valor.
return_value = fruits.setdefault("kiwi")
print(f"El valor retornado de ('kiwi') es: {return_value}")
print(f"El diccionario actualizado es: {fruits} \n")


# Intentamos agregar una clave que no existe en el diccionario con valor.
return_value = fruits.setdefault("mango", 5)
print(f"El valor retornado de ('mango') es: {return_value}")
print(f"El diccionario actualizado es: {fruits} \n")
