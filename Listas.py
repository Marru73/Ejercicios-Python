# En programación, las estructuras de datos son aquellas que nos permiten organizar la información de maneraeficiente, y así, diseñar alternativas de solución para un determinado problema.
# En Python, una de las estructuras de datos más sencilla que existe son las listas.
# Las listas, se utilizan para almacenar conjuntos de información, de esta manera, crear una colección de elementos ordenados, y a su vez, estos elementos pueden o no estar relacionados entre sí, es decir, 
# una lista puede ser homogénea o heterogénea.
# Lista heterogénea: Nos referimos a que todos los elementos que conforman la lista son de diferentes tipos de datos.
# Lista homogénea: Nos referimos a que todos los elementos que conforman la lista son del mismo tipo de datos.
# La sintaxis es la siguiente: lista = []

# lista_homogénea = ["Javier", "Carlos", "María"]
# lista_heterogénea = ["nombre", 2, 3.14, True]

print("Lista vacía")
lista_vacia = []

print(lista_vacia)

print("\nListas homogéneas")

vocales = ["a", "e", "i", "o", "u"]
print(vocales)

numeros_enteros = [1, 2, 3, 4, 5]
print(numeros_enteros)

numeros_decimales = [1.5, 2.2, 3.3, 4.9, 5.1]
print(numeros_decimales)

valores_booleanos = [True, False, False, True]
print(valores_booleanos)


print("\nListas heterogéneas")

datos = ["Carlos", 20, 1.70, True]
print(datos)
