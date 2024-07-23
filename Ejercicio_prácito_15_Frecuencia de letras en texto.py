texto = input("Introduce un texto: ")
letras = dict.fromkeys(texto, 0)
for character in texto:
    letras[character] += 1
print(letras)