# El método count() busca un caracter o una subcadena dentro de una cadena.
# Se escribe variable.count(substring, int, int). Puede utilizar 3 argumentos a la vez.
# El segundo argumento lo que hará es empezar en el carácter correspondiente al número que hayamos puesto en vez de empezar desde el principio.
# El tercer argumento indica en qué número de caracter va a terminar.

# Ejemplo 1
string = "La casa de Bernarda Alba"
print(string.count(""))

# Ejemplo 2

string = "mi mamá me mima"
contador = 0

print (string.center(40, "="))

contador = string.count("M")
print (f"\nLa letra M se encontró {contador} veces en la cadena: {string}")

contador = string.count("m")
print (f"\nLa letra m se encontró {contador} veces en la cadena: {string}")

contador = string.count("mamá")
print (f"\nLa palabra mamá se encontró {contador} veces en la cadena: {string}")

contador = string.count("me mima")
print (f"\nLa oración me mima se encontró {contador} veces en la cadena: {string}")

contador = string.count("ma")
print (f"\nLa palabra ma se encontró {contador} veces en la cadena: {string}")

contador = string.count("m", 13)
print (f"\nLa letra m se encontró {contador} veces, desde la posición 13 en la cadena: {string}")

contador = string.count("m", 100)
print (f"\nLa letra m se encontró {contador} veces, desde la posición 100 en la cadena: {string}")

contador = string.count("m", -3)
print (f"\nLa letra m se encontró {contador} veces, desde la posición -3 en la cadena: {string}")

contador = string.count("m", 3, 7)
print (f"\nLa letra m se encontró {contador} veces, desde la posición 3 hasta la posición 7 en la cadena: {string}")

contador = string.count("m", -4, -1)
print (f"\nLa letra m se encontró {contador} veces, desde la posición -4 hasta la posición -1 en la cadena: {string}")