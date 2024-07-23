# Ejercicio Práctico 1

print("""Estos son sus departamentos:

        1.- Atención al cliente
        2.- logística
        3.- Gerencia \n""")

nombre = input("Introduce tu nombre: ")
clave = int(input("Introduce el número de departamento: "))
año = float(input("Introduce el número de años de antigüedad: "))

if clave == 1:
    if año == 1 and año <2:
        print("A", nombre, "le corresponden 6 días de vacaciones")
    elif año >= 2 and  año <= 6:
        print("A", nombre, "le corresponden 14 días de vacaciones")
    elif año >= 7:
        print("A", nombre, "le corresponden 20 días de vacaciones")
    else:
        print("A", nombre, "No le corresponden días de vacaciones")

        

elif clave == 2:
    if año == 1 and año <2:
            print("A", nombre, "le corresponden 7 días de vacaciones")
    elif año >= 2 and  año <= 6:
        print("A", nombre, "le corresponden 15 días de vacaciones")
    elif año >= 7:
        print("A", nombre, "le corresponden 22 días de vacaciones")
    else:
        print("A", nombre, "No le corresponden días de vacaciones")


elif clave == 3:
    if año == 1 and año <2:
            print("A", nombre, "le corresponden 10 días de vacaciones")
    elif año >= 2 and  año <= 6:
        print("A", nombre, "le corresponden 20 días de vacaciones")
    elif año >= 7:
        print("A", nombre, "le corresponden 30 días de vacaciones")
    else:
        print("A", nombre, "No le corresponden días de vacaciones")

        
else:
    print("La clave del departamento no existe, vuelva a intentarlo.")


    

