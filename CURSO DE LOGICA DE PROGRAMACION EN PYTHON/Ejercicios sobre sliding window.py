
"""🧠 EJERCICIO 1 — Elegir la estructura correcta (y justificarla)

Tienes una lista de números enteros que representa IDs de usuarios que han realizado una acción:

ids = [4, 7, 2, 7, 4, 9, 2, 4, 10, 7, 3, 2, 9, 9, 4]


Quiero que hagas tres cosas, pero no de cualquier manera:

✅ Parte A — Usuarios únicos

Obtén los IDs sin duplicados.

Pero quiero:

la forma más clara

la más eficiente

y que puedas explicar por qué esa estructura es la correcta

✅ Parte B — Conteo de ocurrencias

Calcula cuántas veces aparece cada ID.

Requisitos:

resultado en un dict

sin usar list.count() en un bucle (eso sería O(n²))

✅ Parte C — IDs que aparecen más de una vez

Obtén un conjunto (set) con los IDs que aparecen 2 o más veces.

Pero:

no recorras la lista más veces de las necesarias

aprovecha lo que ya calculaste antes si tiene sentido"""

from collections import Counter

ids = [4, 7, 2, 7, 4, 9, 2, 4, 10, 7, 3, 2, 9, 9, 4]
print(ids)

# Parte A
ids_sin_duplicados = set(ids)
print(ids_sin_duplicados)

# Parte B

conteo = Counter(ids) # Se utiliza Counter que está importado de la librería "collections" que hemos cargado al principio.
print(conteo)

"""La forma que se utilizaría sin usar la librería collectins sería:
conteo = {}

for n in ids:
    conteo[n] = conteo.get(n, 0) + 1
    

"""
#parte C
repetidos = {n for n, count in conteo.items() if count >= 2}
print(repetidos)

"""
🔥 EJERCICIO 2 — Primer elemento repetido (en O(n))

Te doy una lista:

ids = [5, 3, 8, 2, 9, 1, 3, 7, 8]

Objetivo:

Encontrar el primer ID que se repite
(en este caso sería 3).

Reglas:

❌ no usar count

❌ no usar doble bucle

✅ solo una pasada por la lista

✅ usa la estructura adecuada

    """

ids = [5, 3, 8, 2, 9, 1, 3, 7, 8]
def primer_repetido(ids):
    vistos = set()

    for x in ids:
        if x in vistos:
            return x
        vistos.add(x)

    return None
print(primer_repetido(ids))
        
"""
🔥 EJERCICIO 3 — Ventana deslizante (sliding window)

Esto es pensamiento algorítmico intermedio y se usa muchísimo.

Problema

Tienes una lista de números:

nums = [2, 1, 5, 1, 3, 2, 6]
k = 3


Queremos encontrar la suma máxima de cualquier sublista contigua de tamaño k.

Ejemplos de ventanas:

[2, 1, 5] → suma 8

[1, 5, 1] → suma 7

[5, 1, 3] → suma 9

[1, 3, 2] → suma 6

[3, 2, 6] → suma 11 ✅

Resultado: 11

❌ Prohibido

recalcular la suma completa en cada ventana (eso sería O(n·k))

✅ Objetivo

una sola pasada → O(n)

reutilizar el cálculo anterior  
    """

nums = [2, 1, 5, 1, 3, 2, 6]
k = 3

window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum = window_sum + nums[i] - nums[i - k]
    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)

""" 
🔥 Mini-reto final de este ejercicio

Completa esta idea:

guarda también el índice cuando haya nuevo máximo

al final devuelve la sublista

Estructura:

window_sum = sum(nums[:k])
max_sum = window_sum
end_index = k - 1

for i in range(k, len(nums)):
    window_sum = window_sum + nums[i] - nums[i - k]
    if window_sum > max_sum:
        max_sum = window_sum
        end_index = i

sublista = nums[end_index - k + 1 : end_index + 1]


Intenta escribirlo tú completo, ejecútalo, y dime qué te devuelve.
Con esto ya cierras el concepto de sliding window como un pro. 💪🔥
"""

nums = [2, 1, 5, 1, 3, 2, 6]
k = 3

# inicializamos la primera ventana
window_sum = sum(nums[:k])
window_max = window_sum
end_index = k - 1  # índice final de la ventana actual con máximo

# recorremos el resto de la lista
for i in range(k, len(nums)):
    window_sum = window_sum + nums[i] - nums[i - k]  # update de la ventana
    if window_sum > window_max:
        window_max = window_sum
        end_index = i  # actualizamos dónde termina la ventana máxima

# obtenemos la sublista del máximo
sublista = nums[end_index - k + 1 : end_index + 1]
print(f"La sublista con suma máxima es: {sublista} y su suma es: {window_max}")

"""🔥 EJERCICIO 3 — Sliding Window Avanzado

Tenemos una lista de temperaturas diarias (en ºC) de una semana:

temperaturas = [15, 18, 21, 20, 19, 23, 22, 24]
k = 4

Objetivo:

Encuentra la sublista de k días consecutivos con la temperatura promedio más alta.

Devuelve la sublista y el promedio.

Hazlo en una sola pasada, sin recalcular la suma completa cada vez.

Reglas:

❌ No uses sum() dentro del bucle.

✅ Usa sliding window (actualiza suma/estado cada vez).

✅ Devuelve sublista y promedio máximo."""


temperaturas = [15, 18, 21, 20, 19, 23, 22, 24]
k = 4

window_sum = sum(temperaturas[:k])
window_max = window_sum
end_index = k - 1

for i in range(k, len(temperaturas)):
    window_sum = window_sum + temperaturas[i] - temperaturas[i - k]
    if window_sum > window_max:
        window_max = window_sum
        end_index = i
promedio = window_max/k
sublista = temperaturas[end_index - k + 1: end_index + 1]
print(f"La sublista es: {sublista} y el promedio es: {promedio}")

"""🔥 EJERCICIO 4 — Sliding Window Variable + Condición

Lista de ventas diarias (unidades vendidas):

ventas = [5, 2, 6, 1, 3, 2, 8, 4, 5, 7]

Objetivo:

Encuentra la sublista contigua más larga cuya suma no supere 15 unidades.

Devuelve la sublista y su suma.

Hazlo en una sola pasada y sin recalcular la suma completa cada vez.

Pistas:

Aquí la ventana no tiene tamaño fijo.

Necesitas mantener dos índices: inicio y fin de la ventana actual.

Cada vez que la suma exceda 15:

mueve el inicio hacia la derecha hasta que la suma vuelva a estar ≤ 15.

Si la suma está dentro del límite y la ventana es más larga que la máxima conocida → actualiza resultado."""

ventas = [5, 2, 6, 1, 3, 2, 8, 4, 5, 7]
i = 0
mayor_sublista: list[int] = []
suma_maxima = 0
suma_actual = 0

# En Python, es más limpio usar un for para el puntero derecho (j)
# 'j' representa el final de nuestra ventana actual
for j in range(len(ventas)):
    # 1. Expandimos la ventana añadiendo el nuevo elemento
    suma_actual += ventas[j]
    
    # 2. Mientras la suma sea mayor a 15, achicamos por la izquierda (i)
    # Esto asegura que la ventana siempre sea válida antes de medirla
    while suma_actual > 15 and i <= j:
        suma_actual -= ventas[i]
        i += 1
    
    # 3. Ahora que la ventana es válida (suma <= 15), medimos
    sublista_actual = ventas[i : j + 1] # j+1 porque el slice es exclusivo
    
    if len(sublista_actual) > len(mayor_sublista):
        mayor_sublista = sublista_actual
        suma_maxima = suma_actual

print(f"La sublista más larga es: {mayor_sublista}")
print(f"Longitud: {len(mayor_sublista)} | Suma: {suma_maxima}")

# Tip Pro: Usar 'suma_actual += ...' y 'suma_actual -= ...' es mucho más
# eficiente que hacer 'sum(ventas[i:j])' en cada vuelta del bucle.



# --- El mismo ejercicio anterior pero usando una función ---

from typing import List, Tuple


def sublista_mas_larga_bajo_limite(nums: List[int], limite: int) -> Tuple[List[int], int]:
    """
    Devuelve la sublista contigua más larga cuya suma es <= limite,
    junto con la suma de esa sublista.

    Complejidad: O(n)
    """

    inicio = 0
    suma_actual = 0

    mejor_i = 0
    mejor_j = -1

    for fin in range(len(nums)):
        # expandimos ventana por la derecha
        suma_actual += nums[fin]

        # encogemos por la izquierda si superamos el límite
        while suma_actual > limite:
            suma_actual -= nums[inicio]
            inicio += 1

        # actualizamos mejor ventana si es más larga
        if fin - inicio > mejor_j - mejor_i:
            mejor_i = inicio
            mejor_j = fin

    sublista = nums[mejor_i : mejor_j + 1]
    suma = sum(sublista)

    return sublista, suma


# --- uso de la función ---

ventas = [5, 2, 6, 1, 3, 2, 8, 4, 5, 7]
limite = 15

sublista, suma = sublista_mas_larga_bajo_limite(ventas, limite)

print(f"La sublista más larga es: {sublista}")
print(f"Longitud: {len(sublista)} | Suma: {suma}")

#------------------------------------------------------#

"""
🟢 EJERCICIO 1 — Sublista más larga con suma ≤ límite
nums = [4, 2, 1, 7, 3, 2, 5, 1, 1, 6]
limite = 8

Objetivo:

Encuentra la sublista contigua más larga cuya suma sea ≤ 8
"""
from typing import List, Tuple


def sublista_mas_larga_con_limite(nums: List[int], limite: int) -> Tuple[List[int], int]:
    """
    Devuelve la sublista contigua más larga cuya suma es <= limite.
    Devuelve también la suma total de la sublista.
    """

    inicio = 0
    suma_actual = 0

    mejor_i = 0
    mejor_j = -1

    for fin in range(len(nums)):
        suma_actual += nums[fin]

        while suma_actual > limite:
            suma_actual -= nums[inicio]
            inicio += 1

        if fin - inicio > mejor_j - mejor_i:
            mejor_i = inicio
            mejor_j = fin

    sublista = nums[mejor_i : mejor_j + 1]
    suma = sum(sublista)

    return sublista, suma


nums = [4, 2, 1, 7, 3, 2, 5, 1, 1, 6]
limite = 8

sublista, suma = sublista_mas_larga_con_limite(nums, limite)

print(f"La sublista más larga es: {sublista}")
print(f"Longitud: {len(sublista)} | Suma: {suma}")


"""🟢 EJERCICIO 2 — Sublista más larga con suma < límite
nums = [1, 2, 3, 4, 1, 1, 1, 5, 2]
limite = 6

Objetivo:

Sublista contigua más larga con suma estrictamente menor que 6.
"""

from typing import Tuple, List

def sublista_mas_larga_con_limite(nums: List[int], limite: int) -> Tuple[List[int], int]:
    """Devuelve la sublista contigua más larga cuya suma es < limite.
        Devuelve también la suma total de la sublista.
    """

    inicio = 0
    suma_actual = 0

    mejor_i = 0
    mejor_j = -1

    for fin in range(len(nums)):
        suma_actual += nums[fin]

        while suma_actual >= limite:
            suma_actual -= nums[inicio]
            inicio += 1

        if fin - inicio > mejor_j - mejor_i:
            mejor_i = inicio
            mejor_j = fin

    sublista = nums[mejor_i : mejor_j + 1]
    suma = sum(sublista)

    return sublista, suma


nums = [1, 2, 3, 4, 1, 1, 1, 5, 2]
limite = 6

sublista, suma = sublista_mas_larga_con_limite(nums, limite)

print(f"La sublista más larga es: {sublista}")
print(f"Longitud: {len(sublista)}")
print(f"Suma: {suma}")

"""
🟢 EJERCICIO 3 — Sublista más larga con suma en un rango

Datos:

nums = [2, 1, 3, 2, 4, 1, 1, 5, 1]
minimo = 5
maximo = 8

🎯 Objetivo

Encuentra la sublista contigua más larga tal que:

minimo <= suma_sublista <= maximo


Es decir, la suma tiene que estar dentro del rango, ni por debajo ni por encima.

📌 Reglas (las mismas de antes)

✔ Sliding window con dos punteros

✔ Suma incremental (+= y -=)

✔ Usar while para encoger la ventana

❌ No usar sum() dentro del bucle

✔ Guardar la mejor ventana por longitud

🧠 Pista importante (para que no te atasques)

Aquí hay dos razones para encoger la ventana:

Si la suma es mayor que maximo → hay que encoger.

Si la suma es menor que minimo → NO encoges, sigues expandiendo.

O sea:

encoges solo cuando te pasas por arriba

mides solo cuando estás dentro del rango
    """

from typing import List, Tuple


def sublista_mas_larga_en_rango(nums: List[int], minimo: int, maximo: int) -> Tuple[List[int], int]:
    """
    Devuelve la sublista contigua más larga cuya suma cumple:
    minimo <= suma <= maximo
    Devuelve también la suma de esa sublista.
    """

    inicio = 0
    suma_actual = 0

    mejor_i = 0
    mejor_j = -1

    for fin in range(len(nums)):
        suma_actual += nums[fin]

        # encogemos solo si superamos el máximo
        while suma_actual > maximo:
            suma_actual -= nums[inicio]
            inicio += 1

        # medimos solo si estamos dentro del rango
        if minimo <= suma_actual <= maximo:
            if fin - inicio > mejor_j - mejor_i:
                mejor_i = inicio
                mejor_j = fin

    sublista = nums[mejor_i : mejor_j + 1]
    suma = sum(sublista)

    return sublista, suma


nums = [2, 1, 3, 2, 4, 1, 1, 5, 1]
minimo = 5
maximo = 8

sublista, suma = sublista_mas_larga_en_rango(nums, minimo, maximo)

print(f"La sublista más larga es: {sublista}")
print(f"Longitud: {len(sublista)}")
print(f"Suma: {suma}")

"""🟢 EJERCICIO 4 — Sublista más larga con suma ≤ límite (clásico)

👉 Ya lo hiciste parecido, pero quiero que lo rehagas sin mirar lo anterior.

nums = [3, 1, 2, 1, 1, 5, 1, 2, 3]
limite = 6

Objetivo:

Encontrar la sublista contigua más larga cuya suma sea menor o igual que 6."""

from typing import List, Tuple

def sublista_mas_larga(nums: List[int], limite: int) -> Tuple[List[int], int]:
    """Devuelve la sublista más larga donde la suma <= limite.
    También devuelve la suma de la misma.
    """

    inicio = 0
    suma_actual = 0

    mejor_i = 0
    mejor_j = -1

    for fin in range(len(nums)):
        suma_actual += nums[fin]

        while suma_actual >= limite:
            suma_actual -= nums[inicio]
            inicio += 1
        
        if fin - inicio > mejor_j - mejor_i:
            mejor_i = inicio
            mejor_j = fin

    sublista = nums[mejor_i : mejor_j+1]
    suma = sum(sublista)

    return sublista, suma

nums = [3, 1, 2, 1, 1, 5, 1, 2, 3]
limite = 6

sublista, suma = sublista_mas_larga(nums, limite)

print(f"La sublista más larga es: {sublista}")
print(f"Longitud: {len(sublista)}")
print(f"Suma: {suma}")


"""🟡 EJERCICIO 5 — suma EXACTA
nums = [1, 2, 3, 2, 1, 1, 1, 3]
k = 5

Objetivo:

Sublista contigua más larga cuya suma sea exactamente 5.
"""
from typing import List, Tuple

def sublista_mas_larga_suma_igual_limite(nums: List[int], limite: int) -> Tuple[List[int], int]:
    """Devuelve la sublista más larga cuya suma == limite
    y la suma de esa sublista.
"""

    inicio = 0
    suma_actual = 0

    mejor_i = 0
    mejor_j = -1

    for fin in range(len(nums)):
        suma_actual += nums[fin]

        while suma_actual > limite:
            suma_actual -= nums[inicio]
            inicio += 1
        if suma_actual == limite:
            if fin - inicio > mejor_j - mejor_i:
                mejor_i = inicio
                mejor_j = fin

    sublista = nums[mejor_i : mejor_j + 1]
    suma = sum(sublista)

    return sublista, suma
    
nums = [1, 2, 3, 2, 1, 1, 1, 3]
limite = 5

sublista, suma = sublista_mas_larga_suma_igual_limite(nums, limite)

print(f"La sublista más larga es: {sublista}")
print(f"Longitud: {len(sublista)}")
print(f"Suma: {suma}")
