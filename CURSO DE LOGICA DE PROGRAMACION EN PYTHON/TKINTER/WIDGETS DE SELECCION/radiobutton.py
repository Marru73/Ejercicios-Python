import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Radiobutton")

"""
Este código sería para un solo botón:

opcion1 = tk.Radiobutton(ventana, text="Opción 1", font=("Arial", 14), fg="blue", bg="lightgray")
opcion1.pack()
"""

# Este sería para más botones:

variable_control = tk.IntVar()

opcion1 = tk.Radiobutton(ventana, text="opción 1", variable=variable_control, value=1)
opcion2 = tk.Radiobutton(ventana, text="opción 2", variable=variable_control, value=2)

opcion1.pack()
opcion2.pack()

def mostrar_seleccion():
    print("Opción seleccionada", variable_control.get())

boton = tk.Button(ventana, text="Mostrar selección", command=mostrar_seleccion)
boton.pack()

# Función para cambiar el color de la ventana según la opción que elijas:

def cambiar_color():
    color_seleccionado = variable_control.get()
    if color_seleccionado == 1:
        ventana.config(bg="red")
    elif color_seleccionado == 2:
        ventana.config(bg="blue")

opcion1 = tk.Radiobutton(ventana, text="Rojo", variable=variable_control, value=1, command=cambiar_color)
opcion2 = tk.Radiobutton(ventana, text="Azul", variable=variable_control, value=2, command=cambiar_color)

opcion1.pack()
opcion2.pack()


ventana.mainloop()