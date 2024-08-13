print("*********************************************************************************")
print("* Programa que determina cuál es el número más grande de tres números *")
print("*********************************************************************************")

num_1 = int(input("Introduce el trere número: "))
num_2 = int(input("Introduce el segundo número: "))
num_3 = int(input("Introduce el tercer número: "))

if num_1 > num_2 and num_1 > num_3:
        print("el número mas grande es el número ", num_1)
elif num_2 > num_1 and num_2 > num_3:
        print("el número mas grande es el número ", num_2)
elif num_3 > num_1 and num_3 > num_2:
        print("el número mas grande es el número ", num_3)
