# El método popitem() se utiliza para eliminar y devolver el último par clave-valor agregado a un diccionario.
# Su sintaxis es: dict_name.popitem()
# Es recomentdable guardar este elemento que se va a borrar en una variable, por lo que su sintaxis ahora será: item = dict_name.popitem().

dictionary = {  "a": 1,
                "b": 2,
                "c": 3
                }

print(dictionary)

item = dictionary.popitem()
print(f"El item eliminado es: {item}")

print(dictionary)