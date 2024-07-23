#Conjunción AND

print("Conjunción AND")

numero_uno = int(input("Escribe un número mayor que 2 y menor que 5: "))

if numero_uno > 2 and numero_uno < 5:
    print("El número ", numero_uno, "cumple con la condición.\n")
else:
    print("El número ", numero_uno, "NO cumple con la condición.\n")
    

#Disyunción OR

print("Disyunción OR")

palabra = input("Para cumplir la condición escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido.\n")
else:
    print("La condición NO se ha cumplido.\n")

#Negación NOT

num_uno = int(input("Introduce un número igual a 5: "))

if not num_uno == 5:
    print("\n El número es diferente de 5 y SI cumple la condición.\n")
else:
    print("\n El número es igual a 5 y NO cumple la condición.\n")
    





    
    
