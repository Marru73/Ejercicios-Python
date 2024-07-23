# La sintaxis es: nombre_variable.insert(). 
# Este método tiene que llevar dos argumentos. Uno será la posición donde queremos insertar el elemento y el otro será el elemento a insertar.
# Por tanto será: nombre_variable.insert(int, nuevo_elemento)

letras = ["b", "d", "f", "g"]
letras.insert(0, "a")
letras.insert(2, "c")
letras.insert(4, "e")
letras.insert(100, "z") # Al poner un número mayor de las posiciones que hay en la lista, el elemento se pondrá al final de la lista.
print(letras)