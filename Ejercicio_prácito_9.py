frase = input("Introduce una frase: ")
letra = input("¿Cón qué letra quieres finalizar el bucle?: ")
character=""
for character in frase:
    if character.lower() == letra.lower():
        break
    elif character.lower() == "a":
        continue
    elif character.lower() == "e":
        continue
    elif character.lower() == "i":
        continue
    elif character.lower() == "o":
        continue
    elif character.lower() == "u":
        continue
    print(character, end="")

