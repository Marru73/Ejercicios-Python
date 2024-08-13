import os
"""file_name = "Marru.txt"
with open(file_name, "w") as file:
    file.write("Fran\n")
    file.write("51\n")
    file.write("Python")

with open(file_name, "r") as file:
    file.read()
    print(file.read())

os.remove(file_name)"""

file_name = "Ventas.txt"

with open(file_name, "a") as file:
    while True:
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Borrar producto")
        print("5. Mostrar productos")
        print("6. Calcular venta total")
        print("7. Calcular venta por producto")
        print("8. Salir")

        option = input("Selecciona una opción: ")

        if option == 1:
            name = input("Introduce el nombre: ")
            quentity = input("Introduce la cantidad: ")
            price = input("Introduce el precio: ")

        elif option == 2:
            name = input("Introduce el nombre a consultar: ")
            with open(file_name, "r") as file:
                file.read()
                print(file.read())



  