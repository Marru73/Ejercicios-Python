# Su sintalis es: diccionario[clave] = nuevo valor

dictionary = {  "a": 1,
                "b": 2,
                "c": 3
            }
print(f"Diccionario original: {dictionary}")

print("\nCambiando el valor de 'a' por 0")
dictionary["a"] = 0
print(f"\nEl resultado del nuevo diccionario es:\n{dictionary}")   

# Para añadir un nuevo elemento, usamos el mismo método ya que si no se encuentra en el diccionario éste lo agregará. 

dictionary["d"] = 4

print(f"El nuevo diccionario es: {dictionary}")