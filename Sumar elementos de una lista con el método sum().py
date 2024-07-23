# La sintaxis es: sum(objeto_iterable, valor_inicial)

numeros = [1, 2, 3]
print(sum(numeros))

numeros = [1, 2, 3]
print(f"\Con valor inicial: 10 \n{numeros}") 
print(sum(numeros, 10)) # En este caso, lo que hace es añadir 10 a la suma de la lista. Este número puede ser negativo también.

numeros = [1, 2, 3]
print(f"\Con valor inicial: -2\n{numeros}") 
print(sum(numeros, -2))

numeros = [1, 2.5, True]
print(f"\n{numeros}")
print(sum(numeros))

lista = [1, 2, "a"]
print(sum(lista)) # En este caso nos dará un error al mezclar números int con str.