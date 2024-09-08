import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Label")
ventana.geometry("600x400")

boton = tk.Button(ventana, text="Presione aquí")
boton.config(fg="white", bg="green", font=("Arial", 12))
boton.pack()

etiqueta = tk.Label(ventana, text="Hola, soy Marrufo")
etiqueta.pack()

def cambiar_texto():
    etiqueta.config(text="¡Botón presionado!")

boton.config(command=cambiar_texto)

ventana.mainloop()