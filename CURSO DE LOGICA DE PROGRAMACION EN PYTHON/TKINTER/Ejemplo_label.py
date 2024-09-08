import time
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Label")
ventana.geometry("600x400")

etiqueta = tk.Label(ventana, text="Hola, soy un Label")
etiqueta.config(fg="blue", bg="yellow", font=("Arial", 14, "italic"))
etiqueta.pack()

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, actualizar_hora)

actualizar_hora()

ventana.mainloop()