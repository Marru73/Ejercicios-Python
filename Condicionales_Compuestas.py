print("Sistema para calcular el promedio de un alumno.")
nombre = input("Introduce tu nombre: " )

matematicas = int(input(nombre + " ¿Cuál es tu calificación de matemáticas?: "))
quimica = int(input(nombre + " ¿Cuál es tu calificación de quimica?: "))
biologia = int(input(nombre + " ¿Cuál es tu calificación de biología?: "))

promedio = (matematicas + quimica + biologia) / 3
"""Esta instrucción solo se pondría si queremos que no tenga decimales, sino que sea un número entero

promedio = int(promedio)

Si queremos que contenga decimales, el número de decimales lo pondremos con la instrucción Round
"""

if promedio >= 6:
    print ('Felicidades ' + nombre + ' "Aprobaste" con un promedio de: ', round(promedio,2))
else:
    print ('Lo siento ' + nombre + ' "La cagaste" con un promedio de: ', round(promedio,1))

print ("Fin.")
