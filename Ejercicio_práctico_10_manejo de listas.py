lista = []
contador = 0
numeros_total = int(input("¿Cuántos números contendrá la lista?: "))
while contador <= numeros_total:
    contador += 1
    if contador != numeros_total:
        numero_int = int(input("Introduce un número entero: "))
        lista.append(numero_int)
print(f"Los número que componen la lista son: {lista} \nY la suma total es: {sum(lista)}")