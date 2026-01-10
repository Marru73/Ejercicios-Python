# Solución Optimizada: Tablas de Multiplicar en Formato Horizontal

# 1. Configuración: Tablas por cada bloque horizontal
tablas_por_bloque = 5

# 2. Bucle principal: Controla los bloques (1-5 y 6-10)
for inicio in range(1, 11, tablas_por_bloque):
    
    # A. Imprimir Encabezados
    for t in range(inicio, inicio + tablas_por_bloque):
        # Imprimimos directamente cada título sin saltar de línea
        print(f"TABLA DEL {t}".ljust(15), end="\t")
    
    print("\n" + "-" * 85) # Salto de línea y separador

    # B. Imprimir Operaciones (Filas)
    for m in range(1, 11): # Multiplicador (Fila 1, Fila 2...)
        for t in range(inicio, inicio + tablas_por_bloque): # Tabla (Columna 1, Columna 2...)
            # Imprimimos la celda actual y nos quedamos en la misma línea
            print(f"{t} x {m} = {t*m}".ljust(15), end="\t")
        
        # Al terminar todas las columnas de esta fila, hacemos un print vacío para saltar de línea
        print()
    
    # Espacio entre bloques
    print()