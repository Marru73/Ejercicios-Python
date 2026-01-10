 Solución: Tablas de Multiplicar en Formato Horizontal

# 1. Configuración: ¿Cuántas tablas queremos por cada fila de la pantalla?
# Usamos 5 para que quepa bien en la terminal sin amontonarse.
tablas_por_bloque = 5

# 2. Bucle principal: Controla los "bloques" (bloque del 1-5 y bloque del 6-10)
# range(1, 11, 5) genera el número 1 y luego el 6.
for inicio_bloque in range(1, 11, tablas_por_bloque):
    
    # A. Imprimir los encabezados de las tablas del bloque actual
    # Esto imprime: "TABLA DEL 1    TABLA DEL 2..."
    for num_tabla in range(inicio_bloque, inicio_bloque + tablas_por_bloque):
        # .ljust(15) reserva 15 espacios para que las columnas no se muevan
        print(f"TABLA DEL {num_tabla}".ljust(15), end="\t")
    
    # Salto de línea después de los títulos y una línea decorativa
    print("\n" + "-" * 85)

    # B. Imprimir las filas de multiplicaciones (del 1 al 10)
    for multiplicador in range(1, 11):
        linea_actual = "" # Aquí acumularemos el texto de toda la fila
        
        # Para cada fila, recorremos las tablas que pertenecen a este bloque
        for num_tabla in range(inicio_bloque, inicio_bloque + tablas_por_bloque):
            # Creamos el texto de la operación: "1 x 1 = 1"
            operacion = f"{num_tabla} x {multiplicador} = {num_tabla * multiplicador}"
            # Añadimos la operación a la línea, ajustada a 15 espacios
            linea_actual += operacion.ljust(15) + "\t"
        
        # Una vez construida la línea con todas las tablas, la imprimimos
        print(linea_actual)
    
    # Espacio en blanco al terminar un bloque de 5 tablas antes de empezar el siguiente
    print()