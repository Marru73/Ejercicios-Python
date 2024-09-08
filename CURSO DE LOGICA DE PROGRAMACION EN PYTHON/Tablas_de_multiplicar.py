# Mostrar las tablas de multiplicar del 1 al 30, en formato horizontal, con ceros delante de n si es menor a 10
print()
for i in range(1, 100):
    for n in range(1, 11):
        print(f"{str(n).zfill(2)} x {str(i).zfill(2)} = {str(n*i).zfill(2)}", end='\t')  # str(n).zfill(2) añade el 0 si n < 10
    print()  # Hacemos un salto de línea después de cada tabla
