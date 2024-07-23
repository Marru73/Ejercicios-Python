# Pues como su nombre indica, lo que hará es justificar el texto al centro, izquiera o derecha.
# Se escribirá variable.center(). Dentro de los paréntesis deberá ir un número entero y tendrá que ser mayor que la longitud del string.
# Podrá llevar dentro de los paréntesis dos argumentos. Por ejemplo center(10, "=")

# center()

string = "menú"
string = string.center(10)
print(string)

string = "menú"
string = string.center(10, "=")
print(string)

# ljust()

string = "menú"
string = string.ljust(10, "=")
print(string)

# rjust()

string = "menú"
string = string.rjust(10, "=")
print(string)
