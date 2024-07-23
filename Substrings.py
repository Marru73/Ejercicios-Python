# El Substring es una subcadena dentro de una cadena. Esta puede tener solo un caracter.
# Se escribe de la siguiente forma: variable[inicio : final : saltos]
# inicio --> Establece el índice donde se iniciará la subcadena
# final ---> Establece el índice donde se  terminará la subcadena
# saltos --> Establece el número de saltos que realizará el índice para generar la subcadena.
# Cuando utilicemos números negativos, la indexación empezará contando de derecha a izquierda.

string = "0123456789"
substring = ""

print (f"Cadena principal: {string}")

substring = string[0]
print (f"\nSubcadena con índice en la posción [0] es: {substring}")

substring = string[5]
print (f"\nSubcadena con índice en la posción [5] es: {substring}")

substring = string[-4]
print (f"\nSubcadena con índice en la posción [-4] es: {substring}")

substring = string[0:3]
print (f"\nSubcadena con índices en la posciones [0:3] es: {substring}")

substring = string[:3]
print (f"\nSubcadena con índices en la posciones [:3] es: {substring}")

substring = string[-4:-1]
print (f"\nSubcadena con índices en la posciones [-4:-1] es: {substring}")

substring = string[:]
print (f"\nSubcadena con índices en la posciones [:] es: {substring}")

substring = string[1:6:2]
print (f"\nSubcadena con índices en la posciones y salto [1:6:2] es: {substring}")

substring = string[::3]
print (f"\nSubcadena con índices en la posciones y salto [::3] es: {substring}")


