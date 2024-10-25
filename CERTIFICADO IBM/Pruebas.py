import numpy as np

def generar_secuencia_numerica(minimo, maximo, paso):

    resultado = np.arange(minimo, maximo+1, paso)

    return resultado
print(generar_secuencia_numerica(0, 100, 5))