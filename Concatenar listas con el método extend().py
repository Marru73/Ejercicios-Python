# La sintaxis es: nombre_lista.extend(objeto_iterable)
# También podría ser: nombre_lista.extend(range(1,10)) ---> esto es un ejemplo.

invitados = ["Carolina", "Juan", "Gerardo"]
amigos = ["Luis", "Ana"]
print(f"Los invitados son: {invitados} y los amigos son: {amigos}")

invitados.extend(amigos)
print(f"\nLa lista final es: {invitados}")

numeros = [10, 20]
print(f"\nLista números: {numeros}")
numeros.extend(range(30, 100, 10))
print(f"Lista números: {numeros}")