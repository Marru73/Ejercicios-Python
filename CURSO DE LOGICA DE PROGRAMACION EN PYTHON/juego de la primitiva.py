"""
# forma normal

import random

numeros = random.sample(range(1, 50), 7)
numeros.sort()
numeros_str = " - ".join(str(n) for n in numeros[:6])

reintegro = random.randint(0, 9)

print(f"Los números ganadores son: {numeros_str}")
print(f" El número complementario es el {numeros[6]}")
print(f"El reintegro es el {reintegro}")
"""

# Metido en funciones:
# Como lo he hecho yo

"""
# Apuestas Usuario

import random


def generar_apuesta():
    numeros = random.sample(range(1, 50), 6) 
    numeros.sort()
    reintegro = random.randint(1, 9)
    return numeros, reintegro


def mostrar_resultado(numeros, reintegro):
    ganadores = " - ".join(str(n) for n in numeros)
    print()
    print(f"Tus números que juegas son: {ganadores}")
    print(f"Tu reintegro es el {reintegro}")


# ---- Programa principal ----
numeros, reintegro = generar_apuesta()
mostrar_resultado(numeros, reintegro)


# Resultado del sorteo:                                                                  
def generar_apuesta_sorteo():
    numeros_sorteo = random.sample(range(1,50),7)
    numeros_sorteo.sort()
    reintegro_sorteo = random.randint(1,9)
    return numeros_sorteo, reintegro_sorteo

def mostrar_resultados_sorteo(numeros_sorteo, reintegro_sorteo):
    ganadores_sorteo = " - ".join(str(n) for n in numeros_sorteo[:6])
    complementario_sorteo = numeros_sorteo[6]
    print()
    print(f"Los números ganadores del sorteo son: {ganadores_sorteo}")
    print(f"El número complementario del sorteo es el {complementario_sorteo}")
    print(f"El reintegro del sorteo es el {reintegro_sorteo}")

numeros_sorteo, reintegro_sorteo = generar_apuesta_sorteo()
mostrar_resultados_sorteo(numeros_sorteo, reintegro_sorteo)


aciertos_numeros = sum(1 for n in numeros if n in numeros_sorteo[:6])
complement = numeros_sorteo[6] in numeros
reint = reintegro == reintegro_sorteo


if aciertos_numeros == 6 and reint: 
    print("Has ganado  6 números + reintegro. Has ganado el bote de 100.000.000€.")
elif aciertos_numeros == 6:
    print("Has conseguido 6 aciertos. Has ganado 1.200.000€.")
elif aciertos_numeros == 5 and complement:
    print("has acertado 5 números más el complementario. Has ganado 300.000€")
elif aciertos_numeros == 5:
    print("has acertado 5 números. Has ganado 5.000€")
elif aciertos_numeros == 4:
    print("Has acertado 4 números. Has ganado 70€")
elif aciertos_numeros == 3:
    print("Has conseguido 3 números. Has ganado 8€")
elif aciertos_numeros < 3 and reint:
    print("Solo has ganado lo jugado.")
else:
    print("No has tenido suerte en este sorteo. Prueba de nuevo para el próximo. ¡¡¡ Suerte !!!")
    """

# Corregido por ChatGPT:

import random

# ---- Funciones ----

def generar_apuesta():
    """Genera la apuesta del usuario: 6 números + reintegro"""
    numeros = random.sample(range(1, 50), 6)
    numeros.sort()
    reintegro = random.randint(0, 9)
    return numeros, reintegro

def mostrar_apuesta(numeros, reintegro):
    """Muestra los números y el reintegro del usuario"""
    numeros_str = " - ".join(str(n) for n in numeros)
    print(f"\nTus números: {numeros_str}")
    print(f"Tu reintegro: {reintegro}")

def generar_sorteo():
    """Genera el sorteo: 6 números + complementario + reintegro"""
    numeros = random.sample(range(1, 50), 6)
    numeros.sort()
    complementario = random.choice([n for n in range(1, 50) if n not in numeros])
    reintegro = random.randint(0, 9)
    return numeros, complementario, reintegro

def mostrar_sorteo(numeros, complementario, reintegro):
    """Muestra los números ganadores, complementario y reintegro"""
    numeros_str = " - ".join(str(n) for n in numeros)
    print(f"\nNúmeros ganadores del sorteo: {numeros_str}")
    print(f"Número complementario: {complementario}")
    print(f"Reintegro del sorteo: {reintegro}")

def comprobar_premio(aciertos, complementario_acertado, reintegro_acertado):
    """Devuelve mensaje según premios obtenidos"""
    if aciertos == 6 and reintegro_acertado:
        return "¡6 aciertos + reintegro! Has ganado el bote de 100.000.000€"
    elif aciertos == 6:
        return "¡6 aciertos! Has ganado 1.200.000€"
    elif aciertos == 5 and complementario_acertado:
        return "¡5 aciertos + complementario! Has ganado 300.000€"
    elif aciertos == 5:
        return "¡5 aciertos! Has ganado 5.000€"
    elif aciertos == 4:
        return "¡4 aciertos! Has ganado 70€"
    elif aciertos == 3:
        return "¡3 aciertos! Has ganado 8€"
    elif reintegro_acertado:
        return "Solo has ganado el reintegro: recuperas lo jugado"
    else:
        return "No has tenido suerte en este sorteo. ¡Prueba de nuevo!"

# ---- Programa principal ----

# Generar apuesta del usuario
numeros_usuario, reintegro_usuario = generar_apuesta()
mostrar_apuesta(numeros_usuario, reintegro_usuario)

# Generar sorteo
numeros_sorteo, complementario_sorteo, reintegro_sorteo = generar_sorteo()
mostrar_sorteo(numeros_sorteo, complementario_sorteo, reintegro_sorteo)

# Calcular aciertos
aciertos_numeros = len(set(numeros_usuario) & set(numeros_sorteo))
complementario_acertado = complementario_sorteo in numeros_usuario
reintegro_acertado = reintegro_usuario == reintegro_sorteo

# Mostrar resultado
mensaje = comprobar_premio(aciertos_numeros, complementario_acertado, reintegro_acertado)
print(f"\nResultado del sorteo: {mensaje}")
