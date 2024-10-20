"""import random
contador1 = 0
contador2 = 0
resultado1 = ""
resultado2 = ""
jugador = 0
while True:
    jugador = random.randint(1, 2)
    if jugador == 1:
        contador1 += 1
    elif jugador == 2:
        contador2 +=1

    if contador1 == 0:
        resultado1 = 'Love'
        print(f" {resultado1} - {resultado2}")
    elif contador1 == 1:
        resultado1 = '15'
        print(f" {resultado1} - {resultado2}")
    elif contador1 == 2:
        resultado1 = '30'
        print(f" {resultado1} - {resultado2}")
    elif contador1 == 3:
        resultado1 = '40'
        print(f" {resultado1} - {resultado2}")
    elif contador2 == 0:
        resultado2 = 'Love'
        print(f" {resultado1} - {resultado2}")
    elif contador2 == 1:
        resultado2 = '15'
        print(f" {resultado1} - {resultado2}")
    elif contador2 == 2:
        resultado2 = '30'
        print(f" {resultado1} - {resultado2}")
    elif contador2 == 3:
        resultado2 = '40'
        print(f" {resultado1} - {resultado2}")

    elif contador1 == 4 and contador2 <= 2:
        print(f"El jugador1 ha ganado el juego por {resultado1} - {resultado2}")   
        break
    elif contador2 == 4 and contador1 <=2:
        print(f"El jugador2 ha ganado el juego por {resultado1}a {resultado2}")   
        break
    elif contador1 == 3 and contador2 == 3:
        print('DEUCE')
        break
"""
    

            
import random

def punto_ganado_por():
    """Devuelve de forma aleatoria el nombre del jugador que gana el punto."""
    return random.choice(["Jugador 1", "Jugador 2"])

def imprimir_puntaje(puntaje_j1, puntaje_j2):
    """Imprime el puntaje actual de cada jugador."""
    puntuaciones = ["0", "15", "30", "40"]
    if puntaje_j1 < 4 and puntaje_j2 < 4:
        print(f"Puntaje: Jugador 1: {puntuaciones[puntaje_j1]} - Jugador 2: {puntuaciones[puntaje_j2]}")
    elif puntaje_j1 == puntaje_j2:
        print("Puntaje: Deuce")
    else:
        ventaja = "Jugador 1" if puntaje_j1 > puntaje_j2 else "Jugador 2"
        print(f"Puntaje: Ventaja {ventaja}")

def juego_de_tenis():
    puntaje_j1 = 0
    puntaje_j2 = 0
    
    while True:
        ganador_punto = punto_ganado_por()
        print(f"¡Punto para {ganador_punto}!")
        
        if ganador_punto == "Jugador 1":
            puntaje_j1 += 1
        else:
            puntaje_j2 += 1
        
        # Si ambos jugadores tienen 3 puntos (equivalente a 40), entran en deuce.
        if puntaje_j1 >= 3 and puntaje_j2 >= 3:
            if puntaje_j1 == puntaje_j2:
                imprimir_puntaje(puntaje_j1, puntaje_j2)
            elif abs(puntaje_j1 - puntaje_j2) == 1:
                imprimir_puntaje(puntaje_j1, puntaje_j2)
            elif abs(puntaje_j1 - puntaje_j2) >= 2:
                ganador = "Jugador 1" if puntaje_j1 > puntaje_j2 else "Jugador 2"
                print(f"¡{ganador} gana el juego!")
                break
        else:
            if puntaje_j1 >= 4:
                print("¡Jugador 1 gana el juego!")
                break
            elif puntaje_j2 >= 4:
                print("¡Jugador 2 gana el juego!")
                break
            
        imprimir_puntaje(puntaje_j1, puntaje_j2)

# Ejecutar el juego de tenis
juego_de_tenis()








 

            