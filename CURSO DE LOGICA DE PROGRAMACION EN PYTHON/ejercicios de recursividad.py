### EJERCICIOS DE RECURSIVIDAD ###

"""
Ejercicio 1: El contador hacia atrás
Crea una función cuenta_atras(n: int).

Caso base: Si n es 0, imprime "¡Fuego!" y termina (return).

Caso recursivo: Imprime n y llama a cuenta_atras(n - 1).

Nota: Fíjate cómo en cada paso restamos 1 para acercarnos al 0 (nuestro caso base).
"""

import time

def cuenta_atras(n: int) -> None:
    Realiza una cuenta regresiva recursiva con efecto visual.
    
    time.sleep(1)
    
    # Caso Base: El momento de parar
    if n == 0:
        print("¡¡¡ FUEGO !!!")
        return # Aquí termina esta llamada a la función

    # Caso Recursivo: La acción y la siguiente llamada
    print(n)
    cuenta_atras(n - 1)

# Ejecución
cuenta_atras(3) # Probamos con 3 para no esperar tanto


"""
El siguiente reto: Ejercicio 2 (El Sumatorio)Aquí es donde la cosa se pone seria. 
En el anterior solo imprimías, ahora quiero que la función devuelva (return) un valor.
Reto: Crea una función sumatorio(n: int) -> int que sume todos los números desde
n hasta 1.Si n = 3, la función debe devolver 6 (porque $3 + 2 + 1 = 6$).
Pista de lógica pro: "El sumatorio de 3 es igual a 3 + el sumatorio de 2".
Pista del Caso Base: ¿Cuál es el número más pequeño que podrías recibir donde ya sabes 
la respuesta sin sumar nada?¿Te atreves a escribir la lógica del return recursivo? 
Recuerda: Empieza desde el Caso Base.
"""

def sumatorio(n: int) -> int:
    if n == 1:
        return 1
    return n + sumatorio(n-1)

print(sumatorio(10))
    

def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    if n < 0:
        print("Número incorrecto. Introduce un número positivo.")
        return 0
        
    return n * factorial(n-1)

print(factorial(-5))


"""
Siguiente Reto: Ejercicio 4 (Invertir una cadena)
Este ejercicio es fundamental para entender cómo la recursividad maneja los datos secuenciales (como strings o listas).

El objetivo: Crear una función invertir_cadena(texto: str) -> str. Si le pasas "Python", debe devolver "nohtyP".

Reglas del juego:

No puedes usar texto[::-1] (el truco de Python).

Debes usar recursividad.

Pistas para construir la lógica:

Caso Base: Si el texto está vacío ("") o tiene una sola letra, ¿qué devuelves? (Es el momento en que ya no puedes "trocear" más).

Caso Recursivo: Piensa en esto: "Invertir 'Hola' es lo mismo que coger la última letra ('a') y ponerla delante de la inversión de 'Hol'".

Herramienta técnica: Recuerda el slicing. texto[-1] es la última letra. texto[:-1] es todo el texto menos la última letra.
"""


def invertir_cadena(texto: str) -> str:
    """
    Función principal (Envoltorio): 
    Valida la entrada una sola vez antes de iniciar la recursión.
    """
    # 1. Validación única
    if len(texto) < 2:
        print("AVISO: El texto debe contener al menos dos caracteres para ser invertido.")
        return texto # Devolvemos el texto tal cual sin iniciar la recursión

    # 2. Si la validación pasa, llamamos a la lógica recursiva
    return _invertir_recursivo(texto)

def _invertir_recursivo(texto: str) -> str:
    """
    Función Ayudante (Helper): 
    Contiene la lógica recursiva pura, sin distracciones de validación.
    """
    # Caso Base (Silencioso)
    if len(texto) <= 1:
        return texto
    
    # Caso Recursivo
    return texto[-1] + _invertir_recursivo(texto[:-1])

# Pruebas:
print(f"Resultado 1: {invertir_cadena('A')}")     # Dispara el aviso
print(f"Resultado 2: {invertir_cadena('Python')}") # No dispara aviso, invierte normal

""" 

El Gran Desafío Final: Ejercicio 5 (Estructuras Anidadas)
Fran, este es el ejercicio que separa a los programadores básicos de los que realmente entienden la lógica profunda. Es un problema real que te encontrarás procesando archivos JSON o bases de datos complejas.

El reto: Sumar todos los números de una lista que contiene... ¡otras listas! Ejemplo: lista_loca = [1, [2, [3, 4]], 5] El resultado debería ser 15.

Tu caja de herramientas (Solo lo que sabes):

Sabes usar for elemento in lista:

Sabes que type(elemento) == list te dice si algo es una lista.

Sabes que type(elemento) == int te dice si es un número.

Pista de lógica pro: Crea una función suma_profunda(lista). Dentro del for:

Si el elemento es un número, súmalo a un acumulador.

Si el elemento es una lista, ¡llama a suma_profunda pasando esa sub-lista y suma el resultado!
"""

def suma_anidada(lista):
    total = 0

    for e in lista:
        if isinstance(e, list):
            total += suma_anidada(e)
        else:
            total += e

    return total


print(suma_anidada([1, [2, [3, 4]], 5]))

"""
def limpiar_datos(lista_mixta: list):
    strings = []
    enteros = [] 
    for e in lista_mixta:
        if isinstance(e, int):
            enteros.append(e)
        elif isinstance(e, str):
            strings.append(e)
    return enteros, strings
lista_mixta = [10, "Hola", 20, "Mundo", 30]
print(limpiar_datos(lista_mixta))
"""

def super_suma(datos: list) -> int:
    total = 0
    for e in datos:
        if isinstance(e, int):
            total += e
        elif isinstance(e, list):
            total += super_suma(e)
        else:
            continue

    return total

datos = [1, "error", [2, [3, "salta", 4], "nada"], 5]
print(super_suma(datos))