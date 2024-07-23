# Con istitle() verifica si la primera letra de la cadena está en mayúsculas y el resto en minúsculas y devolverá True o False. El método se escribe variable.istitle().
# Tittle() lo que hará es escribir la cadena correctamente, poniendo la primera letra en mayúsculas y el resto en minúscula. Se escribe variable.title().
first_name = input("Nombre: ")
last_name = input("Apellido: ")
full_name = f"{first_name} {last_name}"

print()
print(f"¿El formato del método title() se ha aplicado?: {full_name.istitle()}")
print(f"Aplicando el método title(): {full_name.title()}")
print(f"Volvemos a imprimir el nombre: {full_name}")

print()
full_name = full_name.title()
print(f"¿El formato del método title() se ha aplicado?: {full_name.istitle()}")
print(f"Se ha aplicado el método title() de manera permanente: {full_name}")

