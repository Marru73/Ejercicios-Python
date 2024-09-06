import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Label")
ventana.geometry("600x400")

etiqueta = tk.Label(ventana, text="Lo de abajo es un Entry")
etiqueta.config(fg="blue", bg="yellow", font=("Arial", 14, "italic"))
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.config(fg="blue", bg="lightgray", font=("Arial", 12))
entrada.pack()

entrada.insert(0, "NOMBRE")


def aplicar_texto():
    texto = entrada.get()
    etiqueta.config(text=texto)

boton_aplicar = tk.Button(ventana, text="Aplicar texto", command=aplicar_texto)
boton_aplicar.pack()

ventana.mainloop()