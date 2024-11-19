"""def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))"""

# Aplicando Yield from:


def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))