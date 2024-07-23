print("Sistema para calcular el promedio de un alumno.")
nombre = input("Introduce tu nombre: " )

matematicas = int(input(nombre + " ¿Cuál es tu calificación de matemáticas?: "))
quimica = int(input(nombre + " ¿Cuál es tu calificación de quimica?: "))
biologia = int(input(nombre + " ¿Cuál es tu calificación de biología?: "))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 6:
    print ('Felicidades ' + nombre + ' "Aprobaste" con un promedio de: ', promedio)

print ("Fin.")
