numeros = [1, 2, 3, 4, 5]
original = [1, 2, 3, 4, 5]
numeros.pop()
numeros.pop(0)
print(f"La lista original era: {original}")
print(f"La lista con los números eliminados es: {numeros}")
del original[1:-1]
print(f"Los números eliminados han sido: {original}")

# Así lo he hecho yo 

numeros = [1, 2, 3, 4, 5]
print (f"Lista números: {numeros}")

numeros_eliminados = []
numeros_eliminados.append(numeros.pop(0))
numeros_eliminados.append(numeros.pop())
print(f"Lista números: {numeros} \nLista números eliminados: {numeros_eliminados}")

# Esta es la solución del curso.