frase = input("Introduce una frase: ")
palabra = input("Introduce la palabra que quieres eliminar de la frase: ")

indice = frase.find(palabra)
Frase_final = frase[0:indice] + frase[indice + len(palabra)+1:] # Aquí se pone +1 para que no haya dos espacios unidos al hacer el corte de la palabra a eliminar.
print(Frase_final)

