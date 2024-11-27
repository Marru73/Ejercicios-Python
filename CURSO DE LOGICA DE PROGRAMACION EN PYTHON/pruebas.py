import os
import random

archivo_texto = "archivo.txt"
with open(archivo_texto, "w") as file:
    contador = 0
    while contador <= 500:
        numero = random.randint(0, 50)
        if contador == 500:
            file.write(f"{numero}")
        else:
            file.write(f"{numero}, ")
        contador += 1




os.remove(archivo_texto)
