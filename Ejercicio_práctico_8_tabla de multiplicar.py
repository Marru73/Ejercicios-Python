tabla = int(input("Introduce la tabla que quieres ver: "))
print(f"La tabla del {tabla} es:")
for indice in range(0,11):
    print(f"{tabla}  x  {indice}  =  {tabla * indice}")