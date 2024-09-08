import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Label")

etiqueta = tk.Label(ventana, text="Hola, soy un Label")
# etiqueta.config(text="Nuevo texto") # Esto es para cambiar el texto anterior
etiqueta.config(fg="blue", bg="yellow", font=("Arial", 14, "italic"))
etiqueta.pack()
ventana.mainloop()