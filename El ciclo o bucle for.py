# El ciclo o bucle "for", es una estructura de control que nos permite repetir un bloque de instrucciones (sentencias), cierta cantidad de veces
# la sintaxis es: for variable in objeto_iterable:
#   instrucción
#   instrucción
# Un "objeto iterable", es aquel que permite recorrer sus elementos uno a uno, como por ejemplo una cadena de caracteres.

string = "Hola"

for character in string:
    print(character)
print("El programa ha finalizado")