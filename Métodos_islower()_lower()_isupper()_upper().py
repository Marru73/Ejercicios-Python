# Tanto islower() como isupper() lo que hacen es revisar si todas las letras de un String están en minúsculas o mayúsculas respectivamente.El método sería variable.islower() o variable isupper()
# Con lower() convertimos todo el string a minúsculas. El método sería {variable.lower()}
# Con upper() convertimos todo el string a minúsculas. El método sería {variable.upper()}
string =input("Introduce un String: ")

print(f"\n¿Todas las letras están en minúsculas?: {string.islower()}")
string = string.lower()
print (f"String en ninúsculas: {string}")

print (f"\n¿Todas las letras están en mayúsculas?: {string.isupper()}")
print (f"String en mayúsculas: {string.upper()}")
print (f"String original: {string}")