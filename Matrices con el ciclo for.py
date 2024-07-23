matrix = [  [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]]

# Modo 1 con ciclo for

for row in matrix:
    print(row)

# Modo 2 con ciclos anidados. Esto creará la matriz sin los corchetes.

for row in matrix:
    for element in row:
        print(element, end=" ")

    print()