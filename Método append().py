# append() nos permite agregar nuevos elementos al final de una lista.
# La sintaxis es: nombre_lista.apeend(nuevo_elemento)

print("Agregando un elemento a la lista")
letras = ["a", "b", "c", "d"]
print(f"Lista: {letras}")
letras.append("e")
print(f"Lista: {letras}")

print("Agregando tres elementos a la lista")
letras = ["a", "b", "c", "d"]
print(f"Lista: {letras}")
letras.append("e")
letras.append("f")
letras.append("g")
print(f"Lista: {letras}")

print("Agregando tres elementos de distinto tipo de datos a la lista")
letras = ["a", "b", "c", "d"]
print(f"Lista: {letras}")
letras.append(5)
letras.append(2.5)
letras.append(True)
print(f"Lista: {letras}")