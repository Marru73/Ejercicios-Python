

"""
1. La Calculadora Básica

Crea una función llamada calculadora(a, b, operacion).

Parámetros: Dos números (a, b) y un string (operacion) que puede ser "suma", "resta", "multi" o "div".

Reto: La función debe devolver (return) el resultado de la operación.

Extra: Si la operación no es válida o se intenta dividir por cero, devuelve un mensaje de error.
"""
# Definimos la función con la instrucción 'return' para devolver el valor
def calculadora(a, b, operacion):
    """Realiza operaciones básicas y devuelve el resultado."""
    
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multi":
        return a * b
    elif operacion == "div":
        if b == 0:
            return "Error: División por cero"
        return a / b
    
    # Si no coincide con ninguna operación válida
    return "Error: Operación no válida"

# --- Pruebas de la función ---

# Ahora podemos guardar los resultados en variables
resultado_suma = calculadora(10, 5, "suma")
resultado_error = calculadora(10, 0, "div")

print(f"Resultado suma: {resultado_suma}")
print(f"Prueba error: {resultado_error}")

# Gracias al return, podemos incluso operar con los resultados
total = calculadora(resultado_suma, 2, "multi")
print(f"Resultado final procesado: {total}")

"""
2. Área de un Círculo (Parámetros por defecto)

Crea una función llamada calcular_area que reciba el radio de un círculo.

Reto: Devuelve el área ($Area = \pi \times radio^2$).

Pista: Puedes usar $3.14159$ como valor de $\pi$ o importar math.

Detalle: Haz que el parámetro radio tenga un valor por defecto de 1.
"""
import math

def calcular_area(radio=1):
    """Calcula el área de un círculo y devuelve el valor con alta precisión."""
    return math.pi * (radio ** 2)

# --- Pruebas de la función (Sin variables intermedias) ---

# Llamamos a la función directamente dentro del f-string
print(f"Área con radio 3: {calcular_area(3):.2f}")

# Probamos el valor por defecto
print(f"Área por defecto (radio 1): {calcular_area():.2f}")

# NOTA: También podrías usar round() dentro de la función así:
# return round(math.pi * (radio ** 2), 2)
# Pero es mejor devolver el número completo por si luego necesitas 
# hacer cálculos científicos precisos con él.

"""
3. El Validador de Pares

Crea una función llamada es_par(numero).

Reto: Debe devolver True si el número es par y False si es impar.

Uso: Luego, usa esta función dentro de un bucle for que recorra una lista de números del 1 al 10 e imprima cuáles son pares.
"""
# Solución al Desafío 3: Validador de Pares

def es_par(numero):
    """
    Devuelve True si el número es par.
    Nota: La expresión 'numero % 2 == 0' ya devuelve un Booleano (True/False),
    por lo que no necesitamos el if/else dentro de la función.
    """
    return numero % 2 == 0

# Uso de la función dentro del bucle
print("Números pares del 1 al 10:")

for i in range(1, 11):
    # Usamos la función como condición del 'if'
    if es_par(i):
        print(f"El número {i} es par.")

"""
4. Generador de Diccionarios (K-V)

Crea una función llamada crear_perfil(nombre, edad, **otros_datos).

Reto: La función debe devolver un diccionario con toda la información.

Pista: Investiga el uso de **kwargs para recibir un número ilimitado de datos adicionales (como "ciudad", "equipo", etc.).
"""
# Solución al Desafío 4: Generador de Perfiles (Uso de **kwargs)

def crear_perfil(nombre, edad, **otros_datos):
    """
    Crea un diccionario de usuario combinando datos fijos y dinámicos.
    '**otros_datos' captura cualquier argumento extra como un diccionario.
    """
    # 1. Creamos el diccionario con los datos obligatorios
    perfil = {
        "nombre": nombre,
        "edad": edad
    }
    
    # 2. Usamos .update() para fusionar los datos extra en el perfil
    # otros_datos ya es un diccionario gracias a los **
    perfil.update(otros_datos)
    
    return perfil

# --- Pruebas de la función ---

# Ejemplo 1: Solo con datos obligatorios
usuario_simple = crear_perfil("Erik", 29)
print(f"Usuario simple: {usuario_simple}")

# Ejemplo 2: Con datos extra totalmente dinámicos
usuario_completo = crear_perfil(
    "Marrudev", 
    30, 
    ciudad="Madrid", 
    equipo="Python Team", 
    rol="Admin"
)

print(f"Usuario completo: {usuario_completo}")

# Tip Pro: El nombre 'kwargs' es una convención (KeyWord ARGumentS). 
# Lo importante son los dos asteriscos (**), que actúan como una "red"
# que atrapa cualquier argumento que pases con el formato clave=valor.

"""
5. Limpiador de Textos

Crea una función llamada limpiar_y_contar(texto).

Reto: 1. Debe quitar los espacios sobrantes al principio y al final.
2. Debe convertir todo a minúsculas.
3. Debe devolver una tupla con el texto limpio y la cantidad de caracteres que tiene.
"""
# Solución al Desafío 5: Limpiador de Textos (Tuplas y Métodos de String)

def limpiar_y_contar(texto):
    """
    Limpia espacios, convierte a minúsculas y devuelve una tupla 
    con el texto procesado y su longitud.
    """
    # .strip() elimina espacios al inicio y final
    # .lower() convierte todo a minúsculas
    texto_limpio = texto.strip().lower()
    
    # Devolvemos directamente la tupla (valor1, valor2)
    return (texto_limpio, len(texto_limpio))

# --- Pruebas de la función ---

# Ejemplo con espacios sobrantes y mayúsculas
resultado = limpiar_y_contar("   Hola, mi nombre es FRAN   ")

print(f"Resultado procesado: {resultado}")
print(f"Texto: {resultado[0]}")
print(f"Longitud: {resultado[1]}")

"""
6. El Buscador de Iniciales

Crea una función llamada filtrar_por_letra(lista_nombres, letra).

Reto: Debe devolver una nueva lista que contenga solo los nombres que empiezan por la letra indicada (sin importar si es mayúscula o minúscula).

Ejemplo: filtrar_por_letra(["Ana", "Beto", "Angel"], "a") -> ["Ana", "Angel"].
"""

# Solución al Desafío 1: Filtrar nombres por inicial

# Tu versión es excelente, aquí la tienes con el estilo de limpieza extrema
def filtrar_por_letra(lista_nombres, letra):
    """Filtra una lista de nombres según su letra inicial (Case Insensitive)."""
    
    # Normalizamos la letra a minúscula una sola vez
    busqueda = letra.lower()
    
    # Versión "Pythonic" usando List Comprehension:
    # "Crea una lista con el 'nombre' para cada 'nombre' en 'lista_nombres' 
    # SI el nombre en minúscula empieza por nuestra búsqueda"
    return [n for n in lista_nombres if n.lower().startswith(busqueda)]

# --- Pruebas de la función ---

nombres = ["Juan", "Pedro", "José", "Fernando", "julia"]

# Probamos con 'j' minúscula
print(f"Empiezan por 'j': {filtrar_por_letra(nombres, 'j')}")

# Probamos con 'J' mayúscula (debe funcionar igual)
print(f"Empiezan por 'J': {filtrar_por_letra(nombres, 'J')}")

# Tip: Al usar [n for n in lista if condicion] eliminas la necesidad 
# de crear una lista vacía y hacer el .append() manualmente.

"""
7. Calculadora de Impuestos (Flexible)

Crea una función llamada calcular_precio_final(importe, impuesto=21).

Reto: La función debe calcular el precio sumándole el porcentaje de impuesto indicado. Si el usuario no indica el impuesto, se aplicará el 21% por defecto.

Salida: El número final redondeado a 2 decimales.
"""
# Solución al Desafío 2: Calculadora de Impuestos (Versión Pro)

def calcular_precio_final(importe, impuesto=21):
    """Calcula el precio final sumando el impuesto (21% por defecto)."""
    return importe + (importe * impuesto / 100)

# 1. Captura de datos
importe = float(input("Introduce el importe: "))
entrada = input("Introduce el impuesto (deja vacío para 21%): ")

# 2. Lógica ternaria: Si hay entrada, convierte a float; si no, usa 21
impuesto = float(entrada) if entrada else 21

# 3. Resultado directo en el f-string
print(f"\nPrecio base: {importe}€")
print(f"Total con {impuesto}% IVA: {calcular_precio_final(importe, impuesto):.2f}€")

"""
 8. El Traductor de Temperaturas

Crea una función llamada convertir_clima(valor, escala_destino).

Reto: * Si escala_destino es "F", convierte el valor de Celsius a Fahrenheit ($F = C \times 1.8 + 32$).

Si es "C", convierte de Fahrenheit a Celsius ($C = (F - 32) / 1.8$).

Extra: Devuelve un mensaje de error si la escala no es "C" o "F".
"""

# Solución al Desafío 3: Traductor de Temperaturas

def convertir_clima(valor, escala_destino):
    """
    Convierte temperaturas entre Celsius y Fahrenheit.
    'escala_destino' indica a qué unidad queremos llegar.
    """
    escala = escala_destino.lower()

    if escala == "f":
        # De Celsius a Fahrenheit
        return round(valor * 1.8 + 32, 2)
    elif escala == "c":
        # De Fahrenheit a Celsius
        return round((valor - 32) / 1.8, 2)
    
    return "Error: Escala no válida (Usa 'C' o 'F')"

# --- Pruebas de la función ---

# Ejemplo 1: 30 grados Celsius a Fahrenheit
print(f"30ºC son {convertir_clima(30, 'f')}ºF")

# Ejemplo 2: 86 grados Fahrenheit a Celsius
print(f"86ºF son {convertir_clima(86, 'c')}ºC")

# Ejemplo 3: Prueba de error
print(convertir_clima(25, "Z"))


""" 9. Estadísticas de Frase

Crea una función llamada analizar_texto(frase).

Reto: Debe devolver un diccionario con tres claves:

palabras: el número total de palabras.

caracteres: el número total de letras (sin contar espacios).

mayusculas: cuántas letras en mayúscula hay.
"""

# Solución al Desafío 4: Estadísticas de Frase (Análisis de Texto)

def analizar_texto(frase):
    """
    Analiza una frase y devuelve estadísticas sobre palabras, 
    caracteres (sin espacios) y mayúsculas.
    """
    palabras = frase.split()
    
    # 1. Contamos caracteres eliminando los espacios
    # Usamos .replace(" ", "") para que no cuente los huecos
    caracteres_sin_espacios = len(frase.replace(" ", ""))
    
    # 2. Contamos mayúsculas recorriendo cada LETRA, no cada palabra
    # Usamos una "Generator Expression" para ser más limpios:
    # Sumamos 1 por cada letra que sea mayúscula
    mayusculas = sum(1 for letra in frase if letra.isupper())

    return {
        "palabras": len(palabras),
        "caracteres": caracteres_sin_espacios,
        "mayusculas": mayusculas
    }

# --- Prueba de la función ---
resultado = analizar_texto("Hola, mi nombre es Francisco José")

print("Análisis de la frase:")
for clave, valor in resultado.items():
    print(f"- {clave.capitalize()}: {valor}")


"""
10. El Cajero Automático (Simulación)

Crea una función llamada gestionar_banco(saldo_actual, cantidad, operacion="ingresar").

Reto: * Si la operación es "ingresar", suma la cantidad al saldo.

Si es "retirar", resta la cantidad, pero solo si hay saldo suficiente. Si no, devuelve un mensaje de "Fondos insuficientes".

Retorno: El nuevo saldo o el mensaje de error.
"""

# Solución al Desafío 5: El Cajero Automático (Simulación de Banco)

def gestionar_banco(saldo_actual, cantidad, operacion="ingresar"):
    """
    Gestiona ingresos y retiradas de saldo. 
    Devuelve el nuevo saldo o un mensaje de error.
    """
    op = operacion.lower()

    if op == "ingresar":
        saldo_actual += cantidad
    elif op == "retirar":
        if cantidad > saldo_actual:
            return "SALDO INSUFICIENTE"
        saldo_actual -= cantidad
    else:
        return "Error: Opción incorrecta. Use 'ingresar' o 'retirar'."

    # Centralizamos el retorno de éxito para evitar repetir código
    return f"Su saldo actual es de {saldo_actual}€"

# --- Pruebas de la función ---

# Ejemplo de ingreso (200 + 4800 = 5000)
print(gestionar_banco(200, 4800, "ingresar"))

# Ejemplo de retirada con éxito
print(gestionar_banco(5000, 1000, "retirar"))

# Ejemplo de fondos insuficientes
print(gestionar_banco(500, 1000, "retirar"))

"""
11. El Guardián de Contraseñas

Crea una función llamada validar_password(password).

Reto: Debe devolver True solo si:

Tiene al menos 8 caracteres.

Contiene al menos un número (puedes usar un bucle for y .isdigit() para comprobarlo).

Retorno: True si cumple ambas, False si no.
"""

# Desafío 11: El Guardián de Contraseñas

def validar_password(password):
    """
    Valida si una contraseña cumple con los requisitos de seguridad:
    1. Longitud mínima de 8 caracteres.
    2. Contiene al menos un número.
    """
    # Requisito 1: Verificamos la longitud (Return temprano)
    if len(password) < 8:
        return False
    
    # Requisito 2: Verificamos si hay al menos un número
    # Recorremos cada carácter para ver si alguno es un dígito
    tiene_numero = False
    for caracter in password:
        if caracter.isdigit():
            tiene_numero = True
            break # En cuanto encontramos uno, no hace falta seguir mirando
            
    return tiene_numero

# --- Pruebas de la función ---

# Caso 1: Válida (Larga y con número)
print(f"¿'Matasuegras23' es válida?: {validar_password('Matasuegras23')}")

# Caso 2: Inválida (Corta)
print(f"¿'123' es válida?: {validar_password('123')}")

# Caso 3: Inválida (Sin números)
print(f"¿'SoloLetras' es válida?: {validar_password('SoloLetras')}")

# Tip Pro: Una versión más avanzada en Python sería:
# return len(password) >= 8 and any(c.isdigit() for c in password)


"""
12. El Reloj Humano

Crea una función llamada formatear_segundos(segundos_totales).

Reto: Recibe un número entero de segundos y debe devolver un string con el formato "HH:MM:SS".

Ejemplo: formatear_segundos(3661) -> "01:01:01".

Pista: Usa los operadores // (división entera) y % (módulo).
"""

# Desafío 12: El Reloj Humano (Formateo de tiempo)

def formatear_segundos(segundos_totales):
    """
    Convierte un número entero de segundos al formato HH:MM:SS.
    Utiliza operadores de división entera (//) y módulo (%) para el cálculo.
    """
    # 1. Calculamos las horas totales
    # 3600 segundos = 1 hora
    horas = segundos_totales // 3600
    
    # 2. Calculamos los minutos
    # Primero obtenemos el resto de las horas y lo dividimos por 60
    minutos = (segundos_totales % 3600) // 60
    
    # 3. Calculamos los segundos restantes
    # Es simplemente el resto de dividir por 60
    segundos = segundos_totales % 60
    
    # Retornamos el string formateado
    # :02 asegura que si el número es menor a 10, ponga un cero delante (ej. 01)
    return f"{horas:02}:{minutos:02}:{segundos:02}"

# --- Pruebas de la función ---

# Caso 1: Una hora, un minuto y un segundo
print(f"3661 segundos equivalen a: {formatear_segundos(3661)}")

# Caso 2: Solo minutos y segundos
print(f"125 segundos equivalen a:  {formatear_segundos(125)}")

# Caso 3: Casi un día entero
print(f"86399 segundos equivalen a: {formatear_segundos(86399)}")

# Tip Pro: El operador // te da cuántas veces "cabe" un número en otro,
# y el operador % te da lo que "sobra" de esa operación.

"""
13. Contador de Palabras (Diccionarios)

Crea una función llamada frecuencia_palabras(lista_texto).

Reto: Recibe una lista de palabras y devuelve un diccionario donde las claves son las palabras y los valores son cuántas veces aparece cada una.

Ejemplo: ["sol", "luna", "sol"] -> {"sol": 2, "luna": 1}.
"""

# Ejercicio 3: Contador de Frecuencia de Palabras (Versión Pro)

def frecuencia_palabras(lista_texto):
    """
    Recibe una lista de palabras y devuelve un diccionario con su frecuencia.
    Usa el método .get() para una gestión limpia y eficiente de las claves.
    """
    frecuencias = {}
    
    for palabra in lista_texto:
        # Buscamos el valor actual de la palabra. 
        # Si no existe, .get() nos da un 0. Luego sumamos 1.
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

# --- Pruebas de funcionamiento ---

# Lista de ejemplo con palabras repetidas
mi_lista = ["sol", "luna", "tierra", "sol", "mar", "luna", "sol"]

# Llamada a la función e impresión del resultado
resultado = frecuencia_palabras(mi_lista)

print("Análisis de frecuencias:")
for palabra, cantidad in resultado.items():
    print(f"- {palabra.capitalize()}: {cantidad} veces")

# Esto devolverá: {'sol': 3, 'luna': 2, 'tierra': 1, 'mar': 1}


"""
14. Promedio con Filtro (Umbral)

Crea una función llamada promedio_selectivo(numeros, umbral).

Reto: Debe calcular y devolver el promedio de solo los números de la lista que sean mayores al umbral.

Extra: Si no hay ningún número que supere el umbral, devuelve 0.
"""

# Solución al Desafío 4: Promedio con Filtro (Umbral)

def promedio_selectivo(numeros, umbral):
    """
    Calcula el promedio de los números que superan un umbral.
    Si no hay números que cumplan, devuelve 0.
    """
    # 1. Filtramos en una sola línea usando List Comprehension
    validos = [n for n in numeros if n > umbral]

    # 2. Verificamos si la lista resultante tiene elementos
    # En Python, 'if not lista' es la forma más limpia de ver si está vacía
    if not validos:
        return 0
    
    # 3. Calculamos el promedio y devolvemos con formato profesional
    promedio = sum(validos) / len(validos)
    return f"{promedio:.2f}€"

# --- Pruebas de la función ---
datos = [2, 3, 5, 19, 33, 6]

# Prueba con umbral de 5 (debe promediar 19, 33 y 6)
resultado = promedio_selectivo(datos, 5)
print(f"Promedio de números mayores a 5: {resultado}")

# Prueba con umbral inalcanzable (debe devolver 0)
error = promedio_selectivo(datos, 100)
print(f"Resultado sin coincidencias: {error}")


"""
15. Calculadora de Envío Logístico

Crea una función llamada calcular_envio(distancia, peso, urgente=False).

Lógica:

Coste base: 5€.

Por cada kilo: +0.5€.

Por cada km: +0.1€.

Si es urgente: Se le suma un recargo fijo de 20€ al total.

Retorno: El precio total con el formato: X.XX€.
"""

# Desafío 5: Calculadora de Envío Logístico (Versión Limpia)

def calcular_envio(distancia, peso, urgente=False):
    """
    Calcula el coste total de envío basándose en distancia, peso y urgencia.
    Centraliza la lógica para evitar repetir mensajes de texto.
    """
    # 1. Definimos los costes fijos y variables
    coste_base = 5
    plus_distancia = distancia * 0.10
    plus_peso = peso * 0.50
    
    # 2. Gestionamos el recargo de urgencia de forma limpia
    # Si es urgente sumamos 20, si no, sumamos 0
    recargo_urgente = 20 if urgente else 0
    
    # 3. Calculamos el total
    total = coste_base + plus_distancia + plus_peso + recargo_urgente
    
    # 4. Creamos un desglose claro para el usuario
    desglose = (f"Plus Distancia: {plus_distancia:.2f}€ | "
                f"Plus Peso: {plus_peso:.2f}€ | "
                f"Urgente: {recargo_urgente}€")
    
    return f"{desglose} -> TOTAL: {total:.2f}€"

# --- Pruebas del sistema ---

# Caso A: Envío estándar (25km, 20kg)
print(f"PEDIDO A: {calcular_envio(25, 20)}")

# Caso B: Envío urgente (25km, 20kg, urgente=True)
print(f"PEDIDO B: {calcular_envio(25, 20, urgente=True)}")# Desafío 5: Calculadora de Envío Logístico (Versión Limpia)

def calcular_envio(distancia, peso, urgente=False):