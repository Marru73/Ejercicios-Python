string = input("Introduce la frase: ")
palabra = input("Introduce la palabra invertir de la frase: ")
palabra_invertida = ""
indice = string.find(palabra)
for caracter in palabra:
    palabra_invertida = caracter + palabra_invertida
frase_final = string[0:indice] + palabra_invertida + string[indice-1 + len(palabra) + 1:]
frase_final = frase_final.upper()
frase_final = frase_final.center(len(string)+10, "*")
print(f"La frase final es: {frase_final}")
