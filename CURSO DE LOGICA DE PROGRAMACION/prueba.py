import os
file_name = "Ventas.txt"

open(file_name, "a")
while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Seleccione una opción: ")
    
    if option == 1:
        name = input("Nombre:")
        quantity = input("Cantidad:")
        price = input("Precio:")

        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}")
    
    elif option == 2: 
        name = input("Producto a consultar: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
