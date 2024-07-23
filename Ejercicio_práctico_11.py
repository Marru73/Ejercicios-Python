lista = ["A", "B", "b", "c", "E", "E", "f"]
print(f" Las letras que componen las lista son: {lista}")

letra_eliminar = input("introduce la letra que deseas eliminar: ")


for caracter in lista:
    if letra_eliminar.lower() in lista:
        lista.remove(letra_eliminar.lower())
    elif letra_eliminar.upper() in lista:
        lista.remove(letra_eliminar.upper())    
        
print(lista)
